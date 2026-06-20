from scapy.all import *

def packet_callback(packet):

    if IP in packet:

        print("\n=== Packet Captured ===")

        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)

        if Raw in packet:
            print("Payload:", packet[Raw].load)

sniff(prn=packet_callback, count=3)
