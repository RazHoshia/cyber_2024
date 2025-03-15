import pymysql
import time

def test_mysql_connection():
    host = "localhost"  # Change if MySQL is running in a container with a different network setting
    user = "user"
    password = "password"
    database = "testdb"

    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=3306,
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATABASE();")
            result = cursor.fetchone()
            print("Test Passed: Successfully connected to MySQL.")
            print("Current Database:", result["DATABASE()"])
        connection.close()
    except Exception as e:
        print("Test Failed: Unable to connect to MySQL.", str(e))

if __name__ == "__main__":
    test_mysql_connection()
