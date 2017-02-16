#!/bin/bash

app="cassandra"
if docker ps | awk -v app="app" 'NR>1{  ($(NF) == app )  }'; then
  docker stop "$app" && docker rm -f "$app"
fi
docker run --name cassandra -d cassandra:3
