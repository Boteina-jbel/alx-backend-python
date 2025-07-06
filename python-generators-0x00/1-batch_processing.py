import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that yields users in batches from the user_data table"""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',  # Replace with your MySQL password
            database='ALX_prodev'
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        while True:
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break
            yield rows  # Yield a batch (list of users)

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return


def batch_processing(batch_size):
    """Processes batches and yields users older than 25"""
    for batch in stream_users_in_batches(batch_size):  # 1st loop
        for user in batch:  # 2nd loop
            if int(user['age']) > 25:
                yield user  # 3rd loop done via yield
