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
        seconds = 10000
        current_time = int(time.time())  # Get current epoch time
        time_threshold = current_time - seconds  # Compute the timestamp X seconds ago

        QUERY = f"""
        SELECT 
            hostgroup,
            schemaname,
            username,
            client_address,
            digest,
            digest_text,
            count_star,
            first_seen,
            last_seen,
            sum_time,
            min_time,
            max_time,
            sum_rows_affected,
            sum_rows_sent
        FROM stats_mysql_query_digest
        WHERE last_seen >= {time_threshold}
        ORDER BY last_seen DESC;
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
