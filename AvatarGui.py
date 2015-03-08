import direct.directbase.DirectStart
from panda3d.core import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import *
from pandac.PandaModules import *
from direct.gui.OnscreenText import *
from TTC import font
from toon_color import *
import linecache

class GUI():
	global font
	def __init__(self):
		self.laffMeter()
		
	def laffMeter(self):
		self.head = linecache.getline('DataFolder/Data.txt', 4)
		if self.head == 'duck\n':		
			self.duckhead = loader.loadModel('phase_3/models/gui/laff_o_meter.bam').find('**/duckhead')
		if self.head == 'cat\n':		
			self.duckhead = loader.loadModel('phase_3/models/gui/laff_o_meter.bam').find('**/cathead')
		if self.head == 'monkey\n':		
			self.duckhead = loader.loadModel('phase_3/models/gui/laff_o_meter.bam').find('**/monkeyhead')
		if self.head == 'bear\n':		
			self.duckhead = loader.loadModel('phase_3/models/gui/laff_o_meter.bam').find('**/bearhead')
		if self.head == 'rabbit\n':		
			self.duckhead = loader.loadModel('phase_3/models/gui/laff_o_meter.bam').find('**/bunnyhead')
		if self.head == 'horse\n':		
			self.duckhead = loader.loadModel('phase_3/models/gui/laff_o_meter.bam').find('**/horsehead')
		if self.head == 'mouse\n':		
			self.duckhead = loader.loadModel('phase_3/models/gui/laff_o_meter.bam').find('**/mousehead')
		if self.head == 'pig\n':		
			self.duckhead = loader.loadModel('phase_3/models/gui/laff_o_meter.bam').find('**/pighead')
		if self.head == 'dog\n':		
			self.duckhead = loader.loadModel('phase_3/models/gui/laff_o_meter.bam').find('**/doghead')
		self.duckhead.reparentTo(base.a2dBottomLeft)
		self.smile = loader.loadModel('phase_3/models/gui/laff_o_meter.bam').find('**/smile')
		self.smile.reparentTo(self.duckhead)
		self.eyes = loader.loadModel('phase_3/models/gui/laff_o_meter.bam').find('**/eyes')
		self.eyes.reparentTo(self.duckhead)
		self.laffleft = OnscreenText( text = '100  100', mayChange = True, fg = (0, 0, 0, 1), pos = (-0.4, .07), scale = .42, font = font, align = TextNode.ACenter )
		self.laffleft.reparentTo(self.eyes)
		self.laffright = OnscreenText( text = '100  100', mayChange = True, fg = (0, 0, 0, 1), pos = (0.4, .07), scale = .42, font = font, align = TextNode.ACenter )
		self.laffright.reparentTo(self.eyes)
		self.laffnum = linecache.getline('DataFolder/Data.txt', 5)
		self.laffleft.setText(self.laffnum)
		self.laffright.setText(self.laffnum)
		self.duckhead.setScale(.1)
		self.duckhead.setPos(.17, 0, .15)
		self.color = linecache.getline('DataFolder/Data.txt', 3)
		if self.color == 'white\n':
			self.duckhead.setColor(white)
		if self.color == 'black\n':
			self.duckhead.setColor(black)
		if self.color == 'red\n':
			self.duckhead.setColor(red)
		if self.color == 'orange\n':
			self.duckhead.setColor(orange)
		if self.color == 'yellow\n':
			self.duckhead.setColor(yellow)
		if self.color == 'green\n':
			self.duckhead.setColor(green)
		if self.color == 'blue\n':
			self.duckhead.setColor(blue)
		if self.color == 'purple\n':
			self.duckhead.setColor(purple)
		if self.color == 'grey\n' or self.color == 'gray\n':
			self.duckhead.setColor(gray)
		if self.color == 'pink\n':
			self.duckhead.setColor(pink)
		self.eyes.setColor(white)
		
	def friendsButton(self):
		self.resources = loader.loadModel('phase_3.5/models/gui/friendslist_gui.bam')
		
		
		
GUI = GUI()
