import os
import starting_menu
from read_file import read_file

def umbridge_administration_work():
	print("\nAh, Professor Umbridge, so nice to see you again. Here lies the source of your power.\nAre you feeling like expelling Harry Potter or erasing Hogwarts' existence today?\n\n")

	menu = {}
	menu["1"] = "Expel a student"
	menu["2"] = "Delete a school"
	menu["3"] = "Delete all schools"
	menu["4"] = "Fire a professor"
	menu["5"] = "Exit"

	for k,v in menu.items():
		print("{}) {}".format(k, v))
	
	user_input = input()

	if(user_input == "1"):
		print("expelling a student")
	elif(user_input == "2"):
		school = delete_a_school()
		os.system("clear")
		print_statement = "{} has been destroyed.\n\n".format(school) if school else "ERROR 983: Invalid school name\n\n"
		print(print_statement)
		umbridge_administration_work()
	elif(user_input == "3"):
		delete_all_schools()
		os.system("clear")
		print("Good work, Umbridge! You have successfully erased the existence of all schools.")
		umbridge_administration_work()
	elif(user_input == "4"):
		print("firing a professor")
	elif(user_input == "5"):
		os.system("clear")	
		starting_menu.starting_menu()	
	else:
		os.system("clear")
		print("ERROR 098: Invalid input\n")
		umbridge_administration_work()

def delete_all_schools():
	schools = read_file("Schools.txt")
	for school in schools:
		if school[0] != "Example_School":
			try:
				os.remove("" + school[1])
			except RuntimeError:
				continue

	f = open("Schools.txt", "r")
	lines = f.readlines()
	f.close()

	f = open("Schools.txt", "w")
	for line in lines:
		if line == ("{}\t{}\t{}\n".format("Example_School", "Example_School34", "password")):
			f.write(line)
	f.close()



def delete_a_school():
	os.system("clear")
	print("-----Let's destroy a school today-----\n")
	print("Enter '0' to exit\n")
	found_school = ""

	schools = read_file("Schools.txt")
	print("Choose a school to delete\n")
	i = 1
	for school in schools:
		if(school[0] != "Example_School"):
			print("{}) {}".format(i, school[1]))
			i += 1
	school_del_idx = int(input())
	i=0
	if(school_del_idx == 0):
		os.system("clear")
		umbridge_administration_work()
	for school in schools:
		if i==school_del_idx and school[0] != "Example_School":
			found_school = school[0]

			try:
				os.remove("" + school[1])
				
				f = open("Schools.txt", "r")
				lines = f.readlines()
				f.close()

				f = open("Schools.txt", "w")
				for line in lines:
					if line != ("{}\t{}\t{}\n".format(school[0], school[1], school[2])):
						f.write(line)
				f.close()
			except RuntimeError:
				continue	
		
		i += 1
			
	return found_school
		

