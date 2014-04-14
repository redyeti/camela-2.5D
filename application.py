from storageItem import StorageItem
from animation import Animation
from canvas import Canvas
from camera import Camera
from extern import Extern
from output import Output

class Application(object):
	def __init__(self, animation, canvas, camera, schedule, extern, output):
		self.animation = Animation(self, **animation)
		self.canvas = Canvas(self, **canvas)
		self.camera = Camera(self, **camera)
		self.extern = Extern(self, **extern)
		self.output = Output(self, **output)
		self.schedule = schedule

	def run(self):
		for frame, time in self.animation:
			self.schedule(time, frame, self.camera, self.canvas, data=StorageItem())
			image = self.canvas.render(frame)
			self.output.store(frame, image)
		self.output.save()
