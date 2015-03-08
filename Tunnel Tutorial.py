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
from sys import argv
from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker 
from sys import argv
from panda3d.core import Vec3
from pandac.PandaModules import loadPrcFileData
loadPrcFileData('configurate', 'window-title Loading')
from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
from direct.showbase import DirectObject
from direct.interval.IntervalGlobal import *
import urllib, os, __main__, random
from pandac.PandaModules import *
from random import choice
base.disableMouse()
from direct.directbase.DirectStart import *
from direct.actor.Actor import Actor
from pandac.PandaModules import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import Point3
from pandac.PandaModules import *
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.showbase.Transitions import *
from direct.gui.DirectGui import *
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
from direct.filter.CommonFilters import *
from panda3d.ai import *
import sys
from random import randint
import direct.directbase.DirectStart
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject


#PRINT Commands
ttc = "Toontown Central"
dd = "Donald\'s Dock"
dg = "Daisy\'s Gardens"
mm = "Minnie\'s Melodyland"
dl = "Donald\'s Dreamland"
br = "The Brrrgh"
aa = "Acorn Acres"
gs = "Goofy\'s Speedway"
silly = "Silly Street"
loopy = "Loopy Lane"
punchline = "Punchline Place"




#TOON IN GAME
base.disableMouse()

legsAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand-start.bam', 'firehose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_firehose.bam', 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateL-putt.bam', 'slip-forward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-forward.bam', 'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eatnrun.bam', 'tickle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_tickle.bam', 'water-gun': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_water-gun.bam', 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverNeutral.bam', 'swim': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swim.bam', 'catch-run': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gamerun.bam', 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sad-neutral.bam', 'pet-loop': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petloop.bam', 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zstart.bam', 'wave': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_wave.bam', 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelneutral.bam', 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_poleneutral.bam', 'bank': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_jellybeanJar.bam', 'scientistGame': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistGame.bam', 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand.bam', 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_lookloop-putt.bam', 'victory': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_victory-dance.bam', 'lose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_lose.bam', 'cringe': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_cringe.bam', 'right': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_right.bam', 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_headdown-putt.bam', 'conked': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_conked.bam', 'jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump.bam', 'into-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_into-putt.bam', 'fish-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishEND.bam', 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zend.bam', 'shrug': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_shrug.bam', 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_sprinkle-dust.bam', 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-bottle.bam', 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_takePhone.bam', 'melt': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_melt.bam', 'pet-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petin.bam', 'look-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_look-putt.bam', 'loop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_loop-putt.bam', 'good-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_good-putt.bam', 'juggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_juggle.bam', 'run': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_run.bam', 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_press-button.bam', 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-back-right.bam', 'water': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_water.bam', 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point-start.bam', 'bad-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_bad-putt.bam', 'struggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_struggle.bam', 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_running-jump.bam', 'callPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_callPet.bam', 'throw': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_pie-throw.bam', 'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eat_neutral.bam', 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_tug-o-war.bam', 'bow': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bow.bam', 'swing': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swing.bam', 'climb': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_climb.bam', 'scientistWork': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistWork.bam', 'think': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_think.bam', 'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameThrow.bam', 'walk': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_walk.bam', 'down': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_down.bam', 'pole': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_pole.bam', 'periscope': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_periscope.bam', 'duck': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_duck.bam', 'curtsy': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_curtsy.bam', 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zend.bam', 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_loop_dig.bam', 'angry': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_angry.bam', 'bored': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bored.bam', 'swing-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_swing-putt.bam', 'pet-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petend.bam', 'spit': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_spit.bam', 'right-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point.bam', 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_into_dig.bam', 'castlong': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_castlong.bam', 'confused': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_confused.bam', 'neutral': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_neutral.bam', 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zhang.bam', 'reel': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reel.bam', 'slip-backward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-backward.bam', 'sound': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_shout.bam', 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_sidestep-left.bam', 'up': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_up.bam', 'fish-again': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishAGAIN.bam', 'cast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_cast.bam', 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneBack.bam', 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneNeutral.bam', 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistJealous.bam', 'battlecast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fish.bam', 'sit-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_intoSit.bam', 'toss': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_toss.bam', 'happy-dance': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_happy-dance.bam', 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zstart.bam', 'teleport': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_teleport.bam', 'sit': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sit.bam', 'sad-walk': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_losewalk.bam', 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props-start.bam', 'book': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_book.bam', 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zhang.bam', 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistEmcee.bam', 'leverPull': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverPull.bam', 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_tutorial-neutral.bam', 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_badloop-putt.bam', 'give-props': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props.bam', 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-magnet.bam', 'hypnotize': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hypnotize.bam', 'left-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_left-point.bam', 'leverReach': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverReach.bam', 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_feedPet.bam', 'reel-H': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelH.bam', 'applause': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_applause.bam', 'smooch': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_smooch.bam', 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateR-putt.bam', 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishneutral.bam', 'push': 'phase_9/models/char/tt_a_chr_dgs_shorts_legs_push.bam', 'catch-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameneutral.bam', 'left': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_left.bam'}

torsoAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-hand-start.bam', 'firehose': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_firehose.bam', 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_rotateL-putt.bam', 'slip-forward': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_slip-forward.bam', 'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_eatnrun.bam', 'tickle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_tickle.bam', 'water-gun': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_water-gun.bam', 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverNeutral.bam', 'swim': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_swim.bam', 'catch-run': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gamerun.bam', 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_sad-neutral.bam', 'pet-loop': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petloop.bam', 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zstart.bam', 'wave': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_wave.bam', 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reelneutral.bam', 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_poleneutral.bam', 'bank': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_jellybeanJar.bam', 'scientistGame': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistGame.bam', 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-hand.bam', 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_lookloop-putt.bam', 'victory': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_victory-dance.bam', 'lose': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_lose.bam', 'cringe': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_cringe.bam', 'right': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_right.bam', 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_headdown-putt.bam', 'conked': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_conked.bam', 'jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump.bam', 'into-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_into-putt.bam', 'fish-end': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishEND.bam', 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zend.bam', 'shrug': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_shrug.bam', 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_sprinkle-dust.bam', 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hold-bottle.bam', 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_takePhone.bam', 'melt': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_melt.bam', 'pet-start': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petin.bam', 'look-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_look-putt.bam', 'loop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_loop-putt.bam', 'good-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_good-putt.bam', 'juggle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_juggle.bam', 'run': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_run.bam', 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_press-button.bam', 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-back-right.bam', 'water': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_water.bam', 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-point-start.bam', 'bad-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_bad-putt.bam', 'struggle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_struggle.bam', 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_running-jump.bam', 'callPet': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_callPet.bam', 'throw': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_pie-throw.bam', 'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_eat_neutral.bam', 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_tug-o-war.bam', 'bow': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_bow.bam', 'swing': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_swing.bam', 'climb': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_climb.bam', 'scientistWork': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistWork.bam', 'think': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_think.bam', 'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gameThrow.bam', 'walk': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_walk.bam', 'down': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_down.bam', 'pole': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_pole.bam', 'periscope': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_periscope.bam', 'duck': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_duck.bam', 'curtsy': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_curtsy.bam', 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zend.bam', 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_loop_dig.bam', 'angry': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_angry.bam', 'bored': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_bored.bam', 'swing-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_swing-putt.bam', 'pet-end': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petend.bam', 'spit': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_spit.bam', 'right-point': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-point.bam', 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_into_dig.bam', 'castlong': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_castlong.bam', 'confused': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_confused.bam', 'neutral': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral.bam', 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zhang.bam', 'reel': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reel.bam', 'slip-backward': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_slip-backward.bam', 'sound': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_shout.bam', 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_sidestep-left.bam', 'up': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_up.bam', 'fish-again': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishAGAIN.bam', 'cast': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_cast.bam', 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_phoneBack.bam', 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_phoneNeutral.bam', 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistJealous.bam', 'battlecast': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fish.bam', 'sit-start': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_intoSit.bam', 'toss': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_toss.bam', 'happy-dance': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_happy-dance.bam', 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zstart.bam', 'teleport': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_teleport.bam', 'sit': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_sit.bam', 'sad-walk': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_losewalk.bam', 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_give-props-start.bam', 'book': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_book.bam', 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zhang.bam', 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistEmcee.bam', 'leverPull': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverPull.bam', 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_tutorial-neutral.bam', 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_badloop-putt.bam', 'give-props': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_give-props.bam', 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hold-magnet.bam', 'hypnotize': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hypnotize.bam', 'left-point': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_left-point.bam', 'leverReach': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverReach.bam', 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_feedPet.bam', 'reel-H': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reelH.bam', 'applause': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_applause.bam', 'smooch': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_smooch.bam', 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_rotateR-putt.bam', 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishneutral.bam', 'push': 'phase_9/models/char/tt_a_chr_dgl_shorts_torso_push.bam', 'catch-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gameneutral.bam', 'left': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_left.bam'}

mouseHead = loader.loadModel('phase_3/models/char/mouse-heads-1000.bam')
otherParts = mouseHead.findAllMatches('**/*long*')
for partNum in range(0, otherParts.getNumPaths()):
	otherParts.getPath(partNum).removeNode()
ntrlMuzzle = mouseHead.find('**/*muzzle*neutral')
otherParts = mouseHead.findAllMatches('**/*muzzle*')
for partNum in range(0, otherParts.getNumPaths()):
	part = otherParts.getPath(partNum)
	if part != ntrlMuzzle:
		otherParts.getPath(partNum).removeNode()
mouseTorso = loader.loadModel('phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam')
mouseLegs  = loader.loadModel('phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000.bam')
otherParts = mouseLegs.findAllMatches('**/boots*')+mouseLegs.findAllMatches('**/shoes')
for partNum in range(0, otherParts.getNumPaths()):
	otherParts.getPath(partNum).removeNode()
 
mouseBody = Actor({'head':mouseHead, 'torso':mouseTorso, 'legs':mouseLegs},
				{'torso':torsoAnimDict, 'legs':legsAnimDict})
mouseBody.attach('head', 'torso', 'def_head')
mouseBody.attach('torso', 'legs', 'joint_hips')

#Gloves
gloves = mouseBody.findAllMatches('**/hands')
#Ears
ears = mouseBody.findAllMatches('**/*ears*')
#Head
head = mouseBody.findAllMatches('**/head-*')
#Sleeves
sleeves = mouseBody.findAllMatches('**/sleeves')
#Shirt
shirt = mouseBody.findAllMatches('**/torso-top')
#Shorts
shorts = mouseBody.findAllMatches('**/torso-bot')
#Neck
neck = mouseBody.findAllMatches('**/neck')
#Arms
arms = mouseBody.findAllMatches('**/arms')
#Legs
legs = mouseBody.findAllMatches('**/legs')
#Feet
feet = mouseBody.findAllMatches('**/feet')
 
bodyNodes = []
bodyNodes += [gloves]
bodyNodes += [head, ears]
bodyNodes += [sleeves, shirt, shorts]
bodyNodes += [neck, arms, legs, feet]
#Gloves
bodyNodes[0].setColor(2, 2, 2, 2)
#Head
bodyNodes[1].setColor(0.347656, 0.820312, 0.953125, 1.0)
#Ears
bodyNodes[2].setColor(0.347656, 0.820312, 0.953125, 1.0)
#Sleeves
bodyNodes[3].setColor(1, 1, 1, 1)
#Shirt
bodyNodes[4].setColor(1, 1, 1, 1)
#Shorts
bodyNodes[5].setColor(1, 1, 1, 1)
#Neck
bodyNodes[6].setColor(0.347656, 0.820312, 0.953125, 1.0)
#Arms
bodyNodes[7].setColor(0.347656, 0.820312, 0.953125, 1.0)
#Legs
bodyNodes[8].setColor(0.347656, 0.820312, 0.953125, 1.0)
#Feet
bodyNodes[9].setColor(0.347656, 0.820312, 0.953125, 1.0)
 
topTex = loader.loadTexture('phase_3/maps/desat_shirt_9.jpg')
botTex = loader.loadTexture('phase_3/maps/desat_shorts_2.jpg')
sleeveTex = loader.loadTexture('phase_3/maps/desat_sleeve_9.jpg')
 
bodyNodes[3].setTexture(sleeveTex, 1)
bodyNodes[4].setTexture(topTex, 1)
bodyNodes[5].setTexture(botTex, 1)
 
mouseBody.reparentTo(render)
 
geom = mouseBody.getGeomNode()
geom.getChild(0).setSx(0.730000019073)
geom.getChild(0).setSz(0.730000019073)
offset = 3.2375
 
base.camera.reparentTo(mouseBody)
base.camera.setPos(0, -10.0 - offset, offset)
wallBitmask = BitMask32(1)
floorBitmask = BitMask32(2)
base.cTrav = CollisionTraverser()
def getAirborneHeight():
	return offset + 0.025000000000000001
walkControls = GravityWalker(legacyLifter=True)
walkControls.setWallBitMask(wallBitmask)
walkControls.setFloorBitMask(floorBitmask)
walkControls.setWalkSpeed(24.0, 24.0, 8.0, 80.0)
walkControls.initializeCollisions(base.cTrav, mouseBody, floorOffset=0.025, reach=4.0)
walkControls.setAirborneHeightFunc(getAirborneHeight)
walkControls.enableAvatarControls()
mouseBody.physControls = walkControls
 
def setWatchKey(key, input, keyMapName):
	def watchKey(active=True):
		if active == True:
			inputState.set(input, True)
			keyMap[keyMapName] = 1
		else:
			inputState.set(input, False)
			keyMap[keyMapName] = 0
	base.accept(key, watchKey, [True])
	base.accept(key+'-up', watchKey, [False])
 
keyMap = {'left':0, 'right':0, 'forward':0, 'backward':0, 'control':0}
 
setWatchKey('arrow_up', 'forward', 'forward')
setWatchKey('control-arrow_up', 'forward', 'forward')
setWatchKey('alt-arrow_up', 'forward', 'forward')
setWatchKey('shift-arrow_up', 'forward', 'forward')
setWatchKey('arrow_down', 'reverse', 'backward')
setWatchKey('control-arrow_down', 'reverse', 'backward')
setWatchKey('alt-arrow_down', 'reverse', 'backward')
setWatchKey('shift-arrow_down', 'reverse', 'backward')
setWatchKey('arrow_left', 'turnLeft', 'left')
setWatchKey('control-arrow_left', 'turnLeft', 'left')
setWatchKey('alt-arrow_left', 'turnLeft', 'left')
setWatchKey('shift-arrow_left', 'turnLeft', 'left')
setWatchKey('arrow_right', 'turnRight', 'right')
setWatchKey('control-arrow_right', 'turnRight', 'right')
setWatchKey('alt-arrow_right', 'turnRight', 'right')
setWatchKey('shift-arrow_right', 'turnRight', 'right')
setWatchKey('control', 'jump', 'control')
 
movingNeutral, movingForward = (False, False)
movingRotation, movingBackward = (False, False)
movingJumping = False
 
def setMovementAnimation(loopName, playRate=1.0):
	global movingNeutral
	global movingForward
	global movingRotation
	global movingBackward
	global movingJumping
	if 'jump' in loopName:
		movingJumping = True
		movingForward = False
		movingNeutral = False
		movingRotation = False
		movingBackward = False
	elif loopName == 'run':
		movingJumping = False
		movingForward = True
		movingNeutral = False
		movingRotation = False
		movingBackward = False
	elif loopName == 'walk':
		movingJumping = False
		movingForward = False
		movingNeutral = False
		if playRate == -1.0:
			movingBackward = True
			movingRotation = False
		else:
			movingBackward = False
			movingRotation = True
	elif loopName == 'neutral':
		movingJumping = False
		movingForward = False
		movingNeutral = True
		movingRotation = False
		movingBackward = False
	else:
		movingJumping = False
		movingForward = False
		movingNeutral = False
		movingRotation = False
		movingBackward = False
	ActorInterval(mouseBody, loopName, playRate=playRate).loop()
 
def handleMovement(task):
	global movingNeutral, movingForward
	global movingRotation, movingBackward, movingJumping
	if keyMap['control'] == 1:
		if keyMap['forward'] or keyMap['backward'] or keyMap['left'] or keyMap['right']:
			if movingJumping == False:
				if mouseBody.physControls.isAirborne:
					setMovementAnimation('running-jump-idle')
				else:
					if keyMap['forward']:
						if movingForward == False:
							setMovementAnimation('run')
					elif keyMap['backward']:
						if movingBackward == False:
							setMovementAnimation('walk', playRate=-1.0)
					elif keyMap['left'] or keyMap['right']:
						if movingRotation == False:
							setMovementAnimation('walk')
			else:
				if not mouseBody.physControls.isAirborne:
					if keyMap['forward']:
						if movingForward == False:
							setMovementAnimation('run')
					elif keyMap['backward']:
						if movingBackward == False:
							setMovementAnimation('walk', playRate=-1.0)
					elif keyMap['left'] or keyMap['right']:
						if movingRotation == False:
							setMovementAnimation('walk')
		else:
			if movingJumping == False:
				if mouseBody.physControls.isAirborne:
					setMovementAnimation('jump-idle')
				else:
					if movingNeutral == False:
						setMovementAnimation('neutral')
			else:
				if not mouseBody.physControls.isAirborne:
					if movingNeutral == False:
						setMovementAnimation('neutral')
	elif keyMap['forward'] == 1:
		if movingForward == False:
			if not mouseBody.physControls.isAirborne:
				setMovementAnimation('run')
	elif keyMap['backward'] == 1:
		if movingBackward == False:
			if not mouseBody.physControls.isAirborne:
				setMovementAnimation('walk', playRate=-1.0)
	elif keyMap['left'] or keyMap['right']:
		if movingRotation == False:
			if not mouseBody.physControls.isAirborne:
				setMovementAnimation('walk')
	else:
		if not mouseBody.physControls.isAirborne:
			if movingNeutral == False:
				setMovementAnimation('neutral')
	return Task.cont
 
base.taskMgr.add(handleMovement, 'controlManager')
 
def collisionsOn():
	mouseBody.physControls.setCollisionsActive(True)
	mouseBody.physControls.isAirborne = True
def collisionsOff():
	mouseBody.physControls.setCollisionsActive(True)
	mouseBody.physControls.isAirborne = True
def toggleCollisions():
	if mouseBody.physControls.getCollisionsActive():
		mouseBody.physControls.setCollisionsActive(False)
		mouseBody.physControls.isAirborne = True
	else:
		mouseBody.physControls.setCollisionsActive(True)
		mouseBody.physControls.isAirborne = True

mouseBody.collisionsOn = collisionsOn
mouseBody.toggleCollisions = toggleCollisions
 
localAvatar = mouseBody
base.localAvatar = localAvatar
print "Avatar is loaded."
onScreenDebug.enabled = True
def updateOnScreenDebug(task):
	onScreenDebug.add('Avatar Position', localAvatar.getPos())
	onScreenDebug.add('Avatar Angle', localAvatar.getHpr())
	
	return Task.cont
	
base.taskMgr.add(updateOnScreenDebug, 'UpdateOSD')
print "OnScreenDebug is Active."

toontowncentral = loader.loadModel('phase_15/hood/daisys_garden.bam')
toontowncentral.reparentTo(render)
#toontowncentral.setTransparency(TransparencyAttrib.MBinary, 1)
print ttc, "is loaded."
sky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
sky.reparentTo(render)
print "Sky is loaded."

loadedArea = 'toontowncentral'

background = OnscreenImage(image = ('phase_3/maps/loading_bg_clouds.jpg'), pos = (0, 0, 0), parent=render2d)
background.hide()
MickeyFont = loader.loadFont('phase_3/models/fonts/MickeyFont.bam')
TTCloadingText = OnscreenText(text = "Heading to Toontown Central...", scale = .08, pos = (-1.065, -.775, -.775), align=TextNode.ALeft, font = MickeyFont, fg=(0, 0, 0.5176470588235293, 1))
TTCloadingText.hide()
PPloadingText = OnscreenText(text = "Heading to Punchline Place...", scale = .08, pos = (-1.065, -.775, -.775), align=TextNode.ALeft, font = MickeyFont, fg=(0, 0, 0.5176470588235293, 1))
PPloadingText.hide()
LLloadingText = OnscreenText(text = "Heading to Loopy Lane...", scale = .08, pos = (-1.065, -.775, -.775), align=TextNode.ALeft, font = MickeyFont, fg=(0, 0, 0.5176470588235293, 1))
LLloadingText.hide()
SSloadingText = OnscreenText(text = "Heading to Silly Street", scale = .08, pos = (-1.065, -.775, -.775), align=TextNode.ALeft, font = MickeyFont, fg=(0, 0, 0.5176470588235293, 1))
SSloadingText.hide()
progressbar = DirectWaitBar(value=0, range=100, pos=(0, 0, -0.85))
progressbar.hide()
progressbar.setSx(1.065)
progressbar.setSz(0.38)

def ShowLoading():
  background.show()
  progressbar.show()
  base.graphicsEngine.renderFrame()
  base.graphicsEngine.renderFrame()
  
def addTime():
  progressbar['value'] += 20
  
def AreaLoaded():
  background.hide()
  progressbar.hide()
 
def resetTime():
  progressbar['value'] -= 100
  
def LoadingScreen():
  loadseq = Sequence()
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

LoadingScreen()

def updateTunnel(task):
	global loadedArea
	global sillystreet
	global toontowncentral
	global loopylane
	global punchlineplace
	
	x = localAvatar.getPos().get_x()
	y = localAvatar.getPos().get_y()
	#Toontown Central to Silly Street
	if x >= 24.4827 and x <= 38.4088 and y <= -148.86 and y >= -157.229 and loadedArea == 'toontowncentral':
		LoadingScreen()
		loadingText.text = "Heading to Silly Street..."
		toontowncentral.removeNode()
		toontowncentral = loader.unloadModel('phase_4/models/neighborhoods/toontown_central_full.bam')
		print ttc, "is removed."
		loadedArea = 'sillystreet'
		sillystreet = loader.loadModel('phase_15/street/silly_street.bam')
		sillystreet.reparentTo(render)
		sky.hide()
		print silly, "is loaded."
		localAvatar.setPosHpr(-92.8635, -101.512, -.475, 807.436, 0, 0)
	#Silly Street To Toontown Central
	if x >= -89.3891 and x <= -89.0583 and y >= -108.088 and y <= -91.84 and loadedArea == 'sillystreet':
		LoadingScreen()
		sillystreet.removeNode()
		sillystreet = loader.unloadModel('phase_15/street/silly_street.bam')
		print silly, "is removed."
		loadedArea = 'toontowncentral'
		toontowncentral = loader.loadModel('phase_4/models/neighborhoods/toontown_central_full.bam')
		toontowncentral.reparentTo(render)
		sky.show()
		print ttc, "is loaded."
		localAvatar.setPosHpr(34.8669, -147.037, 2.525, 687.063, 0, 0)
		
	#Toontown Central to Loopy Lane
	if x>= -148.853 and x <= -148.477 and y >= -4.0677 and y <= 12.18 and loadedArea == 'toontowncentral' :
		LoadingScreen()
		loadingText.text = "Heading to Loopy Lane..."
		toontowncentral.removeNode()
		toontowncentral = loader.unloadModel('phase_4/models/neighborhoods/toontown_central_full.bam')
		print ttc, "is removed."
		loadedArea = 'loopylane'
		loopylane = loader.loadModel('phase_15/street/loopy_lane.bam')
		loopylane.reparentTo(render)
		sky.hide()
		print loopy, "is loaded."
		localAvatar.setPosHpr(-77.9962, 94.6412, -.475, 90.4253, 0, 0)
		
	#Loopy Lane to Toontown Central
	if x >= -74.4742 and x <= -74.3676 and y >= 86.8523 and y <= 103.1 and loadedArea == 'loopylane' :
		LoadingScreen()
		loopylane.removeNode()
		loopylane = loader.unloadModel('phase_15/street/loopy_lane.bam')
		print loopy, "is removed."
		loadedArea = 'toontowncentral'
		toontowncentral = loader.loadModel('phase_4/models/neighborhoods/toontown_central_full.bam')
		toontowncentral.reparentTo(render)
		sky.show()
		print ttc, "is loaded."
		localAvatar.setPosHpr(-143.758, 3.33671, .525, 262.36, 0, 0)
		
	#Toontown Central to Punchline Place
	if x>= -54.2305 and x<= -38.067 and y >= 93.3841 and y<= 95.1947 and loadedArea == 'toontowncentral' :
		loadingText.text = "Heading to Punchline Place..."
		LoadingScreen()
		toontowncentral.removeNode()
		toontowncentral = loader.unloadModel('phase_4/models/neighborhoods/toontown_central_full.bam')
		print ttc, "is removed."
		loadedArea = 'punchlineplace'
		punchlineplace = loader.loadModel('phase_15/street/punchline_place.bam')
		punchlineplace.reparentTo(render)
		sky.hide()
		print punchline, "is loaded."
		localAvatar.setPosHpr(2.02962, 20.0454, -.475, 270.907, 0, 0)
		
	#Punchline Place to Toontown Central
	if x>= -.170619 and x<= .00195409 and y>= 11.9 and y<= 28.1477 and loadedArea == 'punchlineplace' :
		TTCloadingText.show()
		LoadingScreen()
		punchlineplace.removeNode()
		punclineplace = loader.unloadModel('phase_15/street/punchline_place.bam')
		print punchline, "is removed."
		loadedArea = 'toontowncentral'
		toontowncentral = loader.loadModel('phase_4/models/neighborhoods/toontown_central_full.bam')
		toontowncentral.reparentTo(render)
		sky.show()
		print ttc, "is loaded."
		localAvatar.setPosHpr(-44.6497, 88.9564, .525, 174.003, 0, 0)
		
	
	return Task.cont

base.taskMgr.add(updateTunnel, 'UpdateTunnel')

base.disableMouse()
run()
