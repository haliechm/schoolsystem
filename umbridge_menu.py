import os
import umbridge_administration_work
import starting_menu

def umbridge_menu():

	
	num_of_tries = 3
	not_finished = True
	for i in range(3):
		if(not_finished):
			user_input = input("Is it you, Professor Umbridge? Enter you password to prove yourself. Number of tries left: {}.\n".format(num_of_tries))
			if(user_input == "I</3HarryPotter"):
				not_finished = False
				umbridge_administration_work.umbridge_administration_work()
			elif (num_of_tries >= 2):
				num_of_tries -= 1
				os.system("clear")
				print("Hmmmmmm... incorrect. You are running out of tries...\n") 
			else:
				num_of_tries -= 1
				os.system("clear")
				print("Are you a muggle meddling in Professor Umbridge's business?\n")
				starting_menu.starting_menu()
