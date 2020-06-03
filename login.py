import os
import starting_menu
import school_menu

def login(schools):

	num_of_tries = 3
	not_correct = True

	for i in range(3):
		if(not_correct and num_of_tries >= 1):
			os.system("clear")
			print(">>>>LOGIN<<<<\n")
			print("Number of tries remaining: {}".format(num_of_tries))
			user_input_id = input("Enter your ID:\n")
			user_input_password = input("Enter your password:\n")

			for school in schools:
				if(user_input_id == school[1] and user_input_password == school[2]):
					school_menu.school_menu(schools, school[0], school[1], school[2])
					not_correct = False 
			if not_correct:
				num_of_tries -= 1

	if not_correct:
		os.system("clear")
		print("ERROR 019: Invalid ID or password\n")
		starting_menu.starting_menu()
