import mysql.connector
import csv

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password'  # put your real MySQL password here
    )

def create_database(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

def connect_to_prodev():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='ALX_prodev'
    )

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        )
    """)
    conn.commit()
    cursor.close()

def insert_data(conn, filename):
    cursor = conn.cursor()
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("SELECT COUNT(*) FROM user_data WHERE user_id = %s", (row['user_id'],))
            if cursor.fetchone()[0] == 0:
                cursor.execute(
                    "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                    (row['user_id'], row['name'], row['email'], row['age'])
                )
    conn.commit()
    cursor.close()

def stream_user_data(conn):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row
    cursor.close()
