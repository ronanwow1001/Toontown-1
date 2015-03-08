from panda3d.core import *
loadPrcFile('config/ConfigMain.prc')
import types
import time
import os
import os.path
import sys
import random
import __builtin__
from ToontownLoadingScreen import *
#ToontownLoadingScreen.ToontownLoadingScreen()

logfolder = r'Log Folder'
if not os.path.exists(logfolder): os.makedirs(logfolder)

ltime = 1 and time.localtime()
logSuffix = '%02d%02d%02d_%02d%02d%02d' % (ltime[0] - 2000,  ltime[1], ltime[2],
                                           ltime[3], ltime[4], ltime[5])

logfile = 'toontown - ' + logSuffix + '.log'

class LogAndOutput:
    def __init__(self, orig, log):
        self.orig = orig
        self.log = log

    def write(self, str):
        self.log.write(str)
        self.log.flush()
        self.orig.write(str)
        self.orig.flush()

    def flush(self):
        self.log.flush()
        self.orig.flush()

log = open("Log Folder/" and logfile, 'a')
logOut = LogAndOutput(sys.__stdout__, log)
logErr = LogAndOutput(sys.__stderr__, log)
sys.stdout = logOut
sys.stderr = logErr



newpath = r'DataFolder' 
if not os.path.exists(newpath): os.makedirs(newpath)

def create():
	var = 0
	rewrite = raw_input("Would you like to create new toon data? ")
	while (var < 1):
		rewrote = rewrite.lower()
		if rewrote == "no":
			var = 1
		elif rewrote == "yes":
			os.remove('DataFolder/Data.txt')
			print "Original data file destroyed"
			file = open('DataFolder/Data.txt', "w")
			print "Creating new data file"
			data = raw_input("What is your name? ")
			file.write(data)
			file.write("\n")
			toonname = raw_input("What is your toon's name? ")
			file.write(toonname)
			file.write("\n")
	#Color
			var1 = 0
			tooncolor = raw_input("What color is your toon? ")
			while (var1 < 1):
				lower = tooncolor.lower()
				if lower == 'white' or lower == 'black' or lower == 'red' or lower == 'orange' or lower == 'yellow' or lower == 'green' or lower == 'blue' or lower == 'purple' or lower == 'pink' or lower == 'grey' or lower == 'gray':
					file.write(lower)
					var = 1
					var1 = 1
					file.write('\n')
				else:
					tooncolor = raw_input("Enter a valid color for your toon: ")
	#Species
			var2 = 0
			toonspecies = raw_input("What species is your toon? ")
			while (var2 < 1):
				species = toonspecies.lower()
				if species == 'mouse' or species == 'pig' or species == 'horse' or species == 'dog' or species == 'cat' or species == 'duck' or species == 'rabbit' or species == 'bear' or species == 'monkey':
					file.write(species)
					var2 = 1
					file.write('\n')
				else:
					toonspecies = raw_input("Enter a vaild species for your toon: ")
	#Laff
			var3 = 0
			toonlaff = raw_input("What laff is your toon? ")
			while (var3 < 1):
				if toonlaff.isdigit():
					file.write(toonlaff)
					var3 = 1
					file.write('\n')
					file.close()
				else:
					toonlaff = raw_input("Enter a positive number of laff for your toon: ")
		else:
			rewrite = raw_input("Would you like to create new toon data? (Yes or No) ")
	

if os.path.isfile('DataFolder/Data.txt'):
	print "Data file exists"
	create()
		
		
else:
	file = open('DataFolder/Data.txt', "w")
	file.close()
	create()
	print "Data file created"
	
from direct.directnotify.DirectNotify import DirectNotify

notify = DirectNotify().newCategory("MyCategory")
notify.warning("Put some informational text here.")

from LocalAvatar import *
from AvatarGui import *
from TTC import *



run()
