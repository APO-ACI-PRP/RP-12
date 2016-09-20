#!/usr/bin/env python
#import json
#import xmltodict
#import sys
#sys.path.append("/Users/znx-osz/PycharmProjects/ACI-Day1")
#from device import Device
#

# Import the modules needed to run the script.
import sys, os
import aci_show_physical_inventory
import aci_show_interfaces
import aci_show_domains
import aci_show_ip_int_brief
import aci_show_tenants
import aci_provisioning
import diagram
import acitoolkit.acitoolkit as ACI
from acitoolkit.acitoolkit import Credentials, Session
from acitoolkit.aciphysobject import Pod

#export TERM = xterm

# Main definition - constants
# set menu_actions dictionary to empty
menu_actions  = {}

# Menu Variables
show1 = 'Show physical inventory'
show2 = 'Show interfaces'
show3 = 'Show bridge domain'
show4 = 'Show ip interface brief'
show5 = 'Show tenants'
#ip_addr = '172.31.216.24'
ip_addr = '172.31.1.191'

login1 ='admin'
password='scotch123'
url='http://' + ip_addr
output = 'my_diagram.png'

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
   os.system('clear')
   print "    !  ACI Python Training - Toolkit Version  !\n"
   print "Please choose the show command you want to start:"
   print "Current IP addresss ", ip_addr
   print ""
   print "1. " + show1
   print "2. " + show2
   print "3. " + show3
   print "4. " + show4
   print "5. " + show5
   print "6. Display ACI fabric diagram"
   print "7. Create ACI components"
   print "8. Select to change IP Address"
   print "\n0. Quit"
   choice = raw_input(" >>  ")
   exec_menu(choice)

   return

# Execute menu
def exec_menu(choice):
	os.system('clear')
	ch = choice.lower()
	if ch == '':
		menu_actions['main_menu']()
	else:
		try:
			menu_actions[ch]()
		except KeyError:
			print "Invalid selection, please try again.\n"
		menu_actions['main_menu']()
	return

# Menu 1 - show version function
def menu1():
	aci_show_physical_inventory.main(login1,password,url)
	print
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return


# Menu 2 - show interface function
def menu2():
	aci_show_interfaces.main(login1,password,url)
	print
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return

# Menu 3 - show interface function
def menu3():
	aci_show_domains.main(login1,password,url)
	print
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return


# Menu 4 - show interface function
def menu4():
	aci_show_ip_int_brief.main(login1,password,url)
	print
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return

# Menu 5 - show interface function
def menu5():
	aci_show_tenants.main(login1,password,url)
	print
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return

def menu6():
	diagram.main(login1,password,url,output)
	#os.system('clear')
	os.system('open -a Preview my_diagram.png')

	#html_process.run()
	print "Finshed"
	print
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return

def menu7():
	aci_provisioning.main(login1,password,url)
	#os.system('clear')
	#html_process.run()
	print
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return

def menu8():
	global ip_addr,url
	print
	ip_addr = raw_input("Enter IP Address ")
	url='http://' + ip_addr
	exec_menu('9')
	return

# Back to main menu
def back():
	menu_actions['main_menu']()

# Exit program
def exit():
	sys.exit()


# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
   'main_menu': main_menu,
   '1': menu1,
   '2': menu2,
   '3': menu3,
   '4': menu4,
   '5': menu5,
   '6': menu6,
   '7': menu7,
   '8': menu8,
   '9': back,
   '0': exit,
}


# =======================
#    DISPLAY FUNCTION
# =======================

def display(return_list):
	global show

	if show == 1:
		show = 0
		for dict1 in return_list:
			for key,value1 in dict1.items():
				print key + " - " + value1


	else:
		count = 0
		for tuple1 in return_list:
			print
			for dict1 in tuple1:
				for key,value1 in dict1.items():
					print key + " - " + value1
					count += 1
					if count > 23:
						os.system("read -p \"Press enter key\"")
						count = 0

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
   # Launch main menu
   main_menu()