# Description: Dockerfile for the backend service
FROM postgres:17.0
LABEL authors="lucas"

# Install packages
RUN apt-get update -y && \
    # Install Python 3, pip, venv for the API app
    apt-get install -y python3 python3-pip python3-venv && \
    # Install supervisor for process management (start API and PostgreSQL)
    apt-get install -y supervisor

# Working directory
WORKDIR /app/backend

# Copy backend files into container
COPY . /app/backend

# Create directories for logs
# Directory for PostgreSQL already exist
RUN mkdir -p /var/log/app

# Create a virtual environment in the /app/venv directory for the API app
RUN python3 -m venv /app/venv

# Upgrade pip and install dependencies via requirements.txt file
RUN /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r requirements.txt

# Supervisor configuration file for the API app and PostgreSQL
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Entry point for the container
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
