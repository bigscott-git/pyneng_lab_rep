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

port_security_template = [
'switchport port-security maximum 2',
'switchport port-security violation restrict',
'switchport port-security'
]

def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
	result = []
	for key in intf_vlan_mapping:
		result.append('interface ' + key)
		for command in access_template:
			if command.endswith('vlan'):
				result.append(command + ' ' + str(intf_vlan_mapping[key]))   
			else:
				result.append(command)

		else:
			if psecurity:
				result += psecurity
	print(result)
	return(result)


generate_access_config(access_config, access_mode_template, port_security_template)
