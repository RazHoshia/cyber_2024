import os
import time
import django
from django.db import transaction
from django.utils.timezone import now
from django.conf import settings
import pymysql
import json

# Setup Django environment for standalone script
if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analysis_server.settings")
    django.setup()

# from myapp.models import MyModel  # Import your Django model

def proccess():
    
    conn = pymysql.connect(
            host=settings.PROXYSQL_HOST,
            port=settings.PROXYSQL_PORT,
            user=settings.PROXYSQL_USER,
            password=settings.PROXYSQL_PASSWORD,
            cursorclass=pymysql.cursors.DictCursor
        )
    
    while True:
        try:
            interval = 10000
            current_time = int(time.time())  # Get current epoch time
            time_threshold = current_time - interval  # Compute the timestamp X seconds ago
            with conn.cursor() as cursor:
                cursor.execute(settings.PROXYSQL_FETCH_QUERY.format(time_threshold))
                rows = cursor.fetchall()
            d = json.dumps(rows, indent=4)
            print(d)
            # fetch -> proccess each -> save results to query model with other details.

        # TODO implement fetch and proccess here 
        except Exception as e:
            print(f"Error in worker process: {e}")
        time.sleep(interval)  # Wait for 1 minute
