#!/usr/bin/bash

GAMEHOST="morphygames.co.uk"

cd "$( dirname "${BASH_SOURCE[0]}" )"

if [ -z $1 ]
  then echo "Please supply an argument for the version number"
  exit
fi

docker build -t witcher-maze:$1 ./maze/web/
docker build -t witcher-riddle:$1 ./riddle/web/
docker build -t witcher-escape:$1 ./escape/web/

docker kill maze-app riddle-app escape-app nginx
docker ps -a | grep Exit | cut -d ' ' -f 1 | xargs docker rm

docker run --name maze-app --network bridge -e VIRTUAL_HOST=maze.$GAMEHOST -d witcher-maze:1.13
docker run --name riddle-app --network bridge -e VIRTUAL_HOST=riddle.$GAMEHOST -d witcher-riddle:1.13
docker run --name escape-app --network bridge -e VIRTUAL_HOST=escape.$GAMEHOST -d witcher-escape:1.13
docker run --name nginx --network bridge -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro -d jwilder/nginx-proxy:alpine
