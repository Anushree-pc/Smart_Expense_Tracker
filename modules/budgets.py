from database.connection import create_connection


def add_budget(category_id, amount, month, year):

    # Validate category
    if category_id is None:
        print("❌ Category is required.")
        return False

    # Validate budget amount
    if amount is None or float(amount) <= 0:
        print("❌ Budget amount must be greater than zero.")
        return False

    # Validate month
    if month is None or int(month) < 1 or int(month) > 12:
        print("❌ Month must be between 1 and 12.")
        return False

    # Validate year
    if year is None or int(year) < 2000:
        print("❌ Invalid year.")
        return False

    connection = create_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
        INSERT INTO budgets
        (category_id, amount, month, year)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            category_id,
            amount,
            month,
            year
        )

        cursor.execute(query, values)
        connection.commit()

        print("✅ Budget added successfully!")

        return True

    except Exception as error:

        print(f"❌ Error adding budget: {error}")

        return False

    finally:

        if cursor:
            cursor.close()

        connection.close()

def get_budgets():
    connection = create_connection()

    if connection is None:
        return []

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT
            b.budget_id,
            c.category_name,
            b.amount,
            b.month,
            b.year
        FROM budgets b
        JOIN categories c
            ON b.category_id = c.category_id
        ORDER BY b.year DESC, b.month DESC
        """

        cursor.execute(query)

        return cursor.fetchall()

    except Exception as error:
        print(f"❌ Error retrieving budgets: {error}")
        return []

    finally:
        if cursor:
            cursor.close()
        connection.close()

def get_budget_status(month, year):
    connection = create_connection()

    if connection is None:
        return []

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT
            b.budget_id,
            c.category_name,
            b.amount AS budget_amount,
            COALESCE(SUM(t.amount), 0) AS spent_amount,
            b.amount - COALESCE(SUM(t.amount), 0) AS remaining_amount
        FROM budgets b
        JOIN categories c
            ON b.category_id = c.category_id
        LEFT JOIN transactions t
            ON b.category_id = t.category_id
            AND t.type = 'Expense'
            AND MONTH(t.transaction_date) = b.month
            AND YEAR(t.transaction_date) = b.year
        WHERE b.month = %s
        AND b.year = %s
        GROUP BY
            b.budget_id,
            c.category_name,
            b.amount
        ORDER BY c.category_name
        """

        cursor.execute(query, (month, year))

        return cursor.fetchall()

    except Exception as error:
        print(f"❌ Error calculating budget status: {error}")
        return []

    finally:
        if cursor:
            cursor.close()
        connection.close()
        
def check_budget_alerts(month, year):
    budget_status = get_budget_status(month, year)

    alerts = []

    for budget in budget_status:
        budget_amount = float(budget["budget_amount"])
        spent_amount = float(budget["spent_amount"])

        if budget_amount == 0:
            continue

        usage_percentage = (spent_amount / budget_amount) * 100

        if usage_percentage >= 100:
            alerts.append(
                f"🚨 {budget['category_name']}: Budget exceeded!"
            )

        elif usage_percentage >= 80:
            alerts.append(
                f"⚠️ {budget['category_name']}: "
                f"{usage_percentage:.1f}% of budget used."
            )

    return alerts