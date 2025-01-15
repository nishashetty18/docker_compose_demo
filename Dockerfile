# Use Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY app/ demo/ /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
