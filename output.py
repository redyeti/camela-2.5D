from lxml import etree

class Output(object):
	def __init__(self, app, format):
		pass
		
	def store(self, frame, image):
		s = etree.tostring(image)
		with open("out/frame_%04i.svg" % frame, "w") as f:
			f.write(s)
