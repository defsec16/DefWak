import os
import scapy.all as scapy
import argparse
os.syatem('clear')
banner = '''
	|\          /\          /|
	| \        /  \        / |
	|  \      /    \      /  |
	|   \    /      \    /   |
	|    \  /        \  /    |
	|_____\/__________\/_____|
	      /\          /\
	     /  \        /. \
	    /    \      /    \
	   /      \    /      \
	  /        \  /        \
	 /          \/          \
       python3 skannet.py --target (ip)  '''

print(banner)
def scan(ip):
	arp_request= scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	ans_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
	clients_list = []
	print('IP\t\t\tMAC Address\n====================================================')
	for element in ans_list:
		client_dict ={'ip':element[1].psrc, 'mac':element[1].hwsrc}
		clients_list.append(client_dict)
	return clients_list		
def get_arguments():
	parser=argparse.ArgumentParser()
	parser.add_argument('-t', '--target', dest='target', help='Target IP / IP range.')
	options = parser.parse_args()
	return options
def print_result(result_list):
	print('IP\t\t\tMAC Address\n===============================================')
	for client in result_list:
		print(client['ip'] + '\t\t' + client['mac'])
options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)

