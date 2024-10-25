# PRJ-ST2SAS
 Project - ST2SAS - Docker Containers (I2 - 2425S7) - 2024/2025

## Description

Note: This is not the report of the project. The report can be found in the `Report` .
This project is about deploying multiple application using containers, and permit them to communicate with each other.

Here we have two containers:
- **Container A**: Our NodeJS (React.js) application
- **Container B**: Our Backend with API (FastAPI) + PostgresSQL database

## Run the project
To deploy the containers, we use Docker Compose.
Run the following command to deploy the containers:
```bash
docker compose up --build
```
## About the project

This project is about having different services running in separated containers. All of this
can process can be managed by one file: docker-compose.yaml file.
In our project, there will be two containers running as prescribed by the subject:
1. Docker Container A - Frontend: will run the frontend of our project.
- Based on: Node.js (v22.9.0), React, Tailwind + DaisyUI
- Using port: 80
2. Docker Container B – Backend: will run the backend of our project.
     Part 1 – API REST:
     - Running on Python (3.12) with FastAPI for the REST service
    - Using port: 3000

     Part 2 – PostgreSQL:
      - Version: 17.0
      - Using port: 5432

###  Machine Characteristics
1. Machine 1 – Used for the development:
- OS: MacOS Sequoia Version 15.1 Beta (24B5077a)
- Docker version 27.2.0, build 3ab4256
- Hypervisor (used for tests purpose):
- Vagrant - spox/ubuntu-arm (1.0.0) – VMWare Fusion 13.5.2
- Docker version 27.3.1, build ce12230
- Ports:
    1. 8080:80
    2. 3000:3000
2. Machine 2 – Used for testing:
- OS: Windows 10 22H2 19045.5011
- Docker version 27.2.0, build 3ab4256

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

## Steps executed by Docker compose

1. Define the services
   1. backend
       - Pull the backend image from Docker Hub 
       - Named the container **prjst2sas-backend**
       - Set the environment variables
       - Set the volume
       - Set the ports (API , Postgres)
       - Connect to the network **prjst-network**
   2. frontend
       - Pull the frontend image from Docker Hub
       - Named the container **prjst2sas-frontend**
       - Set the ports (nginx)
       - Connect to the network **prjst-network**
2. network
    - Create the network **prjst-network**
    - use the driver **bridge**
3. volumes
    - Create the volume **db-data**
## Docker Images

The Docker images are built using the Dockerfile in the `frontend` and `backend` folders.
The images are built using the following command:
```bash
docker build -t 450666049652775641901333182796/prjst2sas-frontend:stable frontend
docker build -t 450666049652775641901333182796/prjst2sas-backend:stable backend
```
Docker images have been pushed to Docker Hub:
```bash
docker push 450666049652775641901333182796/prjst2sas-frontend:stable
docker push 450666049652775641901333182796/prjst2sas-backend:stable
```

Links:
- [Frontend Docker Image](https://hub.docker.com/repository/docker/450666049652775641901333182796/prjst2sas-frontend/general)
- [Backend Docker Image](https://hub.docker.com/repository/docker/450666049652775641901333182796/prjst2sas-backend/general)


## Tools/Bibliography

- [wait-for-it.sh](https://github.com/vishnubob/wait-for-it) used for waiting for the database to be ready before starting the API.
- [FastAPI](https://fastapi.tiangolo.com/) used for the API.
- [React.js](https://reactjs.org/) used for the Frontend.
- [DaisyUI](https://daisyui.com/) used for the CSS framework.
- [PostgresSQL](https://www.postgresql.org/) used for the database.
- [Docker](https://www.docker.com/) used for the containers.

## Example of backend/.env file

If you want to run the backend locally, you need to create a `.env` file in the `backend` folder with the following content:
```bash
POSTGRES_USER=9670395335672399139331544411282
POSTGRES_PASSWORD=IeN2mgXSmw4XzxR5QY97EgAkIYQp9JU
POSTGRES_SCHEMA=school
POSTGRES_DB=prjst2sas
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

API_PORT=3000
API_HOST=0.0.0.0
```
**Don't forget to enable dotenv.load_dotenv() in backend/core/settings.py**

## Contributors

- Lucas KOCOGLU
- Maxime BOULLE
- Nicolas LAHIMASY