from unittest.mock import MagicMock, patch

from modules.transactions import add_transaction
from modules.categories import add_category
from modules.budgets import add_budget, check_budget_alerts
from modules.reports import get_monthly_report


def test_financial_balance_calculation():
    income = 5000
    expense = 3200

    balance = income - expense

    assert balance == 1800


def test_budget_remaining_amount():
    budget = 5000
    spent = 3200

    remaining = budget - spent

    assert remaining == 1800


def test_budget_exceeded():
    budget = 5000
    spent = 5500

    assert spent > budget


def test_budget_within_limit():
    budget = 5000
    spent = 3500

    assert spent < budget
    
def test_budget_warning_threshold():
    budget = 5000
    spent = 4000

    usage_percentage = (spent / budget) * 100

    assert usage_percentage >= 80
    assert usage_percentage < 100


def test_budget_exceeded_threshold():
    budget = 5000
    spent = 5000

    usage_percentage = (spent / budget) * 100

    assert usage_percentage >= 100
    
def test_balance_calculation():
    total_income = 10000
    total_expense = 6500

    balance = total_income - total_expense

    assert balance == 3500


def test_no_expense_balance():
    total_income = 5000
    total_expense = 0

    balance = total_income - total_expense

    assert balance == 5000


def test_expenses_greater_than_income():
    total_income = 3000
    total_expense = 4500

    balance = total_income - total_expense

    assert balance == -1500
    
    
def test_add_transaction_successfully():
    mock_connection = MagicMock()
    mock_cursor = MagicMock()

    mock_connection.cursor.return_value = mock_cursor

    with patch(
        "modules.transactions.create_connection",
        return_value=mock_connection
    ):

        result = add_transaction(
            "Expense",
            500,
            1,
            "Test Expense",
            "2026-09-22"
        )

    assert result is True

    mock_cursor.execute.assert_called_once()
    mock_connection.commit.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_connection.close.assert_called_once()


def test_add_transaction_database_failure():
    with patch(
        "modules.transactions.create_connection",
        return_value=None
    ):

        result = add_transaction(
            "Expense",
            500,
            1,
            "Test Expense",
            "2026-09-22"
        )

    assert result is False
    
    
def test_add_category_successfully():
    mock_connection = MagicMock()
    mock_cursor = MagicMock()

    mock_connection.cursor.return_value = mock_cursor

    with patch(
        "modules.categories.create_connection",
        return_value=mock_connection
    ):

        result = add_category("Test Category")

    assert result is True

    mock_cursor.execute.assert_called_once()
    mock_connection.commit.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_connection.close.assert_called_once()


def test_add_category_database_failure():
    with patch(
        "modules.categories.create_connection",
        return_value=None
    ):

        result = add_category("Test Category")

    assert result is False
    
def test_budget_alert_when_exceeded():

    mock_budget_status = [
        {
            "category_name": "Food",
            "budget_amount": 5000,
            "spent_amount": 5500
        }
    ]

    with patch(
        "modules.budgets.get_budget_status",
        return_value=mock_budget_status
    ):

        alerts = check_budget_alerts(9, 2026)

    assert len(alerts) == 1
    assert "Budget exceeded" in alerts[0]


def test_budget_warning_at_80_percent():

    mock_budget_status = [
        {
            "category_name": "Transport",
            "budget_amount": 5000,
            "spent_amount": 4000
        }
    ]

    with patch(
        "modules.budgets.get_budget_status",
        return_value=mock_budget_status
    ):

        alerts = check_budget_alerts(9, 2026)

    assert len(alerts) == 1
    assert "80.0%" in alerts[0]


def test_no_budget_alert_below_80_percent():

    mock_budget_status = [
        {
            "category_name": "Entertainment",
            "budget_amount": 5000,
            "spent_amount": 2000
        }
    ]

    with patch(
        "modules.budgets.get_budget_status",
        return_value=mock_budget_status
    ):

        alerts = check_budget_alerts(9, 2026)

    assert alerts == []
    
def test_monthly_report_successfully():

    mock_connection = MagicMock()
    mock_cursor = MagicMock()

    mock_connection.cursor.return_value = mock_cursor

    mock_cursor.fetchone.return_value = {
        "total_income": 10000,
        "total_expense": 6500,
        "balance": 3500
    }

    with patch(
        "modules.reports.create_connection",
        return_value=mock_connection
    ):

        report = get_monthly_report(9, 2026)

    assert report["total_income"] == 10000
    assert report["total_expense"] == 6500
    assert report["balance"] == 3500


def test_monthly_report_database_failure():

    with patch(
        "modules.reports.create_connection",
        return_value=None
    ):

        report = get_monthly_report(9, 2026)

    assert report is None
    
    
def test_transaction_rejects_negative_amount():

    result = add_transaction(
        "Expense",
        -500,
        1,
        "Invalid transaction",
        "2026-09-22"
    )

    assert result is False


def test_transaction_rejects_zero_amount():

    result = add_transaction(
        "Expense",
        0,
        1,
        "Invalid transaction",
        "2026-09-22"
    )

    assert result is False


def test_transaction_rejects_invalid_type():

    result = add_transaction(
        "Invalid",
        500,
        1,
        "Invalid transaction",
        "2026-09-22"
    )

    assert result is False


def test_transaction_rejects_empty_description():

    result = add_transaction(
        "Expense",
        500,
        1,
        "",
        "2026-09-22"
    )

    assert result is False
    
def test_budget_rejects_zero_amount():

    result = add_budget(
        1,
        0,
        9,
        2026
    )

    assert result is False


def test_budget_rejects_negative_amount():

    result = add_budget(
        1,
        -500,
        9,
        2026
    )

    assert result is False


def test_budget_rejects_invalid_month():

    result = add_budget(
        1,
        5000,
        13,
        2026
    )

    assert result is False


def test_budget_rejects_invalid_year():

    result = add_budget(
        1,
        5000,
        9,
        1999
    )

    assert result is False