# Import necessary modules from Scapy
from scapy.all import *  # Import all functions and classes from Scapy
from scapy.layers.dns import DNS, DNSQR, DNSRR, IP  # Import DNS layers and IP layer

def extract_a_records(pcap_file):
    """
    Function to extract A records (IPv4 addresses) from a given pcap file.
    
    Args:
        pcap_file (str): The path to the pcap file to analyze.
    
    Returns:
        dict: A dictionary where keys are domain names and values are their corresponding A record IP addresses.
    """
    # Load packets from the pcap file using Scapy
    packets = rdpcap(pcap_file)
    
    # Initialize an empty dictionary to store the A records
    a_records = {}
    
    # Initialize a counter to keep track of the number of packets processed
    count = 0
    
    # Loop through each packet in the packets list
    for pkt in packets:
        # Increment the packet counter
        count += 1
        
        # Check if the current packet contains a DNS layer
        if DNS in pkt:
            # Extract the DNS layer from the packet
            dns_layer = pkt[DNS]
            
            # Check if the DNS layer contains DNS resource records (DNSRR)
            if pkt.haslayer(DNSRR):
                # Extract the DNS resource record from the packet
                dns_rr = pkt[DNSRR]
                
                # Check if the record is of type A (type code 1), which represents an IPv4 address
                if dns_rr.type == 1:
                    # Decode the domain name and remove any trailing dots
                    domain_name = dns_rr.rrname.decode().strip('.')
                    
                    # Extract the IP address from the DNS resource record
                    ip_address = dns_rr.rdata
                    
                    # Store the A record in the dictionary if the domain name is not already present
                    if domain_name not in a_records:
                        a_records[domain_name] = ip_address
        
        # Optional: Uncomment the following line to print each packet (useful for debugging)
        # print(pkt)
    
    # Print the total number of packets processed
    print("Packets: ", count)
    
    # Return the dictionary of A records
    return a_records

def print_a_records(a_records):
    """
    Function to print the A records from the dictionary in a readable format.
    
    Args:
        a_records (dict): A dictionary where keys are domain names and values are their corresponding A record IP addresses.
    """
    # Loop through each domain and its associated IP address in the dictionary
    for domain, ip in a_records.items():
        # Check that neither the domain nor the IP address is empty
        if domain != '' and ip != '':
            # Print the domain and its associated IP address
            print(f"{domain} -> {ip}")

if __name__ == "__main__":
    # Specify the path to the pcap file to analyze
    pcap_file = "dnsPlain.pcapng"
    
    # Call the function to extract A records from the pcap file
    a_records = extract_a_records(pcap_file)
    
    # Call the function to print the extracted A records
    print_a_records(a_records)