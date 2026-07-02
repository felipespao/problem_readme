FROM python:3.12-alpine

WORKDIR /app

COPY compute.py /usr/local/bin/compute
RUN chmod +x /usr/local/bin/compute
