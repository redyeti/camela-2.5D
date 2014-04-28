from __future__ import division
import numpy as np
import re
from math import sqrt, cos, sin, atan, pi
from numpy.linalg import inv

from helper import Translation
from helper import Rotation
from helper import Scale
from helper import angle

class Transformation(np.matrix):
	re_transform = re.compile(r'([a-z-]+)\(([0-9.,\s-]+)\);?\s*')

	@property
	def scale(self):
		sx = sqrt(self[0,0]**2 + self[0,1]**2)
		sy = sqrt(self[1,0]**2 + self[1,1]**2)	
		return self.__class__.init([sx, 0, 0, 0, sy, 0]).view(Scale)

	@property
	def rotation(self):
		t = angle(self)
		s = sin(t)
		c = cos(t)

		#q = self[1,0]**2 / self[1,1]**2 + 1
		#s = self[1,0] / q**(self[1,1])
		#c = 1 / sqrt(q)
		
		return self.__class__.init([c, -s, 0, s, c, 0]).view(Rotation)

	def check(self):
		pass
		#if abs(sum((self - self.scalePart * self.rotationPart * self.translationPart).flat)) >= 0.1:
		#	print "INVALID!"

	@property
	def translationBefore(self):
		return (self * inv(self.rotation) * inv(self.scale)).view(Translation)

	@property
	def translationAfter(self):
		return (inv(self.rotation) * inv(self.scale) * self).view(Translation)

	@classmethod
	def init(cls, arr):
		return np.matrix(arr+[0,0,1]).reshape(3,3).view(cls)

	@classmethod
	def fromCss(cls, string):
		matrix = np.identity(3)

		for transform, data in cls.re_transform.findall(string):
			data = [float(x) for x in data.split(",")]
			m2 = cls.fromData(transform, data)
			matrix = matrix * m2
			matrix.check()

		return matrix

	@classmethod
	def fromData(cls, transform, data):
		if transform == "none":
			m2 = np.identity(3)
		elif transform == "translate":
			m2 = [1, 0, data[0], 0, 1, data[1]]
		elif transform == "rotate":
			r = data[0] / 180 * pi
			s = sin(r)
			c = cos(r)
			m2 = [c, -s, 0, +s, c, 0]
		elif transform == "scale":
			sx = data[0]
			if len(data) == 1:
				sy = sx
			else:
				sy = data[1]
			m2 = [sx, 0, 0, 0, sy, 0]
		elif transform == "matrix":
			m2 = [data[0], data[2], data[4], data[1], data[3], data[5]]
		else:
			raise ValueError("Unknown transformation type: "+transform)

		mr = cls.init(m2)
		return mr

	def toData(self):
		d = [self[0,0], self[1,0], self[0,1], self[1,1], self[0,2], self[1,2]]
		return ("matrix", d)

	def toCss(self):
		t, d = self.toData()
	
		dstring = ", ".join([("%1.12f" % x) for x in d])
		return "%s(%s)" % (t, dstring)
