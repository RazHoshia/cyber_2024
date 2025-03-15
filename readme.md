# MySQL Reverse Proxy Project

This project sets up a **MySQL database** with a **ProxySQL reverse proxy**, providing an easy-to-use environment for testing and development.

## Getting Started

### Prerequisites

Ensure you have **Docker** and **Docker Compose** installed.

Install dependencies for running tests:

```sh
pip install -r requirements.txt
```

### Running the Project

To start all services:

```sh
docker compose up
```

This command will:

- Start the **MySQL database** with mock data.
- Start **ProxySQL** as a reverse proxy for MySQL.
- Set up user authentication and query routing.

To shut everything down:

```sh
docker compose down
```

To **reset** the database (removing all data):

```sh
docker compose down -v
```

> ⚠️ Using `-v` removes all volumes, including stored MySQL data.

## Project Structure

```
/project-root
│── docker-compose.yml   # Docker setup for MySQL & ProxySQL
│── mysql/
│   ├── init.sql         # MySQL initialization script (users, tables, sample data)
│   ├── mysqld.cnf       # MySQL configuration
│── reverse_proxy/
│   ├── proxysql.cnf     # ProxySQL configuration
│── tests/
│   ├── test_db_setup.py     # Tests if MySQL is running & correctly configured
│   ├── test_fetch_from_proxy.py  # Tests if ProxySQL is running & routing queries
│   ├── test_e2e.py       # End-to-end test verifying full system functionality
│── requirements.txt      # Python dependencies for running tests
│── README.md             # Project documentation
```

## Running Tests

Tests are located in the **`tests/`** folder and ensure the system is working as expected.

- **`test_db_setup.py`**: Verifies MySQL is up and correctly initialized.
- **`test_fetch_from_proxy.py`**: Checks that ProxySQL is up and correctly routing queries.
- **`test_e2e.py`**: Runs a sanity test after `docker compose up` to validate the entire system.

Run tests with:

```sh
pytest tests/
```

> 📌 Ensure `docker compose up` is running before running tests.

## Notes

- **MySQL database** starts with a mock `users` table and sample data.
- **ProxySQL** is preconfigured for query routing and logging.
- **Tests** ensure proper functionality of the database, proxy, and integration.

---

This README provides a complete guide for setting up, running, and testing the project. 🚀
