import mysql.connector

def stream_user_ages():
    """Generator that yields user ages one by one from the user_data table"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',  # Replace with your actual MySQL password
            database='ALX_prodev'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")

        for (age,) in cursor:  # only one loop here
            yield float(age)  # yield each age one by one as float

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return


def calculate_average_age():
    """Uses stream_user_ages to compute the average without loading all data"""
    total_age = 0
    count = 0

    for age in stream_user_ages():  # second loop
        total_age += age
        count += 1

    if count > 0:
        average = total_age / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No users found.")
