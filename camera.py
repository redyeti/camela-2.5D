from math import atan
import numpy as np

class Camera(object):
	def __init__(self, app, focalLength, position):

		# Format factor 1, but 4:3
		self.__hAngle = 2 * atan(36/2/focalLength)
		self.__vAngle = 2 * atan(27/2/focalLength)

	@property
	def matrix(self):
		#FIXME: for now ...
		return np.identity(3)
