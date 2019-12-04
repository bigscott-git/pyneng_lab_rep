#!/usr/bin/env python3 


london_co = {
        'r1': {
                'location': '21 New Globe Walk',
                'vendor': 'Cisco',
                'model': '4451',
                'ios': '15.4',
                'ip': '10.255.0.1'
        },
        'r2': {
                'location': '21 New Globe Walk',
                'vendor': 'Cisco',
                'model': '4451',
                'ios': '15.4',
                'ip': '10.255.0.2'
        },
        'sw1': {
                'location': '21 New Globe Walk',
                'vendor': 'Cisco',
                'model': '3850',
                'ios': '3.6.XE',
                'ip': '10.255.0.101',
                'vlans': '10,20,30',
                'routing': True
        }
}


device = input('Choose your node aarrrrgh (r1 r2 sw1): ')
option = input(f'choose an option {list(london_co[device].keys())} ')     


print('\n' + '-' * 30 + '\n')
print(london_co[device].get(option.lower(), f'There is no such option as {option}'))
print('\n' + '-' * 30 + '\n')

