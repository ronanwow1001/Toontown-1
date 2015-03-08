import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject

class World(DirectObject):
	def __init__(self):
		#base.setBackgroundColor(0, 0, 0)
		self.terrain = loader.loadModel('phase_15/hood/toontown_central.bam')    	# loads in the terrain
		self.terrain.reparentTo(render)												# sets it in game
		self.statue = loader.loadModel('phase_4/models/props/goofy_statue.bam') 	# loads in a model
		self.statue.reparentTo(render)												# sets it in game
		self.keyMap = {"w" : False,													# creates keymap allowing key input
				"s" : False,
				"a" : False,
				"d" : False}
		taskMgr.add(self.statueControl, "Statue Control")							# adds statueControl to task manager
		taskMgr.doMethodLater(10, self.debugTask, "Debug Task")						# tells game to add Debug task to task manager after 10 seconds
		self.accept("w", self.setKey, ["w", True])									# defines the key inputs
		self.accept("s", self.setKey, ["s", True])
		self.accept("a", self.setKey, ["a", True])
		self.accept("d", self.setKey, ["d", True])
		self.accept("w-up", self.setKey, ["w", False])
		self.accept("s-up", self.setKey, ["s", False])
		self.accept("a-up", self.setKey, ["a", False])
		self.accept("d-up", self.setKey, ["d", False])
		
	def setKey(self, key, value):
		self.keyMap[key] = value
		
	def statueControl(self, task):
		dt = globalClock.getDt()
		if( dt > .20):
			return task.cont
		if(self.keyMap["w"] == True):												# up
			self.statue.setY(self.statue, 10 * dt)
		if(self.keyMap["s"] == True):												# down
			self.statue.setY(self.statue, -10 * dt)
		if(self.keyMap["a"] == True):												# left
			self.statue.setX(self.statue, -10 * dt)
		if(self.keyMap["d"] == True):												# right
			self.statue.setX(self.statue, 10 * dt)
		return task.cont
		
	def debugTask(self, task):
		print(taskMgr)
		taskMgr.removeTasksMatching("Statue Move *")
		return task.again
		
		
w = World()	
run()
