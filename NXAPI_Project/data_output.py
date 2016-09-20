#!/usr/bin/env python
#
from json2html import *
import sys
import json
import commands

# Path w/nxapi.py & device.py
#
sys.path.append("/Users/crobertson/Desktop/")

# Parse XML file & return requested fields
#

def main():
    h_version = open('h_version.htm', "w")
    for value1 in parse_file(file1,keys1):
        json_output1 = json.dumps( value1, indent=4)
        infoFromJson1 = json.loads(json_output1)
        html_output1 = json2html.convert(json = infoFromJson1)
        h_version.write(html_output1)
    h_version.close()
    # Run parse_file for file2
    #
    h_intf = open('h_intf.htm', "w")
    tuple_dict_list2 = (parse_file(file2,keys2,index2))
    for tuple2 in tuple_dict_list2:
        for dict2 in tuple2:
            json_output2 = json.dumps( dict2, indent=4)
            infoFromJson2 = json.loads(json_output2)
            html_output2 = json2html.convert(json = infoFromJson2)
            print html_output2
            h_intf.write(html_output2)
    h_intf.close()
    # Run parse_file for file3
    #
    h_vlan = open('h_vlan.htm', "w")
    tuple_dict_list3 = (parse_file(file3,keys3,index3))
    for tuple3 in tuple_dict_list3:
        for dict3 in tuple3:
            json_output3 = json.dumps( dict3, indent=4)
            infoFromJson3 = json.loads(json_output3)
            html_output3 = json2html.convert(json = infoFromJson3)
            print html_output3
            h_vlan.write(html_output3)
    h_vlan.close()
    # Run parse_file for file4
    #
    h_swprts = open('h_swprts.htm', "w")
    tuple_dict_list4 = (parse_file(file4,keys4,index4))
    for tuple4 in tuple_dict_list4:
        for dict4 in tuple4:
            json_output4 = json.dumps( dict4, indent=4)
            infoFromJson4 = json.loads(json_output4)
            html_output4 = json2html.convert(json = infoFromJson4)
            print html_output4
            h_swprts.write(html_output4)
    h_swprts.close()
    # Run parse_file for file5
    #
    h_prt_chan = open('h_prt_chan.htm', "w")
    tuple_dict_list5 = (parse_file(file5,keys5,index5))
    for tuple5 in tuple_dict_list5:
        for dict5 in tuple5:
            json_output5 = json.dumps( dict5, indent=4)
            infoFromJson5 = json.loads(json_output5)
            html_output5 = json2html.convert(json = infoFromJson5)
            print html_output5
            h_prt_chan.write(html_output5)
    h_prt_chan.close()


def parse_file(filename,keys,index_field=None):

    xml_file = open(filename)

    list1 = []
    dict1 = {}
    tuple1 = ()
    index_exist = False
    new_tuple = False

    for line in xml_file:
        line = line.lstrip()

        if index_field != None:
            if line.startswith('<' + index_field[0] + '>'):
                if len(tuple1) > 0:
                    list1.append(tuple1)
                    tuple1=()
                pos1 = line.find('>')
                pos1 += 1
                pos2 = line.find('</' + index_field[0])
                dict1 = {index_field[0]:line[pos1:pos2]}
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
                    list1.reverse()
    if len(tuple1) > 0:

        list1.append(tuple1)
        tuple1=()

    return list1

# Set "show command" XML Output file for parse_file
#
file1 = 'sh_version.xml'
file2 = 'sh_interface.xml'
file3 = 'sh_vlan.xml'
file4 = 'sh_int_swports.xml'
file5 = 'sh_port_chan_sum.xml'

# Set desired fields/keys within "show command" XML Output for return from parse_file
#
index1 = []
index2 = ['interface']
index3 = ['vlanshowbr-vlanid-utf']
index4 = ['interface']
index5 = ['group']

#
keys1 = ['kick_file_name', 'proc_board_id', 'host_name','chassis_id']
keys2 = ['state', 'eth_speed', 'eth_duplex', 'eth_ip_addr', 'eth_mask']
keys3 = ['vlanshowbr-vlanstate', 'vlanshowbr-vlanid', 'vlanshowplist-ifidx', 'vlanshowbr-vlanname']
keys4 = ['switchport', 'oper_mode', 'access_vlan', 'access_vlan_name', 'native_vlan', 'native_vlan_name', 'trunk_vlans']
keys5 = ['port-channel', 'layer', 'status', 'type', 'prtcl', 'port', 'port-status']
 
# Run parse_file for file1 and write to html output
#


