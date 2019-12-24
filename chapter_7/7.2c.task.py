#!/usr/bin/env python3

ignore = ['duplex', 'alias', 'Current configuration']


with open('config_sw1.txt', 'r') as source, open('config_sw1_cleared.txt', 'a') as dest:
	for string in source:
		for i in ignore:
			if i in string:
				break
				
		else:
			dest.write(string)
