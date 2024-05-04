#!/usr/bin/env python

import subprocess
import optparse
import re

#Creating a function to parse arguments from the command line
def get_arguments():
    parser = optparse.OptionParser()  #creating an instance to the class that handles all the parsing
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()  #Collecting the options(user values)
    #Checking whether the user has entered a value or not
    if not options.interface:
        parser.error("[-]Please specify a user interface.Use --help for more information")
    elif not options.new_mac:
        parser.error("[-]Please specify a MAC address.Use --help for more information")
    return options


#Creating a function to run the linux commands
def change_mac(interface, new_mac):
    print("[+]Changing MAC Address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


#Creating a funtion to read the current MAC address
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if search_result:
        return search_result.group(0)
    else:
        print("[-]Could not read MAC address")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("[+]The Current MAC is " + str(current_mac))

#Checking if the MAC address is changed or not
if current_mac:
    change_mac(options.interface, options.new_mac)
    current_mac = get_current_mac(options.interface)
    if options.new_mac == str(current_mac):
        print("[+]MAC address changed successfully")
    else:
        print("[-]Couldn't change MAC address")

