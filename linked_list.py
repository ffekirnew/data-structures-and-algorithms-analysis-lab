class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def __repr__(self):
		return "{} -> [{}]".format(self.data, self.next)

	def getData(self):
		return self.data

	def setData(self, new_data):
		self.data = new_data

	def getNext(self):
		return self.next

	def setNext(self, key):
		self.next = key


class SLL:
	"""docstring for SLL"""
	def __init__(self):
		self.head = Node(None)

	def __repr__(self):
		return "SLL object at {}".format(self.head)

	def PushFront(self, key):
		'''
		O(1)
		'''
		temp = Node(key)
		temp.next = self.head.next
		self.head.next = temp

	def TopFront(self):
		'''
		O(1)
		'''
		return self.head.next

	def PopFront(self):
		'''
		O(1)
		'''
		front_element = self.head.next
		self.head.next = self.head.next.next

		return front_element.data

	def PushBack(self, key):
		'''
		O(n)
		'''
		current_node = self.head
		while current_node.next != None:
			current_node = current_node.next

		current_node.next = Node(key)

	def TopBack(self):
		'''
		O(n)
		'''
		current_node = self.head
		while current_node.next != None:
			current_node = current_node.next

		return current_node

	def PopBack(self):
		'''
		O(n)
		'''
		current_node = self.head
		while current_node.next != None:
			current_node = current_node.next

		last_element = current_node
		current_node = None

		return last_element.data

	def Find(self, key):
		'''
		O(n)
		'''
		current_node = self.head
		found = False
		while not found and current_node.next != None:
			if current_node.data == key:
				found = True
			else:
				current_node = current_node.next

		return current_node.data == key

	def Erase(self, key):
		'''
		O(n)
		'''
		previous_node = None
		current_node = self.head
		found = False
		while not found and current_node.next != None:
			if current_node.data == key:
				found = True
			else:
				previous_node = current_node
				current_node = current_node.next

		if current_node.data == key:
			previous_node.next = current_node.next
			return current_node.data

	def Empty(self):
		'''
		O(1)
		'''
		return self.head.next == None

	def AddBefore(self, key, new_data):
		'''
		O(n)
		'''
		previous_node = None
		current_node = self.head
		found = False
		while not found and current_node.next != None:
			if current_node.data == key:
				found = True
			else:
				previous_node = current_node
				current_node = current_node.next

		if current_node.data == key:
			temp = Node(new_data)
			temp.next = current_node
			previous_node.next = temp