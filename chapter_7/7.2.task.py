#!/usr/bin/env python3

with open('config_sw1.txt', 'r') as source:
	for string in source:
		if string.startswith('!'):
			continue
		else:
			print(string.rstrip())

