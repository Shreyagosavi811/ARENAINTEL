FROM python:3.12-slim

# Set environment variables for Python optimization
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Create a non-root user
RUN addgroup --system --gid 1001 arenagroup && \
    adduser --system --uid 1001 --ingroup arenagroup arenauser

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY ./app ./app

# Ensure correct ownership for the non-root user
RUN chown -R arenauser:arenagroup /app

# Switch to the non-root user
USER arenauser

# Expose the default port (can be overridden by hosting platform via $PORT)
EXPOSE 8000

# Start Uvicorn, binding to 0.0.0.0 and dynamically using the PORT env var if set, otherwise 8000
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
