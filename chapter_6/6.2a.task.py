#!/usr/bin/env python3

a = input('Enter IP address: ')
b = a.split('.')


for i in b:
	try:
		int(i)
	except ValueError:
		print("Incorrect IP address!")
		break
	else:
		if int(i) not in range(0,256):
                	print("Incorrect IP address!")
                	break
else:
	if int(b[0]) in range (1,224):
		print('unicast')
	elif int(b[0]) in range (224,240):
		print('multicast')

	elif b == ['255', '255', '255', '255']:
		print('local broadcast')

	elif b == ['0', '0', '0', '0']:
		print('unassigned')

	elif b == []:
		print('unused')
