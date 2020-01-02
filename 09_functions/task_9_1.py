#!/usr/bin/env python3


access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}


def generate_access_config(intf_vlan_mapping, access_template):
	result = []
	for key in intf_vlan_mapping:
		a = ''
		result.append('inerface ' + key)
		for command in access_template:
			if  command.endswith('vlan'):
				result.append(command + ' ' + str(intf_vlan_mapping[key]))   
			else:
				result.append(command)
#	print(result)
	return result


generate_access_config(access_config, access_mode_template)
