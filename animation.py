from __future__ import division
from collections import Iterator
from priorityQueue import PriorityQueue

class Animation(Iterator):
	def __init__(self, app, length, fps, synchronous):
		self.__app = app
		self.__events = PriorityQueue()
		self.__spf = 1/fps # seconds per frame
		self.__frame = 0
		self.__frameTime = -self.__spf
		self.__length = length
		self.__synchronous = synchronous


	def __dequeue(self):
		# increase frame data
		try:
			time, event = self.__events.pop()
		except IndexError:
			print "No events left."
			raise StopIteration

		if time < self.__frameTime:
			raise Exception("Cannot go back in time: %s requested %s after %s." % (repr(event.__name__), time, self.__frameTime))
		return (time, event)
		
	def __updateQueue(self, event):
		# update the queue
		try:
			t = event.next()
			self.__events.push((self.__sync(t), event))
		except StopIteration:
			pass

	def next(self):
		if self.__frameTime > self.__length:
			print "Reached end time."
			raise StopIteration

		if self.__frameTime == -self.__spf:
			time = 0
			event = iter(())
		else:
			time, event = self.__dequeue()

		if time == self.__frameTime:
			raise Exception("Double Frame: %s requested %s again." % (repr(event.__name__), time))

		self.__frame += 1
		self.__frameTime = time
		self.__updateQueue(event)

		while self.__events and self.__events[0][0] < self.nextTime:
			time, event = self.__dequeue()
			self.__updateQueue(event)


		return (self.__frame, time)

	def __sync(self, time):
		if self.__synchronous:
			return time - (time % self.__spf)
		else:
			return time

	def addEvent(self, eventFn):
		generator = eventFn(self, self.__app.camera, self.__app.canvas)
		time = generator.next()
	
		event = (self.__sync(time), generator)

		self.__events.push(event)

	@property
	def nextTime(self):
		return self.__frameTime + self.__spf

	@property
	def time(self):
		return self.__frameTime
