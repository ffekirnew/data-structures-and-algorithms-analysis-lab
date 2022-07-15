def file_opener(path):
	with open(path, mode='r') as html_file:
		data = html_file.readlines()

	return data