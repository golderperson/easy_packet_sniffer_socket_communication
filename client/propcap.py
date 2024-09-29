#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import os


def pcap():
    host = "host_id" # listen ip
    #create raw socket and bind
    if os.name == "nt":
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

    sniffer.bind((host, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# Windowsの場合はioctlを使用してプロミスキャスモードを有効化

# 単一パケットの読み込み print(repr(sniffer.recvfrom(65565)))
    while True:
        try:
            with open('myfile.bin', 'ab') as f1, open('myfile.txt', 'a', encoding='utf-8') as f:
                # if your os is windows,decide mode on in promiscuous mode
                if os.name == "nt":
                    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
                # Capture a single packet 
                packet, addr = sniffer.recvfrom(65565)
                f1.write(packet)
                decoded_packet = packet.decode('utf-8', errors='ignore')#decode packet
                f.write(decoded_packet)
                print(decoded_packet)
                # if your os is windows,decide mode off in promiscuous mode
                if os.name == "nt":
                    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
                return decoded_packet
        except KeyboardInterrupt as e:
            print("exit")
            exit()




