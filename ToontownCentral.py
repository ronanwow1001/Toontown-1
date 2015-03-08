import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *
from direct.actor.Actor import Actor
from AudioManager import TTCMusic
from TeleportButtons import *


class TTC(DirectObject):
	
	def __init__(self):
		self.createTTC()
		self.createSky()
		taskMgr.doMethodLater(10, self.debugTask, "Debug Task")
		TTCMusic()
		
	def debugTask(self, task):
		print(taskMgr)
		return task.again
		
	def createSky(self):
		self.sky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
		self.sky.reparentTo(render)
		self.sky.setTransparency(TransparencyAttrib.MDual, 1)
		
	def createTTC(self):
		self.TTC = loader.loadModel('phase_15/hood/toontown_central.bam')
		self.TTC.reparentTo(render)
		self.TTC.find('**/toontown_central').setTransparency(TransparencyAttrib.MBinary, 1)


TTC = TTC()
run()
