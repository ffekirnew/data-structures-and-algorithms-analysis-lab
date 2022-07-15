from stack_implementation import Stack

def validator(string):
	matching_delimiters = {'{':'}', '[':']', '(':')', '"':'"', "'": "'", '<':'>'}

	delimiters_stack = Stack(str, len(string))

	for current in string:
		if current in matching_delimiters.keys():
			delimiters_stack.push(current)

		elif current in matching_delimiters.values():
			try:
				previous = delimiters_stack.pop()
				if matching_delimiters[previous] != current:
					return False
			except:
				return False

	return delimiters_stack.isEmpty()