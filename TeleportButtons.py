from direct.gui.DirectGui import *
from ToontownCentral import *

class TeleportButtons:
	
	def __init__(self):
		self.createButtons()
		
	def createButtons(self):
		button = loader.loadModel('phase_3/models/gui/quit_button.bam')
		down = button.find('**/QuitBtn_DN')
		rollover = button.find('**/QuitBtn_RLVR')
		up = button.find('**/QuitBtn_UP')
		ButtonClick = loader.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.mp3')
		ButtonRollover = loader.loadSfx('phase_3/audio/sfx/GUI_rollover.mp3')
		ImpressBT = loader.loadFont('phase_3/models/fonts/ImpressBT.ttf')
		
		ttc = DirectButton(image = (up, rollover, down), relief = None, command = TTC.createTTC(), pressEffect = 0, clickSound = (ButtonClick), rolloverSound = (ButtonRollover), text = "Toontown Central", text_scale = .04, text_font = ImpressBT, enableEdit = True)
		#ttc["state"] = DGG.DISABLED
		ttc["state"] = DGG.NORMAL
		ttc.show()
		
		self.dd = DirectButton(image = (up, rollover, down), relief = None, pressEffect = 0, clickSound = (ButtonClick), rolloverSound = (ButtonRollover), text = "Donald's Dock", text_scale = .04, text_font = ImpressBT)
		#dd["state"] = DGG.DISABLED
		self.dd["state"] = DGG.NORMAL
		self.dd.show()
		self.dd.setPos(1, 0, 0)
		
		
		

