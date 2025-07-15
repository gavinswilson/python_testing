# steps for creating a virtual machine

FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    git

RUN pip3 install pyyaml

COPY feed.py /usr/bin/update.py

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
