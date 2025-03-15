# Use official MySQL image as base
FROM mysql:8.0

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=P@ssw0rd
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=P@ssw0rd

# Copy initialization SQL script
COPY init.sql /docker-entrypoint-initdb.d/

# Copy custom entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Run the entrypoint script before MySQL starts
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]