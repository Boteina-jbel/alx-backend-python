import mysql.connector

def stream_users():
    """Generator that yields one row at a time from the user_data table"""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',  # Replace with your real password
            database='ALX_prodev'
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        for row in cursor:  # Only one loop as required
            yield row

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return
