# Names:	Fikernew Birhanu	Yohannes Bekele
# IDs:		UGR/9932/13			UGR/3361/13


from array_implementation import Array

class Stack:
	"""
	"""

	def __init__(self, data_type, size):
		self.__stack = Array(data_type, size)
		self.__top_index = -1

	def __repr__(self):
		return "Stack Object : top item = {}.".format(self.s_peek())

	def Length(self):
		return len(self.__stack)

	def isEmpty(self):
		return self.__top_index == -1

	def s_push(self, key):
		if not self.isFull():
			try:
				self.__stack.add(key)
				self.__top_index += 1
			except:
				raise ValueError("incorrect value")
		else:
			raise IndexError("Stack overflow")

	def s_pop(self):
		try:
			temp = self.__stack[self.__top_index]
			self.__top_index -= 1
			self.__stack.pop()
			return temp
			
		except:
			raise IndexError("StackEmptyError: stack has not been populated")

	def s_peek(self):
		return self.__stack[self.__top_index]

	def isFull(self):
		return self.__top_index == len(self.__stack) - 1