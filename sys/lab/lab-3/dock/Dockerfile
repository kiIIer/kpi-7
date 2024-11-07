FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y vim iproute2 iputils-ping \
    nmap net-tools ethtool ifupdown \
    netcat iptables tcpdump bridge-utils \
    arping socat openssh-server

RUN apt-get install -y python3-pip
RUN pip3 install psutil==0.7.2

RUN echo 'root:12345' | chpasswd
ENTRYPOINT ["/usr/sbin/init"]