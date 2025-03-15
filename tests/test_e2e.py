import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


from test_db_setup import test_db_read
from test_fetch_from_proxy import test_fetch_queries

def test():
    test_db_read()
    d = test_fetch_queries()
    if not d:
        raise


if __name__ == '__main__':
    test()