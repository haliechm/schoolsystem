def read_file(file):
	opened_file = open(file, "r")
	list_of_lines = []

	for line in opened_file:
		line = line.split()
		list_of_lines.append(line)

	return list_of_lines
