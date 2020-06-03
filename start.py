try:
	s = open("Schools.txt", "r")
	s.close()
except FileNotFoundError:
	s = open("Schools.txt", "w")
	s.close()

import starting_menu
import os

os.system("clear")
starting_menu.starting_menu()
