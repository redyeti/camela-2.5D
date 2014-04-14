# -*- coding: utf8 -*-

# Externe Befehle. Exakten Pfad angeben, falls nicht in PATH,
# ansonsten ist der Befehlsname ausreichend. Sollte im Normalfall
# schon so stimmen.
extern.imageMagick = "convert"

# Primärquelle, also das Eingabebild
canvas.primarySource = "input.g.svg"

# Brennweite der Kamera in mm, mit der das Eingabebild
# aufgenommen worden wäre, wenn es den tatsächlich ein 
# Foto wäre. 50 ist Normalbrennweite, 300 ist Tele,
# 17 ist Weitwinkel. (INF bedeutet Orthonormalprojektion)
camera.focalLength = 50

# Position der Kamera (Standard ist schön in der 
# Bildmitte)
camera.position = (400, 300)

# Elemente mit ihren initialen Eigenschaften. 
# 'name' steht für ein Element der Primärquelle.
# 'datei:name' steht für ein Element aus anderer Quelle.
# Was hier nicht drinsteht, wird als unendlich weit entfernter
# Hintergrund behandelt.
canvas.elements = {
	'SomeId': {'distance': 5},
	'OtherId1': {'width': 10},
	'OtherId2': {'height': 8, 'visible': False},
}

# Setze die Dauer der Animation in Sekunden
animation.length = 10.0

# Setze die Anzahl an Frames pro Sekunde. 
animation.fps = 4

# Setze synchronisationsmodus
animation.synchronous = True

@event
def first(animation, camera, canvas):
	yield 0
	# do something at 0 sec
	

# Set the output format
output.format = "svg"
