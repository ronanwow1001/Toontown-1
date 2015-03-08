

class TTCMusic:
	
	def __init__(self):
		self.TTCplaygroundmusic = loader.loadSfx('phase_4/audio/bgm/TC_nbrhood.mp3')
		self.playTTCMusic()
		#if self.TTCplaygroundmusic.status() == self.TTCplaygroundmusic.PLAYING:
			#print "Works"
	
	def playTTCMusic(self):
		self.TTCplaygroundmusic.play()
		self.TTCplaygroundmusic.setLoop(True)
		
	def stopTTCMusic(self):
		self.TTCplaygroundmusic.stop()
		self.TTCplaygroundmusic.setLoop(False)
		
class DDMusic:
	
	def __init__(self):
		self.DDplaygroundmusic = loader.loadSfx('phase_6/audio/bgm/DD_nbrhood.mp3')
		self.playDDMusic()
		
	def playDDMusic(self):	
		self.DDplaygroundmusic.play()
		self.DDplaygroundmusic.setLoop(True)
		
	def stopDDMusic(self):
		self.DDplaygroundmusic.stop()
		self.DDplaygroundmusic.setLoop(False)

class MMMusic:

	def __init__(self):
		self.MMplaygroundmusic = loader.loadSfx('phase_6/audio/bgm/MM_nbrhood.mp3')
		self.playMMMusic()
		
	def playMMMusic(self):	
		self.MMplaygroundmusic.play()
		self.MMplaygroundmusic.setLoop(True)
		
	def stopMMMusic(self):
		self.MMplaygroundmusic.stop()
		self.MMplaygroundmusic.setLoop(False)
		
class AAMusic:
	
	def __init__(self):
		self.AAplaygroundmusic = loader.loadSfx('phase_6/audio/bgm/AA_nbrhood.mp3')
		self.playAAMusic()
		
	def playAAMusic():
		self.AAplaygroundmusic.play()
		self.AAplaygroundmusic.setLoop(True)
		
	def stopAAMusic():
		self.AAplaygroundmusic.stop()
		self.AAplaygroundmusic.setLoop(False)
		
class GSMusic:
	
	def __init__(self):
		self.GSplaygroundmusic = loader.loadSfx('phase_6/audio/bgm/GS_SZ.mp3')
		self.playGSMusic()

	def playGSMusic():
		self.GSplaygroundmusic.play()
		self.GSplaygroundmusic.setLoop(True)
		
	def stopAAMusic():
		self.GSplaygroundmusic.stop()
		self.GSplaygroundmusic.setLoop(False)
		
class GZMusic:
	
	def __init__(self):
		self.GZplaygroundmusic = loader.loadSfx('phase_6/audio/bgm/GZ_SZ.mp3')
		self.playGZMusic()
		
	def playGZMusic():
		self.GZplaygroundmusic.play()
		self.GZplaygroundmusic.setLoop(True)
		
	def stopGZMusic():
		self.GZplaygroundmusic.stop()
		self.GZplaygroundmusic.setLoop(False)
		
class DGMusic:
	
	def __init__(self):
		self.DGplaygroundmusic = loader.loadSfx('phase_8/audio/bgm/DG_nbrhood.mp3')
		self.playDGMusic()
		
	def playDGMusic():
		self.DGplaygroundmusic.play()
		self.DGplaygroundmusic.setLoop(True)
		
	def stopDGMusic():
		self.DGplaygroundmusic.stop()
		self.DGplaygroundmusic.setLoop(False)
		
class DLMusic:
	
	def __init__(self):
		self.DLplaygroundmusic = loader.loadSfx('phase_8/audio/bgm/DL_nbrhood.mp3')
		self.playDLMusic()
		
	def playDLMusic():
		self.DLplaygroundmusic.play()
		self.DLplaygroundmusic.setLoop(True)
		
	def stopDLMusic():
		self.DLplaygroundmusic.stop()
		self.DLplaygroundmusic.setLoop(False)
		
class BRMusic:
	
	def __init__(self):
		self.BRplaygroundmusic = loader.loadSfx('phase_8/audio/bgm/TB_nbrhood.mp3')
		self.playBRMusic()
		
	def playBRMusic():
		self.BRplaygroundmusic.play()
		self.BRplaygroundmusic.setLoop(True)
		
	def stopBRMusic():
		self.BRplaygroundmusic.stop()
		self.BRplaygroundmusic.setLoop(False)
