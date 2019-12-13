#!/usr/bin/env python3


intmode = input('Enter interface mode (access/trunk): ')
interface = input('Enter interface type and number (example: eth0/0): ')
portmode = {'access': 'Enter vlan ID: ', 'trunk': 'Enter allowed VLANs: '}
vlans = input(portmode[intmode])



mydict = {
'access': f' switchport mode access \n switchport access vlan {vlans} \n switchport nonegotiate \n spanning-tree portfast \n spanning-tree bpduguard enable',
'trunk': f' switchport trunk encapsulation dot1q \n switchport mode trunk \n switchport trunk allowed vlan {vlans}'
}

print('\n' + '-' * 30 + '\n')
print('interface ' + interface)
print(mydict[intmode])
print('\n' + '-' * 30 + '\n')

