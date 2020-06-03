import os
import create_school
import login
from read_file import read_file
from umbridge_menu import umbridge_menu


schools_list = read_file("Schools.txt")
print(schools_list)

def starting_menu(): 
	print(">>>>Welcome<<<<")
	print("Choose 1, 2, 3, or 4 below to get started")

	menu = {}
	menu["1"] = "Create New School"
	menu["2"] = "Login"
	menu["3"] = "Dolores Umbridge Sorcery"
	menu["4"] = "Exit"

	for k,v in menu.items():
		print("{}) {}".format(k,v))	
	
	user_selection = input()
	
	if (user_selection == "1"):
		create_school.create_school(schools_list)
	elif (user_selection == "2"):
		login.login(schools_list)
	elif (user_selection == "3"):
		os.system("clear")
		umbridge_menu()
	elif (user_selection == "4"):
		os.system("clear")
	else :
		os.system("clear")
		print("ERROR 004: Invalid user input\n")
		starting_menu()

