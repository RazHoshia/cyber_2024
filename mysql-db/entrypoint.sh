#!/bin/bash

# Ensure MySQL configuration directory exists
mkdir -p /etc/mysql/mysql.conf.d

# Write MySQL configuration file to allow remote connections
echo -e "[mysqld]\nbind-address = 0.0.0.0" > /etc/mysql/mysql.conf.d/mysqld.cnf

# Restart MySQL service to apply changes
service mysql restart

# Start the default MySQL entrypoint script
exec docker-entrypoint.sh mysqld