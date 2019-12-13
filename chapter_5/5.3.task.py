#!/usr/bin/env python3




intmode = input('Enter interface mode (access/trunk): ')
interface = input('Enter interface type and number (example: eth0/0): ')
vlans = input('Enter VLANS (for trunk interface - devided by comma): ')




mydict = {
'access': f' switchport mode access \n switchport access vlan {vlans} \n switchport nonegotiate \n spanning-tree portfast \n spanning-tree bpduguard enable',
'trunk': f' switchport trunk encapsulation dot1q \n switchport mode trunk \n switchport trunk allowed vlan {vlans}'
}


print('interface' + interface)
print(mydict[intmode])

