class Element(object):
	def __init__(self, canvas, node, distance=None, width=None, height=None):
		self.__node = node # xml data
		if distance is not None:
			self.distance = distance
		elif width is not None:
			self.width = width
		elif height is not None:
			self.height = height

	# internal base attributes:
	# - canvas.viewAngle
	# - self.distance
		
	# properties in m
	distance = abstractproperty()
	width = abstractproperty() # const
	height = abstractproperty() # const
	layerwidth = abstractproperty()
	layerheight = abstractproperty()
	x = abstractproperty()
	y = abstractproperty()

	# properties in px
	pixelwidth = abstractproperty()
	pixelheight = abstractproperty()

	# other properties
	
