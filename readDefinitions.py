from application import Application
from configItem import ConfigItem

def readDefinitions(filename):
	events = []
	def event(fn):
		events.append(fn)
		return fn

	l = {
		'animation': ConfigItem(),
		'camera': ConfigItem(),
		'canvas': ConfigItem(),
		'extern': ConfigItem(),
		'output': ConfigItem(),
		'event': event,
	}
	execfile(filename, dict(), l)

	app = Application(
		animation = l['animation'],
		camera = l['camera'],
		canvas = l['canvas'],
		extern = l['extern'],
		output = l['output'],
	)
	
	for e in events:
		app.animation.addEvent(e)

	return app
