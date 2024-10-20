#FROM node:23.0 as build
#
## Working directory
#WORKDIR /app
#
## Copy the package.json file
#COPY package.json .
#
## Install the dependencies
#RUN npm install
#
## Copy the source code
#COPY . .
#
## Build the application
#RUN npm run build
#
#FROM nginx:stable as production
#LABEL authors="lucas"
#
## Copy the build files to the working directory
#COPY --from=build /app/build /usr/share/nginx/html
#
## Expose port - APP Port
#EXPOSE 80
#
## Set the entrypoint to use nginx
#CMD ["nginx", "-g", "daemon off;"]

####################### SECTION 2 - ALREADY BUILDED FOR A LIGHTER IMAGE #######################

# Description: Dockerfile for the frontend service
# nginx version also tagged as stable (nginx:stable)
FROM nginx:1.26
LABEL authors="lucas"

# Copy the build files to the working directory
COPY ./build /usr/share/nginx/html

# Expose port - APP Port
EXPOSE 80

# Entry point for the container
# daemon off; keeps the nginx process running in the foreground
CMD ["nginx", "-g", "daemon off;"]