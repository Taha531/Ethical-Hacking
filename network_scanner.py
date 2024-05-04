#!/usr/bin/env python

import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("--ip", dest = "ip_address", help = "The IP address or range for scanning")
    (options, arguments) =parser.parse_args()
    if not options.ip_address:
        parser.error("[-]Please specify an IP address or IP range. Use --ip")
    else:
        return options.ip_address

def scan(ip):
    arp_request = scapy.ARP(pdst = ip) #Creating an ARP packet to send
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") #Setting the destination MAC in the ethernet part
    arp_request_broadcast = broadcast/arp_request #Combining both the packets
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0] #To send packets and recieve responses

    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t"+ element[1].hwsrc)


ip = get_arguments()
scan(ip)
