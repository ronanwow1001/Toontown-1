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
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject

rabbithead = loader.loadModel('phase_3/models/char/rabbit-heads-1000.bam')
rabbithead.find('**/head-long').removeNode()
rabbithead.find('**/head-front-long').removeNode()
rabbithead.find('**/muzzle-long-neutral').removeNode()
rabbithead.find('**/muzzle-long-surprise').removeNode()
rabbithead.find('**/muzzle-long-sad').removeNode()
rabbithead.find('**/muzzle-long-smile').removeNode()
rabbithead.find('**/muzzle-long-angry').removeNode()
rabbithead.find('**/muzzle-long-laugh').removeNode()
rabbithead.find('**/ears-long').removeNode()
rabbithead.find('**/joint_pupilL_long').removeNode()
rabbithead.find('**/joint_pupilR_long').removeNode()
rabbithead.find('**/muzzle-short-surprise').removeNode()
rabbithead.find('**/muzzle-short-sad').removeNode()
rabbithead.find('**/muzzle-short-smile').removeNode()
rabbithead.find('**/muzzle-short-angry').removeNode()
rabbithead.find('**/muzzle-short-laugh').removeNode()
#rabbithead.reparentTo(render)
rabbithead.find('**/head-short').setColor(0.347656, 0.820312, 0.953125, 1.0)
rabbithead.find('**/head-front-short').setColor(0.347656, 0.820312, 0.953125, 1.0)
rabbithead.find('**/ears-short').setColor(0.347656, 0.820312, 0.953125, 1.0)

rabbittorso = Actor('phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam', {"neutral" : "phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral.bam"})
rabbittorso.find('**/arms').setColor(0.347656, 0.820312, 0.953125, 1.0)
rabbittorso.reparentTo(render)
rabbittorso.loop("neutral")

rabbitlegs = Actor('phase_3/models/char/tt_a_chr_dgl_shorts_legs_1000.bam', {"neutral" : "phase_3/models/char/tt_a_chr_dgl_shorts_legs_neutral.bam"})
rabbitlegs.find('**/shoes').removeNode()
rabbitlegs.find('**/boots_short').removeNode()
rabbitlegs.find('**/boots_long').removeNode()
rabbitlegs.find('**/legs').setColor(0.347656, 0.820312, 0.953125, 1.0)
rabbitlegs.find('**/feet').setColor(0.347656, 0.820312, 0.953125, 1.0)
rabbitlegs.loop("neutral")
rabbitlegs.reparentTo(render)

neck = rabbittorso.find('**/neck')

rabbithead.reparentTo(neck)

run()
