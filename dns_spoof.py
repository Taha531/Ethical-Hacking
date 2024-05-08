#! /usr/bin/env python

import netfilterqueue


def process_packet(packet):
    print(packet.get_payload())
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
