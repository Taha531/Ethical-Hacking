#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst = ip) #Creating an ARP packet to send
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") #Setting the destination MAC in the ethernet part
    arp_request_broadcast = broadcast/arp_request #Combining both the packets
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0] #To send packets and recieve responses

    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t"+ element[1].hwsrc)


#IP range
scan("192.168.29.1/24")
