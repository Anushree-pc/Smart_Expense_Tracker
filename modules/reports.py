from database.connection import create_connection


def get_monthly_report(month, year):
    connection = create_connection()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT
            COALESCE(
                SUM(CASE WHEN type = 'Income' THEN amount ELSE 0 END),
                0
            ) AS total_income,

            COALESCE(
                SUM(CASE WHEN type = 'Expense' THEN amount ELSE 0 END),
                0
            ) AS total_expense

        FROM transactions

        WHERE MONTH(transaction_date) = %s
        AND YEAR(transaction_date) = %s
        """

        cursor.execute(query, (month, year))

        result = cursor.fetchone()

        total_income = result["total_income"]
        total_expense = result["total_expense"]
        balance = total_income - total_expense

        return {
            "month": month,
            "year": year,
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": balance
        }

    except Exception as error:
        print(f"❌ Error generating monthly report: {error}")
        return None

    finally:
        if cursor:
            cursor.close()

        connection.close()