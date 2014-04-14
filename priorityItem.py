from collections import Sequence

class PriorityItem(Sequence):
	def __init__(self, priority, payload):
		self.__priority = priority
		self.payload = payload

	def __float__(self):
		return self.__priority

	def __str__(self):
		return "<%.2f, %s>" % (self.__priority, repr(self.payload))

	__repr__ = __str__

	def __getitem__(self, i):
		if i == 0:
			return self.__priority
		else:
			return self.payload

	def __len__(self):
		return 2

	@property
	def priority(self):
		return self.__priority
