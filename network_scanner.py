#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst = ip) #Creating an ARP packet to send
    arp_request.show()
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") #Setting the destination MAC in the ethernet part
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request #Combining both the packets
    arp_request_broadcast.show() #Give more details about the contains of the packet
    # scapy.ls(scapy.ARP()) --> This code is used to list all the options and their default values in scapys



#IP range
scan("192.168.29.1/24")
