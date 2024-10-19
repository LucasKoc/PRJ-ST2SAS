# PRJ-ST2SAS
 Project - ST2SAS - Docker Containers (I2 - 2425S7)

## Description

This project is about deploying multiple application using containers, and permit them to communicate with each other.

Here we have two containers:
- **Container A**: Our NodeJS (React.js) application
- **Container B**: Our Backend with API (FastAPI) + PostgresSQL database

To deploy the containers, we use Docker Compose.
Run the following command to deploy the containers:
```bash
docker-compose up --build
```

## Container A

This container is a NodeJS application using React.js. It is a simple application that displays a list of students, teachers, courses and enrollments.
User is able to view and add students, teachers, courses and enrollments.

## Container B

This container is a FastAPI application with a PostgresSQL database. It is a simple API that allows to get and add students, teachers, courses and enrollments.

## Communication

The communication between the two containers is done using the Docker network. The two containers are in the same network and can communicate with each other (using driver bridge).
You can see the network information in the `docker-compose.yaml` file.

## Data Persistence

The data is persisted in the PostgresSQL database. The data is stored in a volume (info in `docker-compose.yaml` file), so the data is not lost when the container is stopped or deleted.

## Access

To access the API, default is `http://localhost:3000/` (Container A).
To access the Frontend, default is `http://localhost:8000/` (Container B).
Option can be updated in the `docker-compose.yaml` file.

## Tools/Bibliography

- [wait-for-it.sh](https://github.com/vishnubob/wait-for-it) used for waiting for the database to be ready before starting the API.
- [FastAPI](https://fastapi.tiangolo.com/) used for the API.
- [React.js](https://reactjs.org/) used for the Frontend.
- [PostgresSQL](https://www.postgresql.org/) used for the database.
- [Docker](https://www.docker.com/) used for the containers.