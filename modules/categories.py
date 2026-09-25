from database.connection import create_connection


def add_category(category_name):
    connection = create_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
        INSERT INTO categories (category_name)
        VALUES (%s)
        """

        cursor.execute(query, (category_name,))
        connection.commit()

        print("✅ Category added successfully!")
        return True

    except Exception as error:
        print(f"❌ Error adding category: {error}")
        return False

    finally:
        if cursor:
            cursor.close()
        connection.close()


def get_categories():
    connection = create_connection()

    if connection is None:
        return []

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT category_id, category_name
        FROM categories
        ORDER BY category_name
        """

        cursor.execute(query)

        return cursor.fetchall()

    except Exception as error:
        print(f"❌ Error retrieving categories: {error}")
        return []

    finally:
        if cursor:
            cursor.close()
        connection.close()