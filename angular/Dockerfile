# Use an official Node.js image
FROM node:18

# Set the working directory
WORKDIR /app

# Install Angular CLI globally
RUN npm install -g @angular/cli

# Expose Angular's default port
EXPOSE 4200

# Copy entrypoint script and set permissions
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Start the container using the entrypoint script
ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]