from storageItem import StorageItem
from animation import Animation
from canvas import Canvas
from camera import Camera
from extern import Extern
from output import Output
import os

class Application(object):
	def __init__(self, animation, canvas, camera, extern, output):
		self.animation = Animation(self, **animation)
		self.canvas = Canvas(self, **canvas)
		self.camera = Camera(self, **camera)
		self.extern = Extern(self, **extern)
		self.output = Output(self, **output)

	@property
	def rootPath(self):
		return os.path.dirname(self.canvas.primarySource)

	def run(self):
		for frame, time in self.animation:
			print "Frame %4i, %4.2fs" % (frame, time)
			image = self.canvas.render(frame)
			self.output.store(frame, image)
		#self.output.save()
