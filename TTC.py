import direct.directbase.DirectStart
from panda3d.core import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import *
from pandac.PandaModules import *
from direct.gui.OnscreenText import *
import sys
import random
from LocalAvatar import localAvatar 


font = loader.loadFont('phase_3/models/fonts/ImpressBT.ttf')

class TTC(DirectObject):
	global font
	def __init__(self): #__init__ tells the file to load everything. Basically load settings and put commands in here.
		self.currentworld = ""
		
		self.title = OnscreenText( text = '', mayChange = True, fg = (0, 0, 0, 1), pos = (.8, -.95), scale = .07, font = font, align = TextNode.ACenter )
		self.thememusic = loader.loadSfx('phase_4/audio/bgm/TC_nbrhood.mid')
		self.thememusic.play()
		self.thememusic.setVolume(.1)
		self.thememusic.setLoop(True)
		self.startWorld() #executes the "loadTerrain" command found below
		
		self.accept("escape", self.askExit)
		self.accept("s", self.muteAudio)
		self.accept("e", self.enableAudio)
		self.accept("l", self.loadingScreen)
		
	def loadingScreen(self):
		from ToontownLoadingScreen import app
		app.begin()
	def startWorld(self):
		self.terrain = loader.loadModel('phase_15/hood/toontown_central.bam')
		self.terrain.reparentTo(render)
		self.terrain.find('**/toontown_central').setTransparency(TransparencyAttrib.MBinary, 1)
		self.title.setText("Toontown Central")
		
		self.sky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
		self.sky.reparentTo(render)
		self.sky.setTransparency(TransparencyAttrib.MDual, 1)
	
		self.currentworld = "TTC"
		if self.currentworld == "TTC":
			self.acceptOnce("d", self.loadDock)
			self.acceptOnce("m", self.loadMelody)
			self.acceptOnce("g", self.loadGarden)
			self.acceptOnce("b", self.loadCold)
			self.acceptOnce("l", self.loadDream)
		self.startPos()	
	def loadTTC(self): #command that defines loading terrain
		self.thememusic.stop()
		self.thememusic = loader.loadSfx('phase_4/audio/bgm/TC_nbrhood.mid')
		self.thememusic.play()
		self.thememusic.setVolume(.1)
		self.thememusic.setLoop(True)
		
		self.terrain.removeNode()
		#self.terrain = loader.unloadModel('phase_15/hood/donalds_dock.bam')
		self.terrain = loader.loadModel('phase_15/hood/toontown_central.bam')
		self.terrain.reparentTo(render)
		self.terrain.find('**/toontown_central').setTransparency(TransparencyAttrib.MBinary, 1)
		self.title.setText("Toontown Central")
		
		self.sky.removeNode()
		#self.sky = loader.unloadModel('phase_3.5/models/props/BR_sky.bam')
		self.sky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
		self.sky.reparentTo(render)
		self.sky.setTransparency(TransparencyAttrib.MDual, 1)
	
		self.currentworld = "TTC"
		if self.currentworld == "TTC":
			self.acceptOnce("d", self.loadDock)
			self.acceptOnce("m", self.loadMelody)
			self.acceptOnce("g", self.loadGarden)
			self.acceptOnce("b", self.loadCold)
			self.acceptOnce("l", self.loadDream)
		self.startPos()	
	def askExit(self):
		self.msgbox = loader.loadModel('phase_3/models/gui/dialog_box_gui.bam')
		self.msgbox.reparentTo(base.a2dBottomCenter)
		self.msgbox.setPos(0, 0, 1)
		buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui.bam')
		OKButtonUP = buttons.find('**/ChtBx_OKBtn_UP')
		OKButtonRLVR = buttons.find('**/ChtBx_OKBtn_Rllvr')
		OKButtonDN = buttons.find('**/ChtBx_OKBtn_DN')
		CloseUP = buttons.find('**/CloseBtn_UP')
		CloseRLVR = buttons.find('**/CloseBtn_Rllvr')
		CloseDN = buttons.find('**/CloseBtn_DN')
		self.OkButton = DirectButton(image = (OKButtonUP, OKButtonDN, OKButtonRLVR), command = self.exitGame, pos = (-.3, 0, -.4), relief = None)
		self.OkButton.reparentTo(self.msgbox)
		self.OkButton.show() 
		self.CloseButton = DirectButton(image = (CloseUP, CloseDN, CloseRLVR), command = self.closeAsk, pos = (.3, 0, -.4), relief = None)
		self.CloseButton.reparentTo(self.msgbox)
		self.CloseButton.show()
		self.exittitle = OnscreenText( text = 'Are you sure you want to leave?', mayChange = False, fg = (0, 0, 0, 1), pos = (0, 0), scale = .07, font = font, align = TextNode.ACenter )
		self.exittitle.reparentTo(self.msgbox)	
		self.msgbox.show()
		
	def closeAsk(self):
		self.msgbox.removeNode()
		self.CloseButton.removeNode()
		self.OkButton.removeNode()
		self.exittitle.removeNode()
			
		
	def exitGame(self):
		sys.exit()
	def enableAudio(self):
		base.enableAllAudio()
		
	def muteAudio(self):
		base.disableAllAudio()
		
	def loadDock(self):
		self.thememusic.stop()
		self.thememusic = loader.loadSfx('phase_6/audio/bgm/DD_nbrhood.mid')
		self.thememusic.play()
		self.thememusic.setVolume(.1)
		self.thememusic.setLoop(True)
	
		self.terrain.removeNode()
		#self.terrain = loader.unloadModel('phase_15/hood/toontown_central.bam')
		self.terrain = loader.loadModel('phase_15/hood/donalds_dock.bam')
		self.terrain.reparentTo(render)
		self.terrain.find('**/donalds_dock').setTransparency(TransparencyAttrib.MBinary, 1)
		self.title.setText('Donald\'s Dock')
		
		self.sky.removeNode()
		#self.sky = loader.unloadModel('phase_3.5/models/props/TT_sky.bam')
		self.sky = loader.loadModel('phase_3.5/models/props/BR_sky.bam')
		self.sky.reparentTo(render)
		self.sky.setTransparency(TransparencyAttrib.MDual, 1)
		
		self.currentworld = "Donald\'s Dock"
		if self.currentworld == "Donald\'s Dock":
			self.acceptOnce("t", self.loadTTC)
			self.acceptOnce("m", self.loadMelody)
			self.acceptOnce("g", self.loadGarden)
			self.acceptOnce("b", self.loadCold)
			self.acceptOnce("l", self.loadDream)
		self.startPos()
	def loadMelody(self):
		self.thememusic.stop()
		self.thememusic = loader.loadSfx('phase_6/audio/bgm/MM_nbrhood.mid')
		self.thememusic.play()
		self.thememusic.setVolume(.1)
		self.thememusic.setLoop(True)
		
		self.terrain.removeNode()
		self.terrain = loader.loadModel('phase_15/hood/minnies_melody_land.bam')
		self.terrain.reparentTo(render)
		#self.terrain.find('**/minnies_melody_land').setTransparency(TransparencyAttrib.MBinary, 1)
		self.title.setText('Minnie\'s Melodyland')

		self.sky.removeNode()
		#self.sky = loader.unloadModel('phase_3.5/models/props/TT_sky.bam')
		self.sky = loader.loadModel('phase_6/models/props/MM_sky.bam')
		self.sky.reparentTo(render)
		self.sky.setTransparency(TransparencyAttrib.MDual, 1)
		
		self.currentworld = "Melody"
		if self.currentworld == "Melody":
			self.acceptOnce("t", self.loadTTC)
			self.acceptOnce("d", self.loadDock)
			self.acceptOnce("g", self.loadGarden)
			self.acceptOnce("b", self.loadCold)
			self.acceptOnce("l", self.loadDream)
	def loadGarden(self):
		self.thememusic.stop()
		self.thememusic = loader.loadSfx('phase_8/audio/bgm/DG_nbrhood.mid')
		self.thememusic.play()
		self.thememusic.setVolume(.1)
		self.thememusic.setLoop(True)
		
		self.terrain.removeNode()
		self.terrain = loader.loadModel('phase_15/hood/daisys_garden.bam')
		self.terrain.reparentTo(render)
		#self.terrain.find('**/daisys_garden').setTransparency(TransparencyAttrib.MBinary, 1)
		self.title.setText('Daisy Gardens')

		self.sky.removeNode()
		#self.sky = loader.unloadModel('phase_3.5/models/props/TT_sky.bam')
		self.sky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
		self.sky.reparentTo(render)
		self.sky.setTransparency(TransparencyAttrib.MDual, 1)
		
		self.currentworld = "Garden"
		if self.currentworld == "Garden":
			self.acceptOnce("t", self.loadTTC)
			self.acceptOnce("d", self.loadDock)
			self.acceptOnce("m", self.loadMelody)
			self.acceptOnce("b", self.loadCold)
			self.acceptOnce("l", self.loadDream)
	def loadCold(self):
		self.thememusic.stop()
		self.thememusic = loader.loadSfx('phase_8/audio/bgm/TB_nbrhood.mid')
		self.thememusic.play()
		self.thememusic.setVolume(.1)
		self.thememusic.setLoop(True)
		
		self.terrain.removeNode()
		self.terrain = loader.loadModel('phase_15/hood/the_burrrgh.bam')
		self.terrain.reparentTo(render)
		#self.terrain.find('**/').setTransparency(TransparencyAttrib.MBinary, 1)
		self.title.setText('The Brrrgh')

		self.sky.removeNode()
		#self.sky = loader.unloadModel('phase_3.5/models/props/TT_sky.bam')
		self.sky = loader.loadModel('phase_3.5/models/props/BR_sky.bam')
		self.sky.reparentTo(render)
		self.sky.setTransparency(TransparencyAttrib.MDual, 1)
		
		self.currentworld = "Cold"
		if self.currentworld == "Cold":
			self.acceptOnce("t", self.loadTTC)
			self.acceptOnce("d", self.loadDock)
			self.acceptOnce("m", self.loadMelody)
			self.acceptOnce("b", self.loadCold)
			self.acceptOnce("l", self.loadDream)
	def loadDream(self):
		self.thememusic.stop()
		self.thememusic = loader.loadSfx('phase_8/audio/bgm/DL_nbrhood.mid')
		self.thememusic.play()
		self.thememusic.setVolume(.1)
		self.thememusic.setLoop(True)
		
		self.terrain.removeNode()
		self.terrain = loader.loadModel('phase_15/hood/donalds_dreamland.bam')
		self.terrain.reparentTo(render)
		#self.terrain.find('**/').setTransparency(TransparencyAttrib.MBinary, 1)
		self.title.setText('Donald\'s Dreamland')

		self.sky.removeNode()
		#self.sky = loader.unloadModel('phase_3.5/models/props/TT_sky.bam')
		self.sky = loader.loadModel('phase_8/models/props/DL_sky.bam')
		self.sky.reparentTo(render)
		self.sky.setTransparency(TransparencyAttrib.MDual, 1)
		
		self.currentworld = "Cold"
		if self.currentworld == "Cold":
			self.acceptOnce("t", self.loadTTC)
			self.acceptOnce("d", self.loadDock)
			self.acceptOnce("m", self.loadMelody)
			self.acceptOnce("b", self.loadCold)
			self.acceptOnce("l", self.loadDream)
			
	def startPos(self):
			startPos = random.choice([1, 2, 3])
			if startPos == 1:
				if self.currentworld == 'TTC':
					startPosi = (-75.955, 82.0341, .025)
					startHpr = (206.686, 0, 0)
					print "Start 1 TTC"
				if self.currentworld == "Donald\'s Dock":
					startPosi = (-62.072, -82.4714, 5.69199)
					startHpr = (-22.9025, 0, 0)
					print "Start 1 Dock"
			if startPos == 2: 
				if self.currentworld == 'TTC':
					startPosi = (30.3073, -43.9795, 4.02455)
					startHpr = (16.1418, 0, 0)
					print "Start 2 TTC"
				if self.currentworld == "Donald\'s Dock":
					startPosi = (70.3026, -17.3636, 5.69199)
					startHpr = (88.1163, 0, 0)
					print "Start 2 Dock"
			if startPos == 3: 
				if self.currentworld == 'TTC':
					startPosi = (-105.675, -84.7621, -.525)
					startHpr = (-21.327, 0, 0)
					print "Start 3 TTC"
				if self.currentworld == "Donald\'s Dock":
					startPosi = (53.0884, 99.52, 3.28025)
					startHpr = (141.021, 0, 0)
					print "Start 3 Dock"
			localAvatar.setPos(startPosi)
			localAvatar.setHpr(startHpr)

		
		
		
TTC = TTC()
