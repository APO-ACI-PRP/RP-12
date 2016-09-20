#
from dagpype import *
import sys
import os


h_version = open('h_version.htm', "r")
h_intf = open('h_intf.htm', "r")
h_vlan = open('h_vlan.htm', "r")
h_swprts = open('h_swprts.htm', "r")
h_prt_chan = open('h_prt_chan.htm', "r")

print '<style type="text/css">'
print '<!--@import url("style.css");-->'
print '</style>'

print ''
print '<div id="hardware">'
print '<!-- Hardware/Version Data HTML Table -->'
print '<img src="tux_cisco.png" alt="Cisco NX-OS Programability w/NX-API" height="198" width="140"></img>'
print '<table align="right" table id="gradient-style">'
print '<tr><th colspan=''2'' align=center>Nexus Hardware/Version Info Table</th></tr>'
stream_lines('h_version.htm') | filt(lambda l: l.replace('<table border="1">', '')) |  filt(lambda l: l.replace('</table>', '')) | to_stream(sys.stdout)
print '<!-- Hardware/Version Data HTML Table -->'
print '</table>'
print '</div>'
print ''

print '<div id="container">'
print ''
print '<div id="switchport">'
print '<!-- Switchport Data HTML Table -->'
print '<table table id="gradient-style">'
print '<tr><th colspan=''2'' align=center>Switchport Info Table</th></tr>'
stream_lines('h_swprts.htm') | filt(lambda l: l.replace('</table>', '')) | filt(lambda l: l.replace('<table border="1">', '')) | to_stream(sys.stdout)
print '<!-- Switchport Data HTML Table -->'
print '</table>'
print '</div>'
print ''

print ''
print '<div id="interface">'
print '<!-- Interface Data HTML Table -->'
print '<table table id="gradient-style">'
print '<tr><th colspan=''2'' align=center>Interface Info Table</th></tr>'
stream_lines('h_intf.htm') | filt(lambda l: l.replace('</table>', '')) | filt(lambda l: l.replace('<table border="1">', '')) | to_stream(sys.stdout)
print ''
print '<!-- Interface Data HTML Table -->'
print '</table>'
print '</div>'
print ''

print ''
print '<div id="vlan">'
print '<!-- VLAN Data HTML Table -->'
print '<table table id="gradient-style">'
print '<tr><th colspan=''2'' align=center>VLAN Info Table</th></tr>'
stream_lines('h_vlan.htm') | filt(lambda l: l.replace('</table>', '')) | filt(lambda l: l.replace('<table border="1">', '')) | to_stream(sys.stdout)
print ''
print '<!-- VLAN Data HTML Table -->'
print '</table>'
print '</div>'
print ''

print ''
print '<div id="port-channel">'
print '<!-- Port-Channel Data HTML Table -->'
print '<table table id="gradient-style">'
print '<tr><th colspan=''2'' align=center>Port-Channel Info Table</th></tr>'
stream_lines('h_prt_chan.htm') | filt(lambda l: l.replace('</table>', '')) | filt(lambda l: l.replace('<table border="1">', '')) | to_stream(sys.stdout)
print ''
print '<!-- Port-Channel Data HTML Table -->'
print '</table>'
print '</div>'
print ''
print '</div>'

h_version.close()
h_intf.close()
h_vlan.close()
h_swprts.close()
h_prt_chan.close()



