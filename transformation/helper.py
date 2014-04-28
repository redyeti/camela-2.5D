from __future__ import division
import numpy as np
from math import atan, pi

def angle(matrix):
	t = atan(matrix[1,0]/matrix[1,1])
	if matrix[0,0] < 0:
		t += pi
	return t

class Translation(np.matrix):
	@property
	def x(self):
		return float(self[0,2])

	@property
	def y(self):
		return float(self[1,2])


class Rotation(np.matrix):
	@property
	def beta(self):
		if self[1,1] == 0:
			return 180
		else:
			t = angle(self)
			return t * 180 / pi
	

class Scale(np.matrix):
	@property
	def sx(self):
		return self[0,0]

	@property
	def sy(self):
		return self[1,1]

