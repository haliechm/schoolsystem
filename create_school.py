import os
import pickle
import pandas as pd
import random
import starting_menu

def create_school(schools_list):

	os.system("clear")

	print("Ah! A new school is being created\n")
	school_name = input("Choose a name for your school (w/o spaces)\n")
	school_password = input("Create a password to login to your account (w/o spaces)\n")

	school_id = school_name + str(random.randint(10,99))
	os.system("clear")
	print("Your ID to login is: {} and your password is: {}\n".format(school_id, school_password))
	
	schools_file = open("Schools.txt", "a")


	line = "{}\t{}\t{}\n".format(school_name, school_id, school_password) 	
	schools_file.write(line)


	data_dict = {"Students":[], "Professors":[], "Courses":[]}
	file_name = "{}".format(school_id)
	outfile = open(file_name, "wb")
	pickle.dump(data_dict, outfile)
	outfile.close()


	schools_file.close()

	schools_list.append([school_name, school_id, school_password])
	starting_menu.starting_menu()
