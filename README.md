# PRJ-ST2SAS
 Project - ST2SAS - Docker Containers (I2 - 2425S7)

## Description

This project is about deploying multiple application using containers, and permit them to communicate with each other.

Here we have two containers:
- **Container A**: Our NodeJS (React.js) application
- **Container B**: Our Backend with API (FastAPI) + PostgresSQL database

```bash
docker run \
    --name st2sas-postgres \
    -e POSTGRES_USER=9670395335672399139331544411282 \
    -e POSTGRES_PASSWORD=IeN2mgXSmw4XzxR5QY97EgAkIYQp9JU \
    -p 5432:5432 \
    -d \
    postgres:17.0
```

backend .env file:
```bash
POSTGRES_USER=9670395335672399139331544411282
POSTGRES_PASSWORD=IeN2mgXSmw4XzxR5QY97EgAkIYQp9JU
POSTGRES_SCHEMA=school
POSTGRES_DB=prjst2sas
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

API_PORT=3000
API_HOST=localhost
```