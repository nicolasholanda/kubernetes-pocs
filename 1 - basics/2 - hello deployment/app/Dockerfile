# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY app.py .

# Install Flask
RUN pip install flask

# Expose the port the app runs on
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
