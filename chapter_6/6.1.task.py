#!/usr/bin/env python3


mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

maclist = []


for addr in mac:
	a = addr.replace(':', '.')
	maclist.append(a)

print('\n' + 30 * '*' + '\n')
print(maclist)
print('\n' + 30 * '*' + '\n')

