from collections import MutableMapping
from abc import abstractproperty
INF = float("infinity")

class Canvas(MutableMapping):
	def __init__(self, app, primarySource, elements):
		self.__drawingElements = elements

	def __getitem__(self, k):
		return self.__drawingElements[k]

	def __setitem__(sekf, k, v):
		self.__drawingElements[k] = v

	def __delitem__(self, k):
		del self.__drawingElements[k]

	def __len__(self):
		return len(self.__drawingElements)

	def __iter__(self):
		return len(self.__drawingElements)
