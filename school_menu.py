import os
import shelve
import pickle
import pandas as pd
import starting_menu
import student
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
	menu["7"] = "Exit"

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
		#print("DataDict[Students]: {}".format(data_dict["Students"]))
		#dele_list = data_dict["Students"]
		#dele_stu = dele_list[0]
		#print("Name: {}".format(dele_stu.first_name))
		outfile = open(file_name, "wb")
		pickle.dump(data_dict, outfile)
		outfile.close()
		os.system("clear")
		print("Student successfully added\n")
		school_menu(schools_list, school_name, school_id, school_password)	
		
	elif(user_input == "2"):
		print("2")
	elif(user_input == "3"):
		os.system("clear")
		print("-----Expelling a student-----\n")
		print("Enter '0' to exit\n")
		infile = open(file_name, "rb")
		data_dict = pickle.load(infile)
		print("Choose a student to delete\n\n")	
		i=1
		for stu in data_dict["Students"]:
			print("{}) {}, {}".format(i, stu.last_name, stu.first_name))
			i+=1
		infile.close()

		stu_delete_idx = int(input())
		stu_list = data_dict["Students"]
		if stu_delete_idx == 0:
			os.system("clear")
			school_menu(schools_list, school_name, school_id, school_password)
		elif(stu_delete_idx >= 1 and stu_delete_idx <= len(stu_list)):
			del data_dict["Students"][stu_delete_idx-1]
			os.system("clear")
			outfile = open(file_name, "wb")
			pickle.dump(data_dict, outfile)
			outfile.close()
			school_menu(schools_list, school_name, school_id, school_password)
			
		else:
			os.system("clear")
			print("ERROR 408: Invalid input\n")
			school_menu(schools_list, school_name, school_id, school_password)

	elif(user_input == "4"):
		print("4")
	elif(user_input == "5"):
		print("5")
	elif(user_input == "6"):
		os.system("clear")
		print("-----Enter '3' to exit-----\n\n")
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
		while(True):
			user_input = int(input())
			if user_input == 3:
				os.system("clear")
				break
		school_menu(schools_list, school_name, school_id, school_password)
		
	elif(user_input == "7"):
		os.system("clear")
		starting_menu.starting_menu()
	else:
		os.system("clear")
		print("ERROR 493: Invalid input\n")
		school_menu(schools_list, school_name, school_id, school_password)
	


