#!/usr/bin/env python
#
from json2html import *
from device import Device
import xml.sax
import xmltodict
import json
import re
import sys

# Path w/nxapi.py & device.py
#
sys.path.append("/Users/crobertson/Desktop/")

''''
# Enter via raw_input N9K IP & User/Password Info
#
n9k_ip = raw_input("Enter N9K IP Address:")
n9k_user = raw_input("Username:")
n9k_pass = raw_input("Password:")
'''
# Hardcoded N9K IP & User/Password Info
#
n9k_ip = '172.31.217.143'
n9k_user = 'admin'
n9k_pass = 'cisco123'

# Nexus IP, Credentials, and Open NX-API Connection
#
n9k = Device(ip=n9k_ip, username=n9k_user, password=n9k_pass)
n9k.open()

# Open file(s) for collecting output data
#
f_intstat = open('intstat.dat', "w")
f_swprts = open('swprts.dat', "w")
f_ipprts = open('ipprts.dat', "w")
f_hard = open('hardware.dat', "w")

# Collect & print "show hardware output
#
sh_hardware = n9k.show('show hardware')
hardware_dict = xmltodict.parse(sh_hardware[1])
hw_data = hardware_dict['ins_api']['outputs']['output']['body']
hw_data_output = json.dumps( hardware_dict, indent=4)
hw_dict = {}
hw_dict['os_version'] = hw_data['kickstart_ver_str']
hw_dict['type'] = hw_data['chassis_id']
hw_dict['memory'] = hw_data['memory'] + hw_data['mem_type']
hw_dict['hostname'] = hw_data['host_name']
hw_dict['bootflash'] = hw_data['bootflash_size']
hw_dict['last_reboot_reason'] = hw_data['rr_reason']
hw_dict['uptime'] = '{} day(s) {} hour(s) {} min(s) {} sec(s)'.format(hw_data['kern_uptm_days'],hw_data['kern_uptm_hrs'],hw_data['kern_uptm_mins'],hw_data['kern_uptm_secs'])
ser_nums = {}
ser_nums_data = hardware_dict['ins_api']['outputs']['output']['body']['TABLE_slot']['ROW_slot']['TABLE_slot_info']['ROW_slot_info']
for each in ser_nums_data:
        if 'serial_num' in each.keys():
                key = each['serial_num']
                ser_nums[key] = each['model_num']
hw_dict['serial_numbers'] = ser_nums

''''
print hw_dict
'''

# Collect & print "show interface status" output
#
sh_int_stat = n9k.show('show interface status')
intstat_dict = xmltodict.parse(sh_int_stat[1])
intstat = intstat_dict['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
intstat_output = json.dumps( intstat_dict, indent=4)

''''
for each in intstat:
	if each['state'] == 'connected':
		print each
'''

# Collect & print "show interface switchport [interface] " output
#
sh_int_swprt = n9k.show('show interface switchport')
swprts_dict = xmltodict.parse(sh_int_swprt[1])
swprts = swprts_dict['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
swprts_output = json.dumps( swprts_dict, indent=4)

''''
for each in swprts:
	print each
'''

# Collect & print "show ip interface" output
#
sh_int_ipprt = n9k.show('show ip interface')
ipprts_dict = xmltodict.parse(sh_int_ipprt[1])
ipprts = ipprts_dict['ins_api']['outputs']['output']['body']['TABLE_intf']
ipprts_output = json.dumps( ipprts_dict, indent=4)

''''
for each in ipprts:
	ipprts2 = each['ROW_intf']
	for each2,value in ipprts2.items():
	print data_string
'''

# Generate HTML Table(s) from JSON Output(s)
#
#
infoFromJson = json.loads(hw_data_output)
print '<!-- Hardware Data HTML Table --!>'
print json2html.convert(json = infoFromJson)
print '<!-- Hardware Data HTML Table --!>'
#
infoFromJson = json.loads(intstat_output)
print '<!-- Interface Status HTML Table --!>'
print json2html.convert(json = infoFromJson)
print '<!-- Interface Status HTML Table --!>'
#
infoFromJson = json.loads(swprts_output)
print '<!-- Switchport Status HTML Table --!>'
print json2html.convert(json = infoFromJson)
print '<!-- Switchport Status HTML Table --!>'
#
infoFromJson = json.loads(ipprts_output)
print '<!-- IP Interface Status HTML Table --!>'
print json2html.convert(json = infoFromJson)
print '<!-- IP Interface Status HTML Table --!>'

# Write output(s) to file(s) & close
#
f_intstat.write (intstat_output)
f_swprts.write (swprts_output)
f_ipprts.write (ipprts_output)
f_hard.write (hw_data_output)
f_hard.close ()
f_intstat.close ()
f_swprts.close ()
f_ipprts.close ()