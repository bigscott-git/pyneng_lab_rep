#!/usr/bin/env python3


#template = f'''
#{'Protocol:':<20} {'OSPF':<20}
#{'Prefix:':<20} {line[0]:<20}
#{'AD/Metric:':<20} {line[1]:<20}
#{'Next-Hop:':<20} {line[2]:<20}
#{'Last update':<20} {line[3]:<20}
#{'Outbound Interface':<20} {line[4]:<20}'''



with open('ospf.txt') as source:
	for strings in source:
		strings = strings.replace('via', '')
		strings = strings.replace(',', '')
		strings = strings.lstrip('0')
		line = strings.split()

		print( f'''
		{'Protocol:':<20} {'OSPF':<20}
		{'Prefix:':<20} {line[0]:<20}
		{'AD/Metric:':<20} {line[1]:<20}
		{'Next-Hop:':<20} {line[2]:<20}
		{'Last update':<20} {line[3]:<20}
		{'Outbound Interface':<20} {line[4]:<20}''')
