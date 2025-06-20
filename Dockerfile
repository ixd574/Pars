FROM python:3.10-slim

WORKDIR /app

# Allow passing API_KEY during build
ARG API_KEY
ENV API_KEY=${API_KEY}

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./app /app

# Create uploads directory
RUN mkdir -p /app/uploads

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
