import scapy.all as scapy

# Set the interface to sniff on (e.g., eth0, wlan0, etc.)
INTERFACE = "eth0"

# Set the number of packets to capture
PACKET_COUNT = 100

# Create a packet sniffer object
sniffer = scapy.sniff(iface=INTERFACE, count=PACKET_COUNT)

# Analyze and display the captured packets
for packet in sniffer:
    # Get the source and destination IP addresses
    src_ip = packet[scapy.IP].src
    dst_ip = packet[scapy.IP].dst

    # Get the protocol (e.g., TCP, UDP, ICMP, etc.)
    protocol = packet[scapy.IP].proto

    # Get the payload data
    payload = packet[scapy.Raw].load

    # Display the packet information
    print(f"Packet {packet.count}:")
    print(f"  Source IP: {src_ip}")
    print(f"  Destination IP: {dst_ip}")
    print(f"  Protocol: {protocol}")
    print(f"  Payload: {payload.decode('utf-8', errors='replace')}")
    print()