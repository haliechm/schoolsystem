import os
import starting_menu
import random
import pickle
from read_file import read_file

def umbridge_administration_work():
	print("\nAh, Professor Umbridge, so nice to see you again. Here lies the source of your power.\nAre you feeling like expelling Harry Potter or erasing Hogwarts' existence today?\n\n")

	menu = {}
	menu["1"] = "Expel a random student"
	menu["2"] = "Delete a school"
	menu["3"] = "Delete all schools"
	menu["4"] = "Fire a random professor"
	menu["5"] = "Exit"

	for k,v in menu.items():
		print("{}) {}".format(k, v))
	
	user_input = input()

	if(user_input == "1"):
		os.system("clear")
		print("OOOOOH Umbridge, would you like to expel a completely random student? It could be a lot of fun...\n")
		lil_menu = {}
		lil_menu["1"] = "Yes, expel away"
		lil_menu["2"] = "No, not today"

		for k,v in lil_menu.items():
			print("{}) {}".format(k, v))


		user_input = input()
		if user_input == "1":
			schools = read_file("Schools.txt")
			i=0
			for school in schools:
				i += 1
			#print("i: " + str(i))
			rand_int = random.randint(0, i-1)
			j = 0
			skool = ""
			for school in schools:
				#print("School: " + str(school[1]))
				#print("Rand int: " + str(rand_int))
				#print("j: " + str(j))
				if rand_int == j:
					skool = school[1]
				j += 1
			try: 
				infile = open(skool, "rb")
				data_dict = pickle.load(infile)
				num_of_students = len(data_dict["Students"])
				rand_int = random.randint(0, num_of_students-1)

				del data_dict["Students"][rand_int]
				infile.close()

				outfile = open(skool, "wb")
				pickle.dump(data_dict, outfile)
				outfile.close()
			except FileNotFoundError:
				#print("NOT FOUND!!!")
				pass
			os.system("clear")
			print("Success! Student successfully expelled\n")
			umbridge_administration_work()

			
		elif user_input == "2":
			os.system("clear")
			umbridge_administration_work()
		else:
			os.system("clear")
			print(">>>>>ERROR 409: Invalid input")
			umbridge_administration_work()
	elif(user_input == "2"):
		school = delete_a_school()
		os.system("clear")
		print_statement = "{} has been destroyed.\n\n".format(school) if school else "ERROR 983: Invalid school name\n\n"
		print(print_statement)
		umbridge_administration_work()
	elif(user_input == "3"):
		os.system("clear")
		delete_all_schools()
	elif(user_input == "4"):
		os.system("clear")
		print("OooOh, Professor Umbridge... shall we fire a completely random professor?\n")
		lil_menu = {}
		lil_menu["1"] = "Yes, of course"
		lil_menu["2"] = "No, not right now"

		for k,v in lil_menu.items():
			print("{}) {}".format(k, v))

		user_input = input()
		if user_input == "1":
			os.system("clear")
			schools = read_file("Schools.txt")
			i=0
			for school in schools:
				i += 1
			rand_int = random.randint(0, i-1)
			j=0
			skool = ""
			for school in schools:
				if rand_int == j:
					skool = school[1]
				j += 1

			infile = open(skool, "rb")
			data_dict = pickle.load(infile)
			num_of_students = len(data_dict["Professors"])
			rand_int = random.randint(0, num_of_students-1)

			del data_dict["Professors"][rand_int]
			infile.close()

			outfile = open(skool, "wb")
			pickle.dump(data_dict, outfile)
			outfile.close()

			os.system("clear")
			print(">>>>>Success! Professor successfully fired\n")
			umbridge_administration_work()
			
		elif user_input == "2":
			os.system("clear")
			umbridge_administration_work()

		else:
			os.system("clear")
			print(">>>>>ERROR 388: Invalid input\n")
			umbridge_administration_work()
	elif(user_input == "5"):
		os.system("clear")	
		starting_menu.starting_menu()	
	else:
		os.system("clear")
		print("ERROR 098: Invalid input\n")
		umbridge_administration_work()

def delete_all_schools():
	os.system("clear")
	print("Are you completely sure you want to delete all schools? There's no going back.\n")
	lil_menu = {}
	lil_menu["1"] = "Yes, I'm sure"
	lil_menu["2"] = "Nevermind."

	for k,v in lil_menu.items():
		print("{}) {}".format(k, v))

	user_input = input()

	if user_input == "1":
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
		os.system("clear")
		print("Good work, Professor Umbridge! You have successfully erased the existence of all schools\n")
		umbridge_administration_work()
	elif user_input == "2":
		os.system("clear")
		print("Mission aborted.")
		umbridge_administration_work()
	else:
		os.system("clear")
		print("ERROR 509: Invalid input")
		umbridge_administration_work()



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
		

