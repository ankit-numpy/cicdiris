# Dockerfile
FROM python:3.12-slim  # Use a slim Python 3.9 image to reduce size

WORKDIR /app  # Set the working directory inside the container

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files (app.py, iris_model.pkl, etc.)
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
