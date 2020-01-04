#!/usr/bin/env python3

def get_int_vlan_map(config_filename):
	with open(config_filename, 'r') as source:
		result = []
		access_dict = {}
		trunk_dict = {}
		for lines in source:
			if 'FastEthernet' in lines:
				interface = lines.split()[-1]
			elif 'mode access' in lines:
				access_dict[interface] = 1
			elif 'access vlan' in lines:
				access_dict[interface] = int(lines.split()[-1])
			elif 'allowed vlan' in lines:
				trunk_dict[interface] = [int(v) for v in str.split(lines.split()[-1], ',')]			
	
		result.append(access_dict)
		result.append(trunk_dict)
		
	print(tuple(result))
	return(tuple(result))

get_int_vlan_map('config_sw2.txt')


