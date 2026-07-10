# -------------------------
# Base Image
# -------------------------
FROM python:3.14-alpine3.23

# -------------------------
# Copy uv binary
# -------------------------
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


RUN apk add --no-cache postgresql-client
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


RUN chmod +x start.sh
# -------------------------
# Expose FastAPI port
# -------------------------
EXPOSE 8000

# -------------------------
# Start FastAPI
# -------------------------
CMD ["sh","start.sh"]