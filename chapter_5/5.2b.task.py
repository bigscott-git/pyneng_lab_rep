#!/usr/bin/env python3

from sys import argv 

network = argv[1]
# input('enter a network as a.b.c.d/x: ')

ip = network[:network.find('/')]
ip_list = ip.split('.')
ip_str = f'{int(ip_list[0]):08b}{int(ip_list[1]):08b}{int(ip_list[2]):08b}{int(ip_list[3]):08b}'



mask = network[network.find('/'):]       
mask_bin = ('1' * int(mask.strip('/'))) + ('0' * (32 - int(mask.strip('/'))))

mask_first_oct = int(mask_bin[0:8])
mask_second_oct = int(mask_bin[8:16])
mask_third_oct = int(mask_bin[16:24])
mask_fourth_oct = int(mask_bin[24:])

mask_first_oct_int = int(mask_bin[0:8], 2)
mask_second_oct_int = int(mask_bin[8:16], 2)
mask_third_oct_int = int(mask_bin[16:24], 2)
mask_fourth_oct_int = int(mask_bin[24:], 2)

ip_cut = ip_str[:int(mask.strip('/'))] + ('0' * (32 - int(mask.strip('/'))))


print('\n' + '---' * 15 + '\n')

print(f'''
{int(ip_cut[:8], 2):8} {int(ip_cut[8:16], 2):8} {int(ip_cut[16:24], 2):8} {int(ip_cut[24:], 2):8}  
{int(ip_cut[:8]):08} {int(ip_cut[8:16]):08} {int(ip_cut[16:24]):08} {int(ip_cut[24:]):08}''')


print(f'''
Mask:
{mask}
{mask_first_oct_int:8} {mask_second_oct_int:8} {mask_third_oct_int:8} {mask_fourth_oct_int:8}
{mask_first_oct:08} {mask_second_oct:08} {mask_third_oct:08} {mask_fourth_oct:08}''')



print('\n' + '---' * 15 + '\n')
print(mask_bin)

