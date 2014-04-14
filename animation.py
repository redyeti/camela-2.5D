from collections import Iterator
from priorityQueue import PriorityQueue

class Animation(Iterator):
	def __init__(self, app, length, fps):
		self.__events = PriorityQueue()

	def __next__(self):
		event = self.__events.pop().payload


		frame = 

		time = 

		return (frame, time)
