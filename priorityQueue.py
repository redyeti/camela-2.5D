import heapq
from collections import Sequence

class PriorityQueue(Sequence):
	def __init__(self, init=None):
		if init is None:
			self.__h = []
		else:
			self.__h = init
			heapq.heapify(self.__h)

	def push(self, i):
		heapq.heappush(self.__h, i)

	def pop(self):
		return heapq.heappop(self.__h)

	def replace(self, i):
		return heapq.heapreplace(self.__h, i)

	def union(self, other):
		return PriorityQueue(heapq.merge(self.__h, other.__h))

	def __getitem__(self, k):
		return self.__h[k]

	def __len__(self, k):
		return len(self.__h)

	def __str__(self):
		return "PriorityQueue(%s)" % repr(self.__h)

	__repr__ = __str__
