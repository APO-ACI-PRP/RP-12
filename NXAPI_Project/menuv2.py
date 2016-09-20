#!/usr/bin/env python
#import json
#import xmltodict
#import sys
#sys.path.append("/Users/znx-osz/PycharmProjects/ACI-Day1")
#from device import Device
#

# Import the modules needed to run the script.
import sys, os
import switch
import data_collect
import data_output
#import html_process
#export TERM = xterm

# Main definition - constants
# set menu_actions dictionary to empty
menu_actions  = {}
show = 0

# Menu Variables
show1 = 'show version'
show2 = 'show interface'
show3 = 'show vlan'
show4 = 'show interface switchports'
show5 = 'show port-channel summary'
ip_addr = '172.31.217.143'


# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
   os.system('clear')
   print "    !  ACI Python Training  !\n"
   print "Please choose the show command you want to start:"
   print "Current IP addresss ", ip_addr
   print ""
   print "1. " + show1
   print "2. " + show2
   print "3. " + show3
   print "4. " + show4
   print "5. " + show5
   print "6. Collect all data for switch"
   print "7. Select to change IP Address"
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
	global show
	returned_list = []
	show = 1
	returned_list = switch.run('show1',ip_addr)
	display(returned_list)
	print
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return


# Menu 2 - show interface function
def menu2():
	returned_list = switch.run('show2',ip_addr)
	display(returned_list)
	print
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return

# Menu 3 - show interface function
def menu3():
	returned_list = switch.run('show3',ip_addr)
	display(returned_list)
	print
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return


# Menu 4 - show interface function
def menu4():
	returned_list = switch.run('show4',ip_addr)
	display(returned_list)
	print
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return

# Menu 5 - show interface function
def menu5():
	returned_list = switch.run('show5',ip_addr)
	display(returned_list)
	print
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return

def menu6():
	data_collect.main(ip_addr)
	os.system('clear')
	data_output.main()
	os.system('clear')
	os.system('python html_process.py > boiled_nxos.html')

	#html_process.run()
	os.system("/Applications/Firefox.app/Contents/MacOS/firefox-bin boiled_nxos.html")
	print "Finshed"
	print
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return

def menu7():
	global ip_addr
	print
	ip_addr = raw_input("Enter IP Address ")
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
