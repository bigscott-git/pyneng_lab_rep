#!/usr/bin/env python3



with open('CAM_table.txt', 'r') as source:
	a = []
	for string in source:
		if 'DYNAMIC' in string:
			string = string.replace('DYNAMIC     ', '')
			a.append(string)
	a.sort()
	print(''.join(a))
	#		print(string.rstrip())
