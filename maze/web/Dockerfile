FROM alpine:3.6

MAINTAINER resb53 <resb53.git@gmail.com>

USER root

EXPOSE 31331

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK
ENV LANG C.UTF-8

# copy files
COPY . /app

# application directory
ENV FLASK_APP /app/maze-flask.py

# set workdir
WORKDIR /app

# basic flask environment
RUN apk add --no-cache bash python3 \
  && pip3 install --upgrade pip \
  && pip3 install flask

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "31331"]
