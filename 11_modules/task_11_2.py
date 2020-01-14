#!/usr/bin/env python3

from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology



f_list = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']

def create_network_map(filenames):
	final_dict = {}
	super_dict = {}
	for files in filenames:
		with open(files) as source:
			showline = source.read()
			final_dict.update(parse_cdp_neighbors(showline))
	super_dict = final_dict.copy()
	for key in final_dict:
		if key in super_dict.values():
			del super_dict[key]

#	print(super_dict)
#	return(super_dict)
	return(super_dict)


#create_network_map(f_list)


draw_topology(create_network_map(f_list))

