from scapy.all import *

filename = "./Printer.pcap"
print (f"Reading from {filename=}")
packets = rdpcap(filename)
# remove or place "not" based on wanting to find evil or not evil.
for packet in packets:
	if not "evil" in packet[IP].flags:
		print(packet[Raw].load.decode("utf-8"), end="")
