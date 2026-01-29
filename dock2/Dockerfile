FROM ubuntu:22.04
RUN apt-get update && apt-get install -y nginx
RUN mkdir -p /var/www/html
COPY myapp /var/www/html/
CMD ["nginx", "-g", "daemon off;"]
