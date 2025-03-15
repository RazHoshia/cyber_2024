FROM proxysql/proxysql

# Install Python and required dependencies
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Set the working directory inside the container
WORKDIR /app

# Create a virtual environment
RUN python3 -m venv /app/venv

# Activate the virtual environment and install dependencies
RUN /app/venv/bin/pip install --upgrade pip 

# copy and install python requierments
COPY requierments.txt requierments.txt
RUN /app/venv/bin/pip install -r requierments.txt

# Copy the Python main into the container
COPY main.py /app/main.py

# Run ProxySQL and execute the Python main in the virtual environment
CMD proxysql & /app/venv/bin/python /app/main.py