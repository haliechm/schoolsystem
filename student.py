class Student():
	num_of_students = 0

	def __init__(self, f_name, l_name, major, year):
		self.first_name = f_name
		self.last_name = l_name
		self.major = major
		self.year = year
		self.courses = []
		self.credits = 0

	def add_course(self, course):
		self.courses.append(course)

	def change_major(self, new_major):
		self.major = new_major
	
	def change_name(self, new_name):
		self.name = new_name


