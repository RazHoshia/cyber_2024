import os
import time
import django
from django.db import transaction
from django.utils.timezone import now

# Setup Django environment for standalone script
if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analysis_server.settings")
    django.setup()

# from myapp.models import MyModel  # Import your Django model

def proccess():
    """Worker function that fetches, processes, and saves data periodically."""
    while True:
        try:
            pass
            print("work")
        # TODO implement fetch and proccess here 
        except Exception as e:
            print(f"Error in worker process: {e}")
        time.sleep(10)  # Wait for 1 minute
