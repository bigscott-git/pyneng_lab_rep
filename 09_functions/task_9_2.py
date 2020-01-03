#!/usr/bin/env python3


trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}


def generate_trunk_config(trunk_template, intf_vlan_mapping):
    result = []
    for keys in intf_vlan_mapping:
        result.append('interface ' + keys)
        for commands in trunk_template:
            if commands.endswith('vlan'):
                vlans = intf_vlan_mapping[keys]
                result.append(commands + ' ' + ','.join([str(v) for v in vlans]))
            else:
                result.append(commands)
    print(result)
    return(result)


generate_trunk_config(trunk_mode_template, trunk_config)
