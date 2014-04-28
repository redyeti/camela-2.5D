from lxml import etree
import os

class SourceLoader(object):

	def __init__(self, app, primarySource):
		self.__app = app
		self.__documents = {}
		self.__primarySource = primarySource
		self.__root = os.path.dirname(primarySource)

	@property
	def primaryTree(self):
		self.__load(self.__primarySource)
		return self.__documents[self.__primarySource]

	def load(self, k):
		if isinstance(k, tuple):
			doc, id = k
		else:
			doc = self.__primarySource
			id = k

		self.__load(doc)
		element = self.__documents[doc].xpath('//*[@id=%s]' % repr('element_'+id))
		if len(element):
			element = element[0]
		else:
			raise KeyError("Id not found: "+repr(id))
		
		if doc != self.__primarySource:
			self.primaryTree.xpath('/svg').append(element)

		return element

	def __load(self, doc):
		if doc not in self.__documents:
			path = os.path.join(self.__root, doc)
			svg = etree.parse(path)
			self.__documents[doc] = svg

