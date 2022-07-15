from array_implementation import Array

class Stack:
	"""
	"""

	def __init__(self, data_type, size):
		self.__stack = Array(data_type, size)
		self.__top_index = -1

	def __repr__(self):
		return "Stack Object : top item = {}.".format(self.top())

	def __len__(self):
		return len(self.__stack)

	def push(self, key):
		try:
			self.__stack.add(key)
			self.__top_index += 1
		except Exception as StackOverflow:
			print("StackOverflowError: stack is full")

	def pop(self):
		try:
			temp = self.__stack[self.__top_index]
			self.__top_index -= 1
			self.__stack.pop()
			return temp
			
		except Exception as StackEmpty:
			print("StackEmptyError: stack has not been populated")

	def top(self):
		return self.__stack[self.__top_index]

	def isEmpty(self):
		return self.__top_index == -1

	def isFull(self):
		return self.__top_index == len(self.__stack) - 1