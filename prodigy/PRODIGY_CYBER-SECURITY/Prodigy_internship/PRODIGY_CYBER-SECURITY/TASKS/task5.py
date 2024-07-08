from scapy.all import *

# Get a list of available interfaces
ifaces = list(conf.ifaces.keys())

# Print the list of interfaces
print("Available interfaces:")
for i, iface in enumerate(ifaces):
    print(f"{i+1}. {iface}")

# Ask the user to select an interface
iface_num = int(input("Enter the number of the interface to use: "))
selected_iface = ifaces[iface_num - 1]

print(f"You selected interface {selected_iface}")

# Define the number of packets to capture
PACKET_COUNT = 10

# Sniff packets on the selected interface
sniffer = sniff(iface=selected_iface, count=PACKET_COUNT)

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