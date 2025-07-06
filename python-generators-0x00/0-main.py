#!/usr/bin/python3

import seed

conn = seed.connect_db()
if conn:
    seed.create_database(conn)
    conn.close()

conn = seed.connect_to_prodev()
if conn:
    seed.create_table(conn)
    seed.insert_data(conn, 'user_data.csv')

    print("\nReading one row at a time:")
    for row in seed.stream_user_data(conn):
        print(row)

    conn.close()
