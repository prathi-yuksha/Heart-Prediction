# Use Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8080

# Run app with Waitress
CMD ["waitress-serve", "--listen=0.0.0.0:8080", "app:app"]
