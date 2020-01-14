#!/usr/bin/env python3

#with open('sh_cdp_n_sw1.txt', 'r') as source:
#        showline = source.read()
#        dev_name = showline[:showline.index('>')].strip()

def parse_cdp_neighbors(command_output):
	res_dict = {}
	output_list = command_output.split('\n')     
	for items in output_list:
		if '>' in items and 'neighbors' in items:
			dev_name = command_output[:command_output.index('>')].strip()
		elif 'Eth' in items and '/' in items:                                 
			init_list = items.split()
			keys = []
			values = []
			keys.append(dev_name)
			keys.append(init_list[1] + init_list[2])
			keys = tuple(keys)
			values.append(init_list[0])
			values.append(init_list[-2] + init_list[-1])
			values = tuple(values)
			res_dict[keys] = values

#	print(res_dict)
	return(res_dict)

if __name__ == '__main__':

        parse_cdp_neighbors(showline)


