import pymysql
import time
import requests
from datetime import datetime

# ProxySQL admin connection details
PROXYSQL_HOST = "127.0.0.1"
PROXYSQL_PORT = 6032
PROXYSQL_USER = "admin"
PROXYSQL_PASSWORD = "admin"

# Log files
LOG_FILE = "proxysql_logs.txt"
SERVER_LOG_FILE = "server_responses.txt"

# HTTP server details
HTTP_SERVER_URL = "http://192.168.189.143:5000/analyze"  # Change this to your actual server IP

def send_to_http_server(log_entry):
    """Send log entry to the HTTP server and log the response."""
    try:
        response = requests.post(HTTP_SERVER_URL, json=log_entry)
        server_response = {
            "timestamp": str(datetime.now()),
            "status_code": response.status_code,
            "server_message": response.text
        }

        # Log server response
        with open(SERVER_LOG_FILE, "a") as server_log:
            server_log.write(f"{server_response['timestamp']} | {server_response['status_code']} | {server_response['server_message']}\n")

        if response.status_code == 200:
            print("Log sent successfully.")
        else:
            print(f"Failed to send log: {response.status_code} - {response.text}")

    except Exception as e:
        error_message = f"Error sending log: {e}"
        print(error_message)

        # Log error to server response log file
        with open(SERVER_LOG_FILE, "a") as server_log:
            server_log.write(f"{str(datetime.now())} | ERROR | {error_message}\n")

def fetch_and_log():
    try:
        # Get the current epoch time (last 10 seconds)
        current_time = int(time.time())  # Current epoch timestamp
        ten_seconds_ago = current_time - 10  # 10 seconds earlier

        QUERY = f"""
        SELECT 
            p.cli_host AS IP, 
            p.db AS DB, 
            p.cli_port AS Source_Port, 
            p.user AS User, 
            q.digest_text AS Query, 
            q.count_star AS Execution_Count, 
            p.command AS Source, 
            FROM_UNIXTIME(q.first_seen) AS First_Seen_Time, 
            FROM_UNIXTIME(q.last_seen) AS Last_Seen_Time 
        FROM stats_mysql_processlist p 
        JOIN stats_mysql_query_digest q  
            ON p.user = q.username 
        WHERE q.last_seen >= {ten_seconds_ago}
        ORDER BY q.last_seen DESC;
        """

        # Connect to ProxySQL
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

            if rows:
                with open(LOG_FILE, "a") as f:
                    for row in rows:
                        log_entry = {
                            "timestamp": str(datetime.now()),
                            "ip": row["IP"],
                            "db": row["DB"],
                            "source_port": row["Source_Port"],
                            "user": row["User"],
                            "query": row["Query"],
                            "execution_count": row["Execution_Count"],
							                            "source": row["Source"],
                            "first_seen_time": row["First_Seen_Time"],
                            "last_seen_time": row["Last_Seen_Time"]
                        }
                        log_line = f"{log_entry['timestamp']} | {log_entry['ip']} | {log_entry['db']} | {log_entry['source_port']} | {log_entry['user']} | {log_entry['query']} | {log_entry['execution_count']} | {log_entry['source']} | {log_entry['first_seen_time']} | {log_entry['last_seen_time']}\n"

                        # Save to ProxySQL log file
                        f.write(log_line)

                        # Send to HTTP server
                        send_to_http_server(log_entry)
                        print(log_line)

                print(f"Logged and sent {len(rows)} entries.")

        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        fetch_and_log()
        time.sleep(10)  # Run every 10 seconds
