# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose port 8000 for the Django app
EXPOSE 8000

# Command to run the Django app with Uvicorn
CMD ["uvicorn", "myproject.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
