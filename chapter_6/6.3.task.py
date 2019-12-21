#!/usr/bin/env python3

trunk_template = [
	'switchport trunk encapsulation dot1q', 'switchport mode trunk',
	'switchport trunk allowed vlan'
]

trunk = {
	'0/1': ['add', '10', '20'],
	'0/2': ['only', '11', '30'],
	'0/4': ['del', '17']
}
for intf, vlan in trunk.items():
	print('interface FastEthernet ' + intf)
	for command in trunk_template:
		if command.endswith('allowed vlan'):
			vlan_list = ''
			for i in vlan:
				vlan_list = vlan_list + i + ' '
			
			print(' {} {}'.format(command, vlan_list))
		else:
			print(' {}'.format(command))
