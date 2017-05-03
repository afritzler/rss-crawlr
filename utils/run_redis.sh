#!/bin/bash

app="redis"
if docker ps | awk -v app="app" 'NR>1{  ($(NF) == app )  }'; then
  docker stop "$app" && docker rm -f "$app"
fi

docker run --net=host --name redis -d redis:alpine
