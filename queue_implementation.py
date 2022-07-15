from array_implementation import Array

class Queue(Array):
	"""
	"""
	
	def __init__(self, data_type, size):
		self.__queue = Array(data_type, size)
		self.__head = 0
		self.__tail = 0

	def __repr__(self):
		return "Queue: {}".format(self.__queue[:])

	def enqueue(self, data):
		if not self.isFull():
			self.__queue.insert(0, data)
			self.__head += 1
		else:
			raise IndexError("queue is full")

	def dequeue(self):
		if not self.isEmpty():
			self.__head -= 1
			return self.__queue.pop()
		else:
			raise IndexError("queue is empty")

	def isFull(self):
		return self.__head - self.__tail == len(self.__queue)

	def isEmpty(self):
		return self.__head == self.__tail
