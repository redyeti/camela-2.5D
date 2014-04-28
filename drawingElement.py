from transformation import Transformation
from numpy.linalg import inv
import numpy as np

class DrawingElement(object):
	def __init__(self, canvas, id, distance=None, width=None, height=None, **params):
		self.__canvas = canvas
		self.__id = id
		self.__node = canvas.loadSvgNode(id)
		
		# first set distance 

		print id, self.__node
		if distance is not None:
			self.__distance = distance
		elif width is not None:
			Transformation.fromCss(self.__node.get("transform",""))
			raise Exception("NYI")
			#self.__distance = ...
		elif height is not None:
			Transformation.fromCss(self.__node.get("transform",""))
			raise Exception("NYI")
			#self.__distance = ...
		else:
			raise ValueError("At least one of distance, width or height must be set.")

		# get transformation data from xml node
		x = float(self.__node.get("x",0))
		y = float(self.__node.get("y",0))
		t1 = Transformation.fromCss(self.__node.get("transform",""))
		t2 = Transformation.fromData("translate", (x,y)) * t1

		#print "Before:", t2.translationBefore.x, t2.translationBefore.y
		#print "After :", t2.translationAfter.x, t2.translationAfter.y

		# apply local transformation data
		self.x = t2.translationAfter.x
		self.y = t2.translationAfter.y
		self.rotation = t2.rotation.beta

		self.scaleX = t2.scale.sx
		self.scaleY = t2.scale.sy

		print (self.x, self.y)

		#FIXME
		# set everything else
		# directly in the node


	def node(self):
		return self.__node

	def updateNode(self, camera):
		s = Transformation.fromData("scale", (self.scaleX, self.scaleY))

		#FIXME: WHY THE MINUS HERE?
		r = Transformation.fromData("rotate", (self.rotation,))
		t = Transformation.fromData("translate", (self.x, self.y))

		tb = t.translationBefore
		
		n = self.__node
		n.set('x', str(tb.x))
		n.set('y', str(tb.y))

		n.set('transform', (s*r).toCss())
