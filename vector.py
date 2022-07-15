from array_implementation import Array
from math import sqrt, pow, pi, acos

class Vector(Array):
	"""
	"""
	def __init__(self, x=0, y=0, z=0):
		super().__init__(int, 3)
		for coordinate in [x, y, z]:
			self.append(coordinate)

		self.x, self.y, self.z = self
		
	def __repr__(self):
		return "Vector({}, {}, {})".format(self.x, self.y, self.z)

	def norm(self):
		return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

	def cross(self, other):
		mul_x = self.y * other.z - self.z * other.y
		mul_y = self.z * other.x - self.x * other.z
		mul_z = self.x * other.y - self.y * other.x

		return Vector(mul_x, mul_y, mul_z)

	def dot(self, other):
		mul_x = self.x * other.x
		mul_y = self.y * other.y
		mul_z = self.z * other.z

		return mul_x + mul_y + mul_z

	def angle_between(self, other):
		return 180 * acos((self.dot(other)) / (self.norm() * other.norm())) / pi