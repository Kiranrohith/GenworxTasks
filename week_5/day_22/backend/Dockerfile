# -------------------------
# Base Image
# -------------------------
FROM python:3.14-alpine3.23

# -------------------------
# Copy uv binary
# -------------------------
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# -------------------------
# Set working directory
# -------------------------
WORKDIR /app

# -------------------------
# Copy dependency file
# -------------------------
COPY requirements.txt .

# -------------------------
# Install dependencies
# -------------------------
RUN uv pip install --system --no-cache -r requirements.txt

# -------------------------
# Copy project files
# -------------------------
COPY . .

# -------------------------
# Expose FastAPI port
# -------------------------
EXPOSE 8000

# -------------------------
# Start FastAPI
# -------------------------
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]