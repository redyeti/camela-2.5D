from application import Application
from configItem import ConfigItem

def readDefinitions(filename):
	localsdict = {
		'animation': ConfigItem(),
		'camera': ConfigItem(),
		'canvas': ConfigItem(),
		'extern': ConfigItem(),
		'output': ConfigItem(),
	}
	execfile(filename, dict(), localsdict)

	return Application(**localsdict)
