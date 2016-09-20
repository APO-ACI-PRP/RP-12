#!/usr/bin/env python

from device import Device
import sys

def fn_sh_version(sw):
    f_sh_version = open('sh_version.xml', "w")
    sh_version= sw.show('show version')
    xml_sh_version=sh_version[1]
    f_sh_version.write (xml_sh_version)
    f_sh_version.close () 

def fn_sh_interface(sw):
    f_sh_interface = open('sh_interface.xml', "w")
    sh_interface= sw.show('show interface')
    xml_sh_interface=sh_interface[1]
    f_sh_interface.write (xml_sh_interface)
    f_sh_interface.close ()  

def fn_sh_vlan(sw):
    f_sh_vlan = open('sh_vlan.xml', "w")
    sh_vlan= sw.show('show vlan')
    xml_sh_vlan=sh_vlan[1]
    f_sh_vlan.write (xml_sh_vlan)
    f_sh_vlan.close ()
    
def fn_sh_int_swports(sw):
    f_sh_int_swports = open('sh_int_swports.xml', "w")
    sh_int_swports= sw.show('show interface switchport')
    xml_sh_int_swports=sh_int_swports[1]
    f_sh_int_swports.write (xml_sh_int_swports)
    f_sh_int_swports.close ()
    
def fn_sh_port_chan_sum(sw):
    f_sh_port_chan_sum = open('sh_port_chan_sum.xml', "w")
    sh_port_chan_sum= sw.show('show port-channel summary')
    xml_sh_port_chan_sum=sh_port_chan_sum[1]
    f_sh_port_chan_sum.write (xml_sh_port_chan_sum)
    f_sh_port_chan_sum.close ()
    
def main(ip_addr):
    print "Gathering files, please wait"
    switch = Device(ip = ip_addr, username = 'admin', password = 'cisco123')
    switch.open()
    sh_version=fn_sh_version(switch)
    sh_interface=fn_sh_interface(switch)
    sh_vlan=fn_sh_vlan(switch)
    sh_int_swports=fn_sh_int_swports(switch)
    sh_port_chan_sum=fn_sh_port_chan_sum(switch)
    
if __name__ == "__main__":
    ip_addr = "172.31.217.143"
    main(ip_addr)
  
