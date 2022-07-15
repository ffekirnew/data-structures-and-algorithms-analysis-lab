# Names:	Fikernew Birhanu	Yohannes Bekele
# IDs:		UGR/9932/13			UGR/3361/13


from stack_implementation import Stack
from open_file import file_opener

def validator(file):
	data = file_opener(file) # this data is the html files in lines
	total_lines = len(data)

	tags = Stack(str, len(data) * 10) # it is not common for more than ten elements to be opened consequetively in a single line

	line_number = 0

	while line_number < total_lines:
		current_line = data[line_number]
		current_index = 0

		while current_index < len(current_line):

			if current_line[current_index] == '<' and current_line[current_index + 1] == '/':

				if tags.isEmpty():
					return False, line_number

				current_index += 2 # jump two steps forward on the index to pass the '<' and the '/' since the goal is to store only the element

				closing_element = ""
				done = False

				while not done:
					current_char = current_line[current_index]

					if current_char == '>':
						done = True
					else:
						closing_element += current_char
						
					current_index += 1

				opening_element = tags.s_pop()

				if closing_element != opening_element:
					return False, line_number


			elif current_line[current_index] == '<':
				current_index += 1 # jump only one to pass '<'

				opening_element = ""
				done = False

				while not done:
					current_char = current_line[current_index]

					if current_char == '>' or current_char == '/' or current_char == ' ':
						done = True
						break
					else:
						opening_element += current_char

					current_index += 1

				if current_char == '/':
					current_index += 2 # to jump the two characters '/' and '>'
				else:
					tags.s_push(opening_element)

			else:
				current_index += 1

		line_number += 1

	return tags.isEmpty(), line_number