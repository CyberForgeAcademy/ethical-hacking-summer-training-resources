from scapy.all import *
from scapy.layers.dns import DNS, DNSRR

def extract_a_records(packet):
    """
    Callback function to process each captured packet and extract A records.
    
    Args:
        packet (scapy.packet): The packet captured by Scapy.
    """
    # Check if the packet has DNS layer
    if DNS in packet:
        dns_layer = packet[DNS]
        
        # Process DNS responses to get A records
        if packet.haslayer(DNSRR):
            dns_rr = packet[DNSRR]
            
            # Check if the record is of type A (type code 1)
            if dns_rr.type == 1:
                domain_name = dns_rr.rrname.decode().strip('.')
                ip_address = dns_rr.rdata
                
                # Print the A record directly
                print(f"{domain_name} -> {ip_address}")

def live_capture(interface):
    """
    Function to perform live capture on a network interface and process DNS A records.
    
    Args:
        interface (str): The name of the network interface to capture packets from.
    """
    print(f"Starting live capture on interface: {interface}")
    
    # Capture packets from the specified interface
    sniff(iface=interface, prn=extract_a_records, store=0, filter="udp port 53")

if __name__ == "__main__":
    # Specify the network interface to capture packets from
    interface = "eth0"  # Replace with your network interface name
    
    # Start live packet capture and extraction
    live_capture(interface)