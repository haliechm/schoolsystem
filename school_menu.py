import os
import shelve
import pickle
import pandas as pd
import starting_menu
import student
import professor
from read_file import read_file

def school_menu(schools_list, school_name, school_id, school_password):
	os.system("clear")

	print("Welcome {}\n".format(school_name))
		
	menu = {}
	menu["1"] = "Enroll a student"
	menu["2"] = "Hire a professor"
	menu["3"] = "Expel a student"
	menu["4"] = "Fire a professor"
	menu["5"] = "Change Password"
	menu["6"] = "See list of all students"
	menu["7"] = "See list of all professors"
	menu["8"] = "Exit"

	for k,v in menu.items():
		print("{}) {}".format(k,v))

	file_name = "{}".format(school_id)
	user_input = input()

	if(user_input == "1"):
		os.system("clear")
		print("------Creating a new student profile------")
		first_name = input("Enter first name of student: \n")
		last_name = input("Enter last name of student: \n")
		major = input("Enter student's area of study: \n")
		year = input("Enter student's age: \n")

		new_student = student.Student(first_name, last_name, major, year)


		infile = open(file_name, "rb")
		data_dict = pickle.load(infile)
		data_dict["Students"].append(new_student)
		infile.close()
		outfile = open(file_name, "wb")
		pickle.dump(data_dict, outfile)
		outfile.close()
		os.system("clear")
		print("Student successfully added\n")
		school_menu(schools_list, school_name, school_id, school_password)	
		
	elif(user_input == "2"):
		os.system("clear")
		print("-----Hiring a professor-----\n\n")
		first_name = input("Enter professor's first name:\t")
		last_name = input("Enter professor's last name:\t")
		salary = input("Enter professor's salary\t")

		new_professor = professor.Professor(first_name, last_name, salary)

		infile = open(file_name, "rb")
		data_dict = pickle.load(infile)
		data_dict["Professors"].append(new_professor)
		infile.close()

		outfile = open(file_name, "wb")
		pickle.dump(data_dict, outfile)
		outfile.close()

		os.system("clear")
		print(">>>>>Professor successfully added\n")
		school_menu(schools_list, school_name, school_id, school_password)
		
	elif(user_input == "3"):
		os.system("clear")
		print("-----Expelling a student-----\n\n")
		print("Enter number of student to expel or enter any other key to exit\n")
		infile = open(file_name, "rb")
		data_dict = pickle.load(infile)
		print("Choose a student to delete\n\n")	
		i=1
		for stu in data_dict["Students"]:
			print("{}) {}, {}".format(i, stu.last_name, stu.first_name))
			i+=1
		infile.close()

		user_input = input()
		try:
			if(int(user_input) >=1 or int(user_input) <= len(data_dict["Students"])):
				del data_dict["Students"][int(user_input)-1]
				outfile = open(file_name, "wb")
				pickle.dump(data_dict, outfile)
				outfile.close()
				os.system("clear")
				print(">>>>>Student successfully expelled\n")
				school_menu(schools_list, school_name, school_id, school_password)
			else:
				os.system("clear")
				school_menu(schools_list, school_name, school_id, school_password)


		except ValueError:
			os.system("clear")
			school_menu(schools_list, school_name, school_id, school_password)


	elif(user_input == "4"):
		os.system("clear")
		print("-----Enter number of professor to fire or enter any other key to exit-----\n\n")

		infile = open(file_name, "rb")
		data_dict = pickle.load(infile)
		i = 1
		for prof in data_dict["Professors"]:
			print("{}) {}, {}".format(i, prof.last_name, prof.first_name))
			i += 1

		infile.close()

		user_input = input()
		try:
			if(int(user_input) >= 1 or int(user_input) <= len(data_dict["Professors"])):
				del data_dict["Professors"][int(user_input) - 1]
				os.system("clear")
				outfile = open(file_name, "wb")
				pickle.dump(data_dict, outfile)
				outfile.close()
				print(">>>>>Professor successfully fired\n")
				school_menu(schools_list, school_name, school_id, school_password)
			else:
				os.system("clear")
				school_menu(schools_list, school_name, school_id, school_password)

		except ValueError:
			os.system("clear")
			school_menu(schools_list, school_name, school_id, school_password)
			
	elif(user_input == "5"):
		print("5")
	elif(user_input == "6"):
		os.system("clear")
		print("-----Enter any key to exit-----\n\n")
		infile = open(file_name, "rb")
		data_dict = pickle.load(infile)
		name_list = []
		for stu in data_dict["Students"]:
			name_list.append("{}, {}".format(stu.last_name.title(), stu.first_name.title()))
		name_list.sort()

		for stu in name_list:
			print(stu)
		
		#for stu in data_dict["Students"]:
			#print("{}, {}".format(stu.last_name, stu.first_name))
		infile.close()
		user_input = input()
		school_menu(schools_list, school_name, school_id, school_password)
		
	elif(user_input == "7"):
		os.system("clear")
		print("-----Enter any key to exit-----\n\n")

		infile = open(file_name, "rb")
		data_dict = pickle.load(infile)

		for prof in data_dict["Professors"]:
			print("{}\t{}\t{}".format(prof.first_name, prof.last_name, prof.salary))

		infile.close()

		u_input = input()
		os.system("clear")
		school_menu(schools_list, school_name, school_id, school_password)
		
	elif(user_input == "8"):
		os.system("clear")
		starting_menu.starting_menu()
	else:
		os.system("clear")
		print("ERROR 493: Invalid input\n")
		school_menu(schools_list, school_name, school_id, school_password)
	


