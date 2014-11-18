#!/usr/bin/python

from scapy.all import * 

pkt = IP(src="192.168.122.84",dst="91.55.107.213")/\
    UDP(sport=60000,dport=53)/\
    DNS(id=1,qd=DNSQR(qname="www.utwente.nl"))

#pkt.show2()
send(pkt)
