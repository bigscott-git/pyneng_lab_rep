#!/usr/bin/env python3


with open('CAM_table.txt', 'r') as source:
	for string in source:
		if 'DYNAMIC' in string:
			#a = ''
			string = string.replace('DYNAMIC     ', '')
			print(string.rstrip())
			
