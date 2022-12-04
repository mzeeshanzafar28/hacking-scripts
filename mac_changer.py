import subprocess

import optparse

import re



def get_arguments():

	parser = optparse.OptionParser()

	parser.add_option("-i","--interface",dest = "interface", help = "Interface to change its mac address")

	parser.add_option("-m","--mac",dest = "new_mac", help = "new mac address for interface")

	(options,arguments) = parser.parse_args()

	if not options.interface:

		parser.error("[-] Please specify an interface, use --help for more info.")

	elif not options.new_mac:

		parser.error("[-] Please specify a new mac address, use --help for more info.")

	return options





def change_mac(interface,new_mac):	

	print("[+] changing MAC address for interface " + interface + " to " + new_mac)

	subprocess.call(["ifconfig", interface, "down"])

	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

	subprocess.call(["ifconfig", interface, "up"])



def get_current_mac(interface):

	ifconfig_result=subprocess.check_output(["ifconfig", interface])

	mac_address_search_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)

	if mac_address_search_result:

		return mac_address_search_result.group(0)

	else:

		print("[-] Could not read current MAC address")



Options = get_arguments()



current_mac_captured=get_current_mac(Options.interface)

print("[+] current mac is " + str(current_mac_captured))



change_mac(Options.interface,Options.new_mac)



new_mac_captured=get_current_mac(Options.interface)



if new_mac_captured == Options.new_mac:

	print("[+] MAC successfully changed to " + new_mac_captured)

else:

	print("[-] MAC address did not get changed.")
