#!/usr/bin/bash

GAMEHOST="morphygames.co.uk"

cd "$( dirname "${BASH_SOURCE[0]}" )"

if [ -z $1 ]
then
  echo "Usage: $0 (run|build version)"
else
  if [ $1 == "build" ]
  then 
    if [ -z $2 ]
      then echo "Please supply an argument for the version number"
      exit
    fi
    docker build -t witcher-maze:$2 ./maze/web/
    docker build -t witcher-riddle:$2 ./riddle/web/
    docker build -t witcher-escape:$2 ./escape/web/
  elif [ $1 == "run" ]
  then
    if [ -z $2 ]
      then echo "Please supply an argument for the version number"
      exit
    fi
    docker kill maze-app riddle-app escape-app nginx
    docker ps -a | grep Exit | cut -d ' ' -f 1 | xargs docker rm

    docker run --name maze-app --network bridge -e VIRTUAL_HOST=maze.$GAMEHOST -d witcher-maze:$2
    docker run --name riddle-app --network bridge -e VIRTUAL_HOST=riddle.$GAMEHOST -d witcher-riddle:$2
    docker run --name escape-app --network bridge -e VIRTUAL_HOST=escape.$GAMEHOST -d witcher-escape:$2
    docker run --name nginx --network bridge -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro -d jwilder/nginx-proxy:alpine
  else
    echo "Requires 'build' or 'run'"
  fi
fi
