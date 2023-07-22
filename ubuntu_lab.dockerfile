FROM ubuntu

LABEL maintainer="Zeal Vora <instructors@kplabs.in>"

RUN apt-get update

RUN apt-get -y install nginx 

EXPOSE 80/tcp

CMD ["nginx", "-g", "daemon off;"]