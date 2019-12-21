#!/usr/bin/env python3


a = input('Enter IP address: ')
b = a.split('.')

c = []

for i in b:
	i = int(i)
	c.append(i)

#print(c)


if c[0] in range (1,224):
	print('unicast')

elif c[0] in range (224,240):
	print('multicast')

elif c == [255, 255, 255, 255]:
	print('local broadcast')

elif c == [0, 0, 0, 0]:
	print('unassigned')

else:
	print('unused')


