#!/usr/bin/env python3


ignore = ['duplex', 'alias', 'Current configuration']

with open('config_sw1.txt', 'r') as source:
	for string in source:
		if string.startswith('!'):
			continue
		for i in ignore:
			if i in string:
				break
				
		else:
			print(string.rstrip())
