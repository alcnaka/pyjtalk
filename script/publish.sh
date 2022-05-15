#!/bin/sh
# Execute from project root
# sh script/publish.sh

version="0.2.0"

docker-compose build
docker tag alcnaka/pyjtalk:$version alcnaka/pyjtalk:latest

docker push alcnaka/pyjtalk:$version
docker push alcnaka/pyjtalk:latest
