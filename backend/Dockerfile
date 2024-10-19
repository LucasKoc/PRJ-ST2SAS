FROM postgres:17.0
LABEL authors="lucas"

# Install packages
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get install -y supervisor

# Set environment variables for PostgreSQL credentials
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}
ENV POSTGRES_HOST=${POSTGRES_HOST}
ENV POSTGRES_PORT=${POSTGRES_PORT}

# Set environment variables for API
ENV API_PORT=${API_PORT}
ENV API_HOST=${API_HOST}

# Working directory
WORKDIR /app/backend

# Copy backend into container
COPY . /app/backend

# Create directories for logs
RUN mkdir -p /var/log/app

# Create and activate a virtual environment
RUN python3 -m venv /app/venv

# Upgrade pip and install dependencies in the virtual environment
RUN /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r requirements.txt

# Expose port - API Port
EXPOSE ${API_PORT}

# Copy the supervisord configuration file into the container
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Set the entrypoint to use supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
