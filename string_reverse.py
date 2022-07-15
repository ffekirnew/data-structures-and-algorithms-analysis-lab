def string_reverse(string):
	if len(string) == 1: return string
	else: return string[-1] + string_reverse(string[:-1])

user_string = input("Please enter the word you want reversed here: ")
print(string_reverse(user_string))