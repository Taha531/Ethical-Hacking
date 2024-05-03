#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    scapy.arping(ip)

#IP range
scan("192.168.29.2")