FROM node:latest
MAINTAINER Ian Foster, ifoster.98@gmail.com

ENV LAST_UPDATE=2017-04-10

RUN apt-get update && \
    apt-get upgrade -y

RUN npm install -g serverless
RUN serverless --version

