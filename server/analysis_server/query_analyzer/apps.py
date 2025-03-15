from django.apps import AppConfig
import multiprocessing
import atexit
import signal
from .sql_proccessor import proccess

worker = None  # Global reference to the worker process

class QueryAnalyzerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "query_analyzer"

    def ready(self):
        """Starts the worker process when Django starts."""
        global worker
        if multiprocessing.current_process().name == "MainProcess":
            worker = multiprocessing.Process(target=proccess, daemon=True)
            worker.start()
            print("Query Analyzer Worker process started.")
