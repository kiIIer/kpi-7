FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y vim iproute2 iputils-ping \
    nmap net-tools ethtool ifupdown \
    netcat iptables tcpdump bridge-utils \
    arping socat openssh-server python3-pip
RUN echo 'root:12345' | chpasswd
RUN apt-get install -y snmp snmpd libsnmp-dev
ENTRYPOINT ["/usr/sbin/init"]
