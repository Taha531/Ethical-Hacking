#!/usr/bin/env python

import subprocess

#use "raw_input" for python2
interface = input("Interface > ")
new_mac = input("New MAC > ")
print("[+]Changing MAC Address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])