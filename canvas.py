from collections import MutableMapping
from drawingElement import DrawingElement
from sourceLoader import SourceLoader
from abc import abstractproperty
INF = float("infinity")

class Canvas(MutableMapping):
	def __init__(self, app, primarySource, elements):
		self.__app = app
		self.__loader = SourceLoader(app, primarySource)
		self.__drawingElements = {}
		for k,v in elements.iteritems():
			self[k] = v

	def __getitem__(self, k):
		return self.__drawingElements[k]

	def __setitem__(self, k, v):
		if not isinstance(v, DrawingElement):
			v = DrawingElement(self, k, **v)
		self.__drawingElements[k] = v

	def __delitem__(self, k):
		del self.__drawingElements[k]

	def __len__(self):
		return len(self.__drawingElements)

	def __iter__(self):
		return iter(self.__drawingElements)

	def loadSvgNode(self, id):
		return self.__loader.load(id)

	@property
	def app(self):
		return self.__app

	def render(self, frame):
		for element in self.values():
			element.updateNode(self.app.camera)	
		return self.__loader.primaryTree
