# Start from the official ProxySQL image
FROM proxysql/proxysql

# Install Python and required dependencies
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Set the working directory inside the container
WORKDIR /app

# Create a virtual environment
RUN python3 -m venv /app/venv

# Activate the virtual environment and install dependencies
RUN /app/venv/bin/pip install --upgrade pip && /app/venv/bin/pip install pymysql requests

# Copy the Python script into the container
COPY script.py /app/script.py

# Run ProxySQL and execute the Python script in the virtual environment
CMD proxysql & /app/venv/bin/python /app/script.py