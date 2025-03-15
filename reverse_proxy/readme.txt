# Reverse Proxy with ProxySQL

This setup uses **ProxySQL** as a reverse proxy for MySQL, allowing efficient query routing, connection pooling, and analytics logging.

## Setup

To start the **ProxySQL** reverse proxy, use:

```sh
docker compose up reverse_proxy
```

To stop the service:

```sh
docker compose down
```

## Configuration

### `proxysql.cnf`

The `proxysql.cnf` file defines the configuration for ProxySQL, including users, query rules, and logging settings.

#### Key Configurations

- **Admin Credentials**  
  ```
  admin_variables=
  {
      admin_credentials="admin:admin;remote_monitor:password"
  }
  ```
  - `admin:admin`: Default admin login credentials.
  - `remote_monitor:password`: A user for fetching query logs and analytics from our analytics server.

- **MySQL Backend Servers**  
  ```
  mysql_servers = (
    { address="mysql", port=3306, hostgroup=10, max_connections=100 }
  )
  ```
  - Routes MySQL traffic to the `mysql` service (host: `mysql`, port: `3306`).
  - Groups the MySQL server under **hostgroup 10**, which is used for query routing.
  - Limits connections to **100 concurrent** connections.

- **User Authentication for MySQL Clients**  
  ```
  mysql_users = 
  (
    { username="myuser", password="password", default_hostgroup=10, transaction_persistent=true },
  )
  ```
  - Defines a MySQL user (`myuser`) with access to queries routed to **hostgroup 10**.
  - Ensures **transaction persistence**, meaning queries within the same transaction stay in the same backend.

- **Query Routing Rules**  
  ```
  mysql_query_rules = (
    {
      rule_id=1,
      active=1,
      match_pattern=".*",
      destination_hostgroup=10,
      apply=1
    }
  )
  ```
  - Matches **all queries (`.*`)** and routes them to **hostgroup 10** (i.e., the MySQL database).
  - Ensures that all queries are processed through ProxySQL.

- **Logging & Connection Settings**  
  ```
  mysql_audit_log_filename="/var/log/proxysql_queries.log"
  mysql_eventslog_filename="/var/log/queries.log"
  mysql_connection_max_age_ms=86400000
  ```
  - Logs query events in `/var/log/queries.log` for analytics.
  - Sets **connection max age** to **24 hours** (`86400000ms`).

## Docker Compose Configuration

The `docker-compose.yml` defines a service for ProxySQL:

```yaml
reverse_proxy:
  image: proxysql/proxysql:latest
  container_name: reverse_proxy
  depends_on:
    - mysql
  ports:
    - "6033:6033"  # MySQL client connections
    - "6032:6032"  # Admin interface
  volumes:
    - ./reverse_proxy/proxysql.cnf:/etc/proxysql.cnf
  command: ["/usr/bin/proxysql", "-f", "-c", "/etc/proxysql.cnf"]
```

### Explanation of Parameters

| Parameter | Description |
|-----------|-------------|
| `depends_on: mysql` | Ensures ProxySQL starts after MySQL. |
| `ports` | Exposes ports `6033` (for MySQL clients) and `6032` (for admin access). |
| `volumes` | Mounts the ProxySQL configuration file from `./reverse_proxy/proxysql.cnf`. |
| `command` | Runs ProxySQL with the specified configuration file. |

## Notes

- The `remote_monitor` user is used to fetch **query logs and analytics** from ProxySQL.
- MySQL clients connect via ProxySQL at `localhost:6033` instead of directly to MySQL.
- Use the admin interface (`localhost:6032`) for monitoring and managing ProxySQL.

---

This README provides a clear guide to setting up and using ProxySQL as a reverse proxy for MySQL. 🚀
