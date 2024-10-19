FROM nginx:latest
LABEL authors="lucas"
WORKDIR /usr/share/nginx/html
# Remember build Frontend before executing DockerFile
# COPY ./build/ .
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]