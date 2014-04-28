#!/usr/bin/env python
#-*- coding: utf8 -*-
import argparse
import numpy as np

np.set_printoptions(suppress=True)


parser = argparse.ArgumentParser(description='Camela 2.5D')
parser.add_argument('--force','-f', action="store_true", help="Bestehende Dateien überschreiben")
parser.add_argument('infile', metavar='INFILE', help="Eingabedatei")
parser.add_argument('outfile', metavar='OUTFILE', nargs="?", help="Ausgabedatei. Falls nicht angegeben, so wird die Ausgabedatei automatisch bestimmt.")

args = parser.parse_args()

from readDefinitions import readDefinitions

application = readDefinitions(args.infile)
application.run()
