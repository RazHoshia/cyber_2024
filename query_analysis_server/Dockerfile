# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy dependencies file and install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]