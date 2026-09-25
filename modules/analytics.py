from database.connection import create_connection


def get_financial_summary():
    connection = create_connection()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT
            COALESCE(SUM(CASE WHEN type = 'Income' THEN amount ELSE 0 END), 0) AS total_income,
            COALESCE(SUM(CASE WHEN type = 'Expense' THEN amount ELSE 0 END), 0) AS total_expense
        FROM transactions
        """

        cursor.execute(query)
        result = cursor.fetchone()

        total_income = result["total_income"]
        total_expense = result["total_expense"]
        balance = total_income - total_expense

        return {
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": balance
        }

    except Exception as error:
        print(f"❌ Error calculating summary: {error}")
        return None

    finally:
        if cursor:
            cursor.close()
        connection.close()

def get_category_expenses():
    connection = create_connection()

    if connection is None:
        return []

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT
            c.category_name,
            COALESCE(SUM(t.amount), 0) AS total_spent
        FROM categories c
        LEFT JOIN transactions t
            ON c.category_id = t.category_id
            AND t.type = 'Expense'
        GROUP BY c.category_id, c.category_name
        ORDER BY total_spent DESC
        """

        cursor.execute(query)

        return cursor.fetchall()

    except Exception as error:
        print(f"❌ Error calculating category expenses: {error}")
        return []

    finally:
        if cursor:
            cursor.close()
        connection.close()
        
def get_monthly_expenses():
    connection = create_connection()

    if connection is None:
        return []

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT
            YEAR(transaction_date) AS year,
            MONTH(transaction_date) AS month,
            SUM(amount) AS total_expense
        FROM transactions
        WHERE type = 'Expense'
        GROUP BY
            YEAR(transaction_date),
            MONTH(transaction_date)
        ORDER BY
            YEAR(transaction_date),
            MONTH(transaction_date)
        """

        cursor.execute(query)

        return cursor.fetchall()

    except Exception as error:
        print(f"❌ Error calculating monthly expenses: {error}")
        return []

    finally:
        if cursor:
            cursor.close()

        connection.close()