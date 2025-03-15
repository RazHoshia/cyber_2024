# Mock MySQL Database

This project provides a mock MySQL database setup using Docker Compose. The database includes a sample `users` table with predefined data and a `monitor` user for replication monitoring.

## Setup

To start the MySQL database, use:

```sh
docker compose up mysql
```

This will initialize a MySQL container with the provided schema and sample data.

To stop and completely reset the database (removing all data and volumes), use:

```sh
docker compose down -v
```

> **Warning**: The `-v` flag removes all volumes, including stored data. Use this option if you want to reset the database.

## Database Configuration

### `init.sql`

The database is initialized with the following:

1. **User Permissions**
   - Grants all privileges on `mydatabase` to `myuser`.
   - Creates a `monitor` user with replication client access.

2. **Database Schema**
   - Creates a `users` table with the following columns:
     - `id` (Primary Key, Auto-Increment)
     - `name` (VARCHAR 100)
     - `email` (VARCHAR 100, Unique)
     - `age` (INT)

3. **Sample Data**
   - Alice (`alice@example.com`, 25 years old)
   - Bob (`bob@example.com`, 32 years old)

### `mysqld.cnf`

The MySQL configuration file includes:

- **`bind-address = 0.0.0.0`**  
  This allows MySQL to accept connections from any IP address, making it accessible from outside the container.

## Docker Compose Configuration

The `docker-compose.yml` file should include a MySQL service with the following:

```yaml
version: '3.8'

services:
  mysql:
    image: mysql:latest
    container_name: mock-mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: mydatabase
      MYSQL_USER: myuser
      MYSQL_PASSWORD: mypassword
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
      - ./mysqld.cnf:/etc/mysql/mysql.conf.d/mysqld.cnf

volumes:
  mysql_data:
```

### Explanation of Parameters

| Parameter | Description |
|-----------|-------------|
| `MYSQL_ROOT_PASSWORD` | Sets the root user's password (here set to `root`). |
| `MYSQL_DATABASE` | Initializes a database named `mydatabase`. |
| `MYSQL_USER` | Creates a user (`myuser`) for accessing the database. |
| `MYSQL_PASSWORD` | Sets the password for `myuser`. |
| `ports` | Exposes MySQL on port `3306` for external access. |
| `volumes` | Mounts a persistent volume for database data and maps initialization/config files. |

## Notes

- When stopping the database, **use `docker compose down -v`** if you want a fresh start.
- The mock database contains a simple **users table** with sample data.
- The **monitor user** is created for replication monitoring.

