from database.connection import create_connection


def add_transaction(
    transaction_type,
    amount,
    category_id,
    description,
    transaction_date
):
    # Validate transaction type
    if transaction_type not in ["Income", "Expense"]:
        print("❌ Invalid transaction type.")
        return False

    # Validate amount
    if amount is None or float(amount) <= 0:
        print("❌ Amount must be greater than zero.")
        return False

    # Validate category
    if category_id is None:
        print("❌ Category is required.")
        return False

    # Validate date
    if transaction_date is None:
        print("❌ Transaction date is required.")
        return False

    # Validate description
    if not description or not description.strip():
        print("❌ Description cannot be empty.")
        return False

    connection = create_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
        INSERT INTO transactions
        (type, amount, category_id, description, transaction_date)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            transaction_type,
            amount,
            category_id,
            description.strip(),
            transaction_date
        )

        cursor.execute(query, values)
        connection.commit()

        print("✅ Transaction added successfully!")

        return True

    except Exception as error:

        print(f"❌ Error adding transaction: {error}")

        return False

    finally:

        if cursor:
            cursor.close()

        connection.close()


def get_transactions():
    connection = create_connection()

    if connection is None:
        return []

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT
            t.transaction_id,
            t.type,
            t.amount,
            c.category_name,
            t.description,
            t.transaction_date
        FROM transactions t
        JOIN categories c
            ON t.category_id = c.category_id
        ORDER BY t.transaction_date DESC
        """

        cursor.execute(query)

        return cursor.fetchall()

    except Exception as error:
        print(f"❌ Error retrieving transactions: {error}")
        return []

    finally:
        if cursor:
            cursor.close()
        connection.close()
def delete_transaction(transaction_id):
    connection = create_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
        DELETE FROM transactions
        WHERE transaction_id = %s
        """

        cursor.execute(query, (transaction_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("✅ Transaction deleted successfully!")
            return True

        print("❌ Transaction not found.")
        return False

    except Exception as error:
        print(f"❌ Error deleting transaction: {error}")
        return False

    finally:
        if cursor:
            cursor.close()
        connection.close()