#! /usr/bin/env python

import netfilterqueue


def process_packet(packet):
    print(packet)


queue = netfilterqueue.Netfilterqueue()
queue.bind(0, process_packet)
queue.run()
