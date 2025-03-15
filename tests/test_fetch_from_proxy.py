import pymysql
import time
import json

# ProxySQL connection details (Using non-admin user)
PROXYSQL_HOST = "127.0.0.1"
PROXYSQL_PORT = 6032
PROXYSQL_USER = "remote_monitor"
PROXYSQL_PASSWORD = "password"

def test_fetch_queries():
    """Fetch the last 10 seconds of queries from ProxySQL and print them"""
    try:
        # Get the current epoch time (last 10 seconds)
        current_time = int(time.time())
        ten_seconds_ago = current_time - 10

        QUERY = f"""
        SELECT 
            *
        FROM stats_mysql_query_digest
        """

        # Connect to ProxySQL using the new user
        conn = pymysql.connect(
            host=PROXYSQL_HOST,
            port=PROXYSQL_PORT,
            user=PROXYSQL_USER,
            password=PROXYSQL_PASSWORD,
            cursorclass=pymysql.cursors.DictCursor
        )

        with conn.cursor() as cursor:
            cursor.execute(QUERY)
            rows = cursor.fetchall()

        conn.close()

        # Print formatted JSON output
        d = json.dumps(rows, indent=4)
        print(d)
        return d

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_fetch_queries()
