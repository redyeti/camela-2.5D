from __future__ import division
from collections import Iterator
from priorityQueue import PriorityQueue

class Animation(Iterator):
	def __init__(self, app, length, fps):
		self.__app = app
		self.__events = PriorityQueue()
		self.__fps = fps
		self.__frame = 0

	def __next__(self):
		# increase frame data
		time, event = self.__events.pop()
		self.__frame += 1

		# update the queue
		if event.maker is not None:
			try:
				e = event.maker.next()
				self.__events.push(e)
			if StopIteration:
				pass

		return (self.__frame, time)

	def addEvent(self, eventFn):
		generator = eventFn(self, self.__app.camera, self.__app.canvas)
		time = generator.next()
		
		self.__events.push(e
