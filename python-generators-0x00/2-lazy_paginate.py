seed = __import__('seed')

def paginate_users(page_size, offset):
    """Fetches a single page of users from the database"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """Generator that lazily yields pages of users one by one"""
    offset = 0
    while True:  # Only one loop
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page  # Yield one page (list of users)
        offset += page_size
