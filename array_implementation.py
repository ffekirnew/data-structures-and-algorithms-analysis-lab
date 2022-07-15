class Array:

	"""
	An array is a data structure with the following key properties:
	* it only contains a fixed number of elements once initialized
	* it only contains elements of the same data type

	* it has time-complexities:
		* O(1) for random access
		* O(n) for inserting and removing elements
	"""

	def __init__(self, data_type, length):
		self.array = [None] * length
		self.size = length
		self.data_type = data_type
		self.lastindex = 0

	def __str__(self):
		return "{}".format(self.array)

	def __repr__(self):
		return "{}".format(self.array)

	def __getitem__(self, item):
		'''
		this special method allows the elements of the objects of the class to 
		be accessed by using indexes and also makes the objects iterable
		'''

		return self.array[item]

	def __len__(self):
		'''
		this method allows the objects of the class to respond to the len()
		method call
		'''
		return self.size

	def __bytes__(self):
		pass

	def __eq__(self, other):
		pass

	def __abs__(self):
		pass

	def __bool__(self):
		return self.array != []

	def insert(self, index, new_data):
		'''
		This method is used to insert elements into the array to a specific index
		time-complexity = O(n)
		'''
		if type(new_data) == self.data_type:
			if not self.__is_full__():
				if index <= self.lastindex:
					self.__shift_right__(index)
					self.array[index] = new_data

				else:
					print("There are empty places before the index inserted.")
			else:
				print("Array is full.")
		else:
			print("The array only accepts elements of {}.".format(self.data_type))

	def append(self, new_data):
		'''
		This method is used to insert elements to the end of the array
		time-complexity = O(1)
		'''
		if not self.__is_full__():
			self.array[self.lastindex] = new_data
			self.lastindex += 1
		else:
			print("Array is full.")
	
	def remove(self, index):
		'''
		This method is used to remove elements from a specific index on the array 
		time-complexity = O(n)
		'''
		if index < self.lastindex:
			self.array[index] = None
			self.__shift_left__(index)
		else:
			print("The index is out of bounds.")

	def pop(self):
		'''
		This method is used to remove the element at the end of the array
		returns the removed element
		time-complexity = O(1)
		'''
		if not self.__is_empty__():
			self.lastindex -= 1
			self.array[self.lastindex] = None
		else:
			return "Array is currently empty."
		

	def __is_empty__(self):
		'''
		This method returns a boolean indicating if the array is currently empty
		time-complexity = O(1) [simple comparison]
		'''
		return self.lastindex == 0

	def __is_full__(self):
		'''
		This method returns a boolean indicating if the array is currently full
		time-complexity = O(1) [simple comparison]
		'''
		return self.lastindex == self.size

	def __shift_right__(self, start_index):
		'''
		This method shifts all elements to the right starting from a specific index
		returns nothing
		time-complexity = O(n)
		'''
		for index in range(self.size - 2, start_index - 1, -1):
			self.array[index + 1] = self.array[index]

		self.lastindex += 1

	def __shift_left__(self, start_index):
		'''
		This method shifts all elements to the left starting from a specific index
		returns nothing
		time-complexity = O(n)
		'''
		for index in range(start_index + 1, self.size):
			self.array[index - 1] = self.array[index]
			
		self.lastindex -= 1
		self.array[self.lastindex] = None

	def migrate(self):
		'''
		This a method to be used in the future when an array is full and the user wants 
		to add another element, we can then make another bigger arrray, copy every element 
		of the existing array to the newly created array, delete the smaller array and assign 
		the new array as the original one
		'''
		pass