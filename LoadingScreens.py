from direct.interval.IntervalGlobal import *
from direct.actor.Actor import Actor
from pandac.PandaModules import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
from pandac.PandaModules import Point3
from pandac.PandaModules import *
from direct.gui.DirectGui import *
import direct.directbase.DirectStart
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
#from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
#from StartMenu import Selection

background = OnscreenImage(image = ('phase_3/maps/loading_bg_clouds.jpg'), pos = (0, 0, 0), parent=render2d)
background.hide()
MickeyFont = loader.loadFont('phase_3/models/fonts/MickeyFont.bam')
ToontownCentral = OnscreenText(text='Heading to Toontown Central...', scale=0.08, pos=(0, -0.775, -0.775), align=TextNode.ACenter, font=MickeyFont, fg=(1, 1, 1, 1))
ToontownCentral.hide()
DonaldsDock = OnscreenText(text='Heading to Donald\'s Dock...', scale=0.08, pos=(0, -0.775, -0.775), align=TextNode.ACenter, font=MickeyFont, fg=(1, 1, 1, 1))
DonaldsDock.hide()
loadingtext = OnscreenText(text='Loading Game...', scale=0.08, pos=(0, -0.775, -0.775), align=TextNode.ACenter, font=MickeyFont, fg=(1, 1, 1, 1))
loadingtext.hide()
DaisyGardens = OnscreenText(text='Heading to Daisy Gardens...', scale=0.08, pos=(0, -0.775, -0.775), align=TextNode.ACenter, font=MickeyFont, fg=(1, 1, 1, 1))
DaisyGardens.hide()
Melodyland = OnscreenText(text='Heading to Minnie\'s Melodyland...', scale=0.08, pos=(0, -0.775, -0.775), align=TextNode.ACenter, font=MickeyFont, fg=(1, 1, 1, 1))
Melodyland.hide()
Brrrgh = OnscreenText(text='Heading to The Brrrgh...', scale=0.08, pos=(0, -0.775, -0.775), align=TextNode.ACenter, font=MickeyFont, fg=(1, 1, 1, 1))
Brrrgh.hide()
DonaldsDreamland = OnscreenText(text='Heading to Donald\'s Dreamland...', scale=0.08, pos=(0, -0.775, -0.775), align=TextNode.ACenter, font=MickeyFont, fg=(1, 1, 1, 1))
DonaldsDreamland.hide()
AcornAcres = OnscreenText(text='Heading to Acorn Acres...', scale=0.08, pos=(0, -0.775, -0.775), align=TextNode.ACenter, font=MickeyFont, fg=(1, 1, 1, 1))
AcornAcres.hide()
GSpeedway = OnscreenText(text='Heading to Goofy Speedway...', scale=0.08, pos=(0, -0.775, -0.775), align=TextNode.ACenter, font=MickeyFont, fg=(1, 1, 1, 1))
GSpeedway.hide()
progressbar = DirectWaitBar(value=0, range=100, pos=(0, 0, -0.85))
progressbar.hide()
progressbar.setSx(1.065)
progressbar.setSz(0.38)
randomnumber = 0

def ShowLoading():
  background.show()
  loadingtext.show()
  progressbar.show()
  base.graphicsEngine.renderFrame()
  base.graphicsEngine.renderFrame()
  
def addTime():
  progressbar['value'] += 20
  
def AreaLoaded():
  background.hide()
  loadingtext.hide()
  progressbar.hide()
  randomnumber = 5
  print "Loading Screen finished."
 
def resetTime():
  progressbar['value'] -= 100
  
def LoadingScreen():
  loadseq = Sequence()
  print "Loading Screen started."
  loadseq.append(Func(ShowLoading))
  loadseq.append(Wait(1))
  loadseq.append(Func(addTime))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTime))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTime))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTime))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTime))
  loadseq.append(Wait(.5))
  loadseq.append(Func(AreaLoaded))
  loadseq.append(Func(resetTime))
  loadseq.start()

#-------------------------------------------------------------------------

def ShowLoadingTTC():
  background.show()
  ToontownCentral.show()
  progressbar.show()
  base.graphicsEngine.renderFrame()
  base.graphicsEngine.renderFrame()
  
def addTimeTTC():
  progressbar['value'] += 20
  
def AreaLoadedTTC():
  background.hide()
  ToontownCentral.hide()
  progressbar.hide()
  print "Loading Screen finished."
 
def resetTimeTTC():
  progressbar['value'] -= 100
  
def LoadingScreenTTC():
  loadseq = Sequence()
  print "Loading Screen started."
  loadseq.append(Func(ShowLoadingTTC))
  loadseq.append(Wait(1))
  loadseq.append(Func(addTimeTTC))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeTTC))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeTTC))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeTTC))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeTTC))
  loadseq.append(Wait(.5))
  loadseq.append(Func(AreaLoadedTTC))
  loadseq.append(Func(resetTimeTTC))
  loadseq.start()

#-------------------------------------------------------------------------

def ShowLoadingDD():
  background.show()
  DonaldsDock.show()
  progressbar.show()
  base.graphicsEngine.renderFrame()
  base.graphicsEngine.renderFrame()
  
def addTimeDD():
  progressbar['value'] += 20
  
def AreaLoadedDD():
  background.hide()
  DonaldsDock.hide()
  progressbar.hide()
  print "Loading Screen finished."
 
def resetTimeDD():
  progressbar['value'] -= 100
  
def LoadingScreenDD():
  loadseq = Sequence()
  print "Loading Screen started."
  loadseq.append(Func(ShowLoadingDD))
  loadseq.append(Wait(1))
  loadseq.append(Func(addTimeDD))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeDD))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeDD))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeDD))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeDD))
  loadseq.append(Wait(.5))
  loadseq.append(Func(AreaLoadedDD))
  loadseq.append(Func(resetTimeDD))
  loadseq.start()
  
#-------------------------------------------------------------------------

def ShowLoadingDG():
  background.show()
  DaisyGardens.show()
  progressbar.show()
  base.graphicsEngine.renderFrame()
  base.graphicsEngine.renderFrame()
  
def addTimeDG():
  progressbar['value'] += 20
  
def AreaLoadedDG():
  background.hide()
  DaisyGardens.hide()
  progressbar.hide()
  print "Loading Screen finished."
 
def resetTimeDG():
  progressbar['value'] -= 100
  
def LoadingScreenDG():
  loadseq = Sequence()
  print "Loading Screen started."
  loadseq.append(Func(ShowLoadingDG))
  loadseq.append(Wait(1))
  loadseq.append(Func(addTimeDG))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeDG))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeDG))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeDG))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeDG))
  loadseq.append(Wait(.5))
  loadseq.append(Func(AreaLoadedDG))
  loadseq.append(Func(resetTimeDG))
  loadseq.start()
  
#-------------------------------------------------------------------------

def ShowLoadingMM():
  background.show()
  Melodyland.show()
  progressbar.show()
  base.graphicsEngine.renderFrame()
  base.graphicsEngine.renderFrame()
  
def addTimeMM():
  progressbar['value'] += 20
  
def AreaLoadedMM():
  background.hide()
  Melodyland.hide()
  progressbar.hide()
  print "Loading Screen finished."
 
def resetTimeMM():
  progressbar['value'] -= 100
  
def LoadingScreenMM():
  loadseq = Sequence()
  print "Loading Screen started."
  loadseq.append(Func(ShowLoadingMM))
  loadseq.append(Wait(1))
  loadseq.append(Func(addTimeMM))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeMM))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeMM))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeMM))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeMM))
  loadseq.append(Wait(.5))
  loadseq.append(Func(AreaLoadedMM))
  loadseq.append(Func(resetTimeMM))
  loadseq.start()
  
#-------------------------------------------------------------------------

def ShowLoadingBR():
  background.show()
  Brrrgh.show()
  progressbar.show()
  base.graphicsEngine.renderFrame()
  base.graphicsEngine.renderFrame()
  
def addTimeBR():
  progressbar['value'] += 20
  
def AreaLoadedBR():
  background.hide()
  Brrrgh.hide()
  progressbar.hide()
  print "Loading Screen finished."
 
def resetTimeBR():
  progressbar['value'] -= 100
  
def LoadingScreenBR():
  loadseq = Sequence()
  print "Loading Screen started."
  loadseq.append(Func(ShowLoadingBR))
  loadseq.append(Wait(1))
  loadseq.append(Func(addTimeBR))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeBR))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeBR))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeBR))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeBR))
  loadseq.append(Wait(.5))
  loadseq.append(Func(AreaLoadedBR))
  loadseq.append(Func(resetTimeBR))
  loadseq.start()  
  
#-------------------------------------------------------------------------

def ShowLoadingDL():
  background.show()
  DonaldsDreamland.show()
  progressbar.show()
  base.graphicsEngine.renderFrame()
  base.graphicsEngine.renderFrame()
  
def addTimeDL():
  progressbar['value'] += 20
  
def AreaLoadedDL():
  background.hide()
  DonaldsDreamland.hide()
  progressbar.hide()
  print "Loading Screen finished."
 
def resetTimeDL():
  progressbar['value'] -= 100
  
def LoadingScreenDL():
  loadseq = Sequence()
  print "Loading Screen started."
  loadseq.append(Func(ShowLoadingDL))
  loadseq.append(Wait(1))
  loadseq.append(Func(addTimeDL))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeDL))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeDL))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeDL))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeDL))
  loadseq.append(Wait(.5))
  loadseq.append(Func(AreaLoadedDL))
  loadseq.append(Func(resetTimeDL))
  loadseq.start()
  
#-------------------------------------------------------------------------

def ShowLoadingAA():
  background.show()
  AcornAcres.show()
  progressbar.show()
  base.graphicsEngine.renderFrame()
  base.graphicsEngine.renderFrame()
  
def addTimeAA():
  progressbar['value'] += 20
  
def AreaLoadedAA():
  background.hide()
  AcornAcres.hide()
  progressbar.hide()
  print "Loading Screen finished."
 
def resetTimeAA():
  progressbar['value'] -= 100
  
def LoadingScreenAA():
  loadseq = Sequence()
  print "Loading Screen started."
  loadseq.append(Func(ShowLoadingAA))
  loadseq.append(Wait(1))
  loadseq.append(Func(addTimeAA))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeAA))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeAA))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeAA))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeAA))
  loadseq.append(Wait(.5))
  loadseq.append(Func(AreaLoadedAA))
  loadseq.append(Func(resetTimeAA))
  loadseq.start()
  
#-------------------------------------------------------------------------

def ShowLoadingGS():
  background.show()
  GSpeedway.show()
  progressbar.show()
  base.graphicsEngine.renderFrame()
  base.graphicsEngine.renderFrame()
  
def addTimeGS():
  progressbar['value'] += 20
  
def AreaLoadedGS():
  background.hide()
  GSpeedway.hide()
  progressbar.hide()
  print "Loading Screen finished."
 
def resetTimeGS():
  progressbar['value'] -= 100
  
def LoadingScreenGS():
  loadseq = Sequence()
  print "Loading Screen started."
  loadseq.append(Func(ShowLoadingGS))
  loadseq.append(Wait(1))
  loadseq.append(Func(addTimeGS))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeGS))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeGS))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeGS))
  loadseq.append(Wait(.5))
  loadseq.append(Func(addTimeGS))
  loadseq.append(Wait(.5))
  loadseq.append(Func(AreaLoadedGS))
  loadseq.append(Func(resetTimeGS))
  loadseq.start()
