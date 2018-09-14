#!/bin/sh
CONF_FILE=/home/ubuntu/SE195/docker/postgresql.conf

docker run -v $CONF_FILE:/etc/postgresql.conf \
    -p 25432:5432 \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=123123 \
    --rm -P --name postgres_instance postgres \
    -c config_file=/etc/postgresql.conf
