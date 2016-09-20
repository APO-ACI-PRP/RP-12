#!/usr/bin/
from device import Device
import os

SHOW_COMMAND = {
	'show1' : 'show version',
	'show2' : 'show interface',
	'show3' : 'show vlan',
	'show4' : 'show interface switchport',
	'show5' : 'show port-channel summary',
}

SHOW_FILE = {
	'show1' : 'sh_version.xml',
	'show2' : 'sh_interface.xml',
	'show3' : 'sh_vlan.xml',
	'show4' : 'sh_int_swport.xml',
	'show5' : 'sh_port_chan_sum.xml',
}

SHOW_KEYS = {
	'show1' : ['kick_file_name', 'proc_board_id', 'host_name', 'memory','chassis_id'],
	'show2' : ['state', 'eth_ip_addr', 'eth_ip_mask', 'eth_speed', 'eth_duplex', 'eth_link_flapped', 'eth_clear_counters'],
	'show3' : ['vlanshowbr-vlanstate', 'vlanshowplist-ifidx','vlanshowbr-vlanname'],
	'show4' : ['switchport', 'oper_mode','access_vlan', 'access_vlan_name', 'native_vlan','native_vlan_name','trunk_vlans'],
	'show5' : ['port-channel','layer', 'status', 'type','prtcl','port','port-status']
}

SHOW_INDEX = {
	'show1' : None,
	'show2' : 'interface',
	'show3' : 'vlanshowbr-vlanid-utf',
	'show4' : 'interface',
	'show5' : 'group',
}

#

def run(show,ip_addr):
	#print show
	return_list =[]
	#print SHOW_FILE[show]
	#print SHOW_KEYS[show]
	#print SHOW_INDEX[show]

	#ip_addr = '172.31.217.143'
	#ip_addr = '172.31.100.90'
	create_file(ip_addr,SHOW_COMMAND[show],SHOW_FILE[show])
	return_list = parse_file(SHOW_FILE[show],SHOW_KEYS[show],SHOW_INDEX[show])
	#print type(return_list)
	return return_list

def create_file(ip_address,command,filename):
	sw1 = Device(ip = ip_address, username = 'admin', password = 'cisco123')
	sw1.open()
	command1 = sw1.show(command)
	try:
		os.remove(filename)
	except:
		pass
	file1 = open(filename,'w')
	file1.write(command1[1])
	file1.close()

def parse_file(filename,keys,index_field=None):
	#print "filename ", filename
	#print "keys ", keys
	#print "index ", index_field

	xml_file = open(filename)

	list1 = []
	dict1 = {}
	tuple1 = ()
	index_exist = False
	new_tuple = False

	for line in xml_file:
		line = line.lstrip()

		if index_field != None:
			if line.startswith('<' + index_field + '>'):
				if len(tuple1) > 0:
					list1.append(tuple1)
					tuple1=()
				pos1 = line.find('>')
				pos1 += 1
				pos2 = line.find('</' + index_field)
				dict1 = {index_field:line[pos1:pos2]}
				tuple1 = (dict1,)
				index_exist = True

			elif index_exist == True:
				for key in range(len(keys)):
					if line.startswith('<' + keys[key] + '>'):
						pos1 = line.find('>')
						pos1 += 1
						pos2 = line.find('</' + keys[key])
						dict1 = {keys[key]:line[pos1:pos2]}
						tuple1 += (dict1,)


		else:
			for key in range(len(keys)):
				if line.startswith('<' + keys[key] + '>'):
					pos1 = line.find('>')
					pos1 += 1
					pos2 = line.find('</' + keys[key])
					dict1 = {keys[key]:line[pos1:pos2]}
					list1.append(dict1)
	if len(tuple1) > 0:

		list1.append(tuple1)
		tuple1=()

	return list1

