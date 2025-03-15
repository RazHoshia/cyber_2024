import pymysql

# ProxySQL connection details
PROXYSQL_HOST = "127.0.0.1"  # Host machine since the port is mapped
PROXYSQL_PORT = 6033         # ProxySQL's MySQL client port
DB_USER = "myuser"
DB_PASSWORD = "password"
DB_NAME = "mydatabase"

def test_connection():
    try:
        # Connect to MySQL via ProxySQL using PyMySQL
        conn = pymysql.connect(
            host=PROXYSQL_HOST,
            port=PROXYSQL_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conn.cursor()

        # Execute a simple query
        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()

        # Print results
        print("Users in the database:")
        for user in users:
            print(user)

        # Close connection
        cursor.close()
        conn.close()

    except pymysql.MySQLError as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    test_connection()
