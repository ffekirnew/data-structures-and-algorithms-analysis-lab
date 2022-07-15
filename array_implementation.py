# Names:	Fikernew Birhanu	Yohannes Bekele
# IDs:		UGR/9932/13			UGR/3361/13


class Array:
	"""
	An __array is a data structure with the following key properties:
	* it only contains a fixed number of elements once initialized
	* it only contains elements of the same data type

	* it has time-complexities:
		* O(1) for random access
		* O(n) for inserting and removing elements
	"""

	def __init__(self, data_type, length):
		self.__array = [None] * length
		self.__size = length
		self.__data_type = data_type
		self.__lastindex = -1

	def __repr__(self):
		return "Array: {}".format(self.__array)

	def __getitem__(self, item):
		'''
		this special method allows the elements of the objects of the class to 
		be accessed by using indexes and also makes the objects iterable
		''' 
		return self.__array[item]

	def __len__(self):
		'''
		this method allows the objects of the class to respond to the len()
		method call
		'''
		return self.__size

	def insert(self, index, new_data):
		'''
		This method is used to insert elements into the __array to a specific index
		time-complexity = O(n)
		'''
		if isinstance(new_data, self.__data_type):
			if not self.__is_full__():
				if index <= self.__lastindex + 1:
					self.__shift_right__(index)
					self.__array[index] = new_data

				else: raise IndexError("index is out of bounds. There are empty places before this index.")
			else: raise IndexError("the array is full.")
		else: raise TypeError("only elements of {} are allowed in this array.".format(self.__data_type))

	def add(self, new_data):
		'''
		This method is used to insert elements to the end of the __array
		time-complexity = O(1)
		'''
		self.insert(self.__lastindex + 1, new_data)
	
	def remove(self, index):
		'''
		This method is used to remove elements from a specific index on the __array 
		time-complexity = O(n)
		'''
		if not self.__is_empty__():
			if index < self.__lastindex + 1:
				self.__array[index] = None
				self.__shift_left__(index)
			else:
				raise IndexError("Index out of bounds. No element exists at the given index.")
		else:
			raise IndexError("The array is empty.")

	def pop(self):
		'''
		This method is used to remove the element at the end of the __array
		returns the removed element
		time-complexity = O(1)
		'''
		if not self.__is_empty__():
			self.__lastindex -= 1
			temp = self.__array[self.__lastindex + 1]
			self.__array[self.__lastindex + 1] = None
			return temp
		else:
			raise IndexError("The array is empty.")

	def reverse(self):
		reversed___array = __array(int, self.__size)
		for index in range(self.__size - 1, -1, -1):
			reversed___array.add(self.__array[index])
		return reversed___array
		

	def __is_empty__(self):
		'''
		This method returns a boolean indicating if the __array is currently empty
		time-complexity = O(1) [simple comparison]
		'''
		return self.__lastindex + 1 == 0

	def __is_full__(self):
		'''
		This method returns a boolean indicating if the __array is currently full
		time-complexity = O(1) [simple comparison]
		'''
		return self.__lastindex + 1 == self.__size

	def __shift_right__(self, start_index):
		'''
		This method shifts all elements to the right starting from a specific index
		returns nothing
		time-complexity = O(n)
		'''
		for index in range(self.__size - 2, start_index - 1, -1):
			self.__array[index + 1] = self.__array[index]

		self.__lastindex += 1

	def __shift_left__(self, start_index):
		'''
		This method shifts all elements to the left starting from a specific index
		returns nothing
		time-complexity = O(n)
		'''
		for index in range(start_index + 1, self.__size):
			self.__array[index - 1] = self.__array[index]
			
		self.__lastindex -= 1
		self.__array[self.__lastindex + 1] = None