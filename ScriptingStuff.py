#Scripted by Sam Goodin (Master Max)
#Also Scripted by Caleb Marshall (Flippy)

from sys import argv
from socket import *
import threading
import thread
from direct.gui.DirectGui import *
from direct.actor.Actor import Actor
from pandac.PandaModules import *
import math
import sys
import socket
from direct.showbase.Audio3DManager import Audio3DManager
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import Point3
from pandac.PandaModules import *
#nout = MultiplexStream()
#Notify.ptr().setOstreamPtr(nout, 0)
#nout.addFile(Filename("tte.log"))
#loadPrcFileData('', 'framebuffer-multisample 1')
#loadPrcFileData('', 'multisamples 8')
#loadPrcFileData('', 'notify-level info')
#loadPrcFileData('', 'default-directnotify-level info')
#loadPrcFileData('', 'want-tk #t')
#ConfigVariableString('default-model-extension', '.bam').setValue('.bam')
from random import choice
import direct.directbase.DirectStart
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
from direct.controls.GravityWalker import GravityWalker
from direct.showbase.InputStateGlobal import inputState
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
import SocketServer
from direct.fsm import StateData
from direct.directnotify import DirectNotifyGlobal
import direct.directbase.DirectStart, random
from sys import argv
from direct.task import Task
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Func, Wait, Sequence
from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import *
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename, AmbientLight, DirectionalLight
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import Vec3, Vec4, BitMask32
from sys import argv
from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *


title = OnscreenImage(image='phase_3/maps/loading_bg_clouds.jpg', pos=(0, 0, 0.0), parent=render2d)
base.graphicsEngine.renderFrame()
base.graphicsEngine.renderFrame()
title.destroy()
toonmono = Filename("phase_3/models/gui/toonmono.cur")
props = WindowProperties()
props.setCursorFilename(toonmono)
#props.setFullscreen(True)
props.setTitle('Toontown Redawned')
props.setIconFilename("phase_1/toontown.ico")
base.win.requestProperties(props)




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

BTFont = loader.loadFont('phase_3/models/fonts/MickeyFont.bam')

sound2 = loader.loadSfx('phase_6/audio/bgm/DD_nbrhood.mp3')
sound1 = loader.loadSfx('phase_6/audio/bgm/GS_SZ.mp3')
sound = loader.loadSfx('phase_4/audio/bgm/TC_nbrhood.mp3')
sound3 = loader.loadSfx('phase_6/audio/bgm/MM_nbrhood.mp3')
sound4 = loader.loadSfx('phase_8/audio/bgm/DL_nbrhood.mp3')
sound5 = loader.loadSfx('phase_4/audio/bgm/Estate Music (new_years_fireworks_music).mp3')
sound6 = loader.loadSfx('phase_8/audio/bgm/DG_nbrhood.mp3')
sound7 = loader.loadSfx('phase_8/audio/bgm/TB_nbrhood.mp3')
sound.setLoop(True)
sound.play()

#Toontown Central Base Terrain
terrain = loader.loadModel('phase_15/hood/toontown_central.bam')
terrain.setPos(9.15527e-005, -1.90735e-006, 2.6226e-006)
terrain.setHpr(0, 0, -0)
terrain.reparentTo(render)

#TTC Sky

sky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
sky.reparentTo(render)
sky.setTransparency(TransparencyAttrib.MBinary, 1)

base.cTrav = CollisionTraverser()
 
#Set it up
collHandEvent = CollisionHandlerEvent()
collHandEvent.addInPattern('into')
collHandEvent.addOutPattern('outof')
 
#Create piers array
 
piers_tt = list()
cSpheres = list()
FishingGUI = loader.loadModel('phase_4/models/gui/fishingGui.bam')
FishingGUI.show()
 
#Setup Pier Function which creates a pier, only taking the co-ordinates
def setupPier(posx, posy, posz, hprx, hpry, hprz):
        piers_tt.append(loader.loadModel('phase_4/models/props/piers_tt.bam'))
        curPier = len(piers_tt)-1
        piers_tt[curPier].setPos(posx, posy, posz)
        piers_tt[curPier].setHpr(hprx, hpry, hprz)
        piers_tt[curPier].reparentTo(render)
        cSpheres.append(CollisionSphere(0, 0, 1, 1))
        curSphere = len(cSpheres)-1
        cnodePath = piers_tt[curPier].attachNewNode(CollisionNode('cnode'))
        cnodePath.node().addSolid(cSpheres[curSphere])
        base.cTrav.addCollider(cnodePath, collHandEvent)
        return piers_tt[curPier]
        cnodePath.show()
 
#Create the piers
Pier1 = setupPier(-63.5335, 41.648, -3.36708, 120, 0, 0)
Pier2 = setupPier(-90.2253, 42.5202, -3.3105, -135, 0, 0)
Pier3 = setupPier(-94.9218, 31.4153, -3.20083, -105, 0, 0)
Pier4 = setupPier(-77.5199, 46.9817, -3.28456, -180, 0, 0)
 
#Setup Collision events
def collisionInto():
        FishingGUI.show()
 
def collisionOutof():
        FishingGUI.hide()
 
base.accept('into', collisionInto)
base.accept('outof', collisionOutof)
 
#Show Piers Collision
def toggleCollisions():
        pierCollisions(Pier1)
        pierCollisions(Pier2)
        pierCollisions(Pier3)
        pierCollisions(Pier4)
       
def pierCollisions(pier):
        pier.physControls.setCollisionsActive(False)
        pier.physControls.isAirborne = True
        pier.physControls.setCollisionsActive(True)
        pier.physControls.isAirborne = True
               
base.accept('f1', toggleCollisions)
 
FishingGUI.show()

#Fisherman Freddy
toon1part1 = Actor("phase_3/models/char/tt_a_chr_dgl_shorts_legs_1000.bam", {"animate":"phase_3/models/char/tt_a_chr_dgl_shorts_legs_neutral.bam"})
toon1part1.reparentTo(render)
toon1part1.loop('animate')
toon1part1.find('**/shoes').remove()
toon1part1.find('**/boots_short').remove()
toon1part1.find('**/boots_long').remove()
toon1part1.find('**/feet').setColor(0.347656, 0.820312, 0.953125, 1.0)
toon1part1.find('**/legs').setColor(0.347656, 0.820312, 0.953125, 1.0)
toon1part1.setPos(-66.4848, -2.016, -1.975)
 
legs = toon1part1.find('**/joint_hips')
toon1part2 = Actor("phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam", {"animate":"phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral.bam"})
toon1part2.find('**/neck').setColor(0.347656, 0.820312, 0.953125, 1.0)
toon1part2.find('**/arms').setColor(0.347656, 0.820312, 0.953125, 1.0)
 
toonsleeves = loader.loadTexture('phase_3/maps/desat_sleeve_10.jpg')
toon1part2.find('**/sleeves').setTexture(toonsleeves,1)

 
toonjacket = loader.loadTexture('phase_3/maps/desat_shirt_2.jpg')
toon1part2.find('**/torso-top').setTexture(toonjacket,1)

 
toonshorts = loader.loadTexture('phase_3/maps/desat_shorts_2.jpg')
toon1part2.find('**/torso-bot').setTexture(toonshorts,1)


 
toon1part2.reparentTo(legs)
toon1part2.loop('animate')
head = toon1part1.find('**/def_head')
npc1part3 = loader.loadModel('phase_3/models/char/rabbit-heads-1000.bam')
npc1part3.find('**/muzzle-short-sad').remove()
npc1part3.find('**/muzzle-short-smile').remove()
npc1part3.find('**/muzzle-short-angry').remove()
npc1part3.find('**/muzzle-short-laugh').remove()
npc1part3.find('**/muzzle-short-surprise').remove()
npc1part3.find('**/muzzle-long-sad').remove()
npc1part3.find('**/muzzle-long-smile').remove()
npc1part3.find('**/muzzle-long-angry').remove()
npc1part3.find('**/muzzle-long-laugh').remove()
npc1part3.find('**/muzzle-long-neutral').remove()
npc1part3.find('**/head-front-long').remove()
npc1part3.find('**/head-long').remove()
npc1part3.find('**/ears-long').remove()
npc1part3.find('**/joint_pupilL_long').remove()
npc1part3.find('**/joint_pupilR_long').remove()
npc1part3.find('**/muzzle-long-surprise').remove()
npc1part3.find('**/eyes').setColor(180, 180, 180)
npc1part3.find('**/head-short').setColor(0.347656, 0.820312, 0.953125, 1.0)
npc1part3.find('**/head-front-short').setColor(0.347656, 0.820312, 0.953125, 1.0)
npc1part3.find('**/ears-short').setColor(0.347656, 0.820312, 0.953125, 1.0)
npc1part3.find('**/joint_pupilL_short').setColor(180, 180, 180)
npc1part3.find('**/joint_pupilR_short').setColor(180, 180, 180)
npc1part3.reparentTo(head)


#Silly Meter
#sm = loader.loadModel('phase_4/models/props/tt_a_ara_ttc_sillyMeter_default.bam')
#sm.setPos(37.1841, -0.159193, 4.02437)
#sm.setH(90.00)
#sm.reparentTo(render)
#rope = loader.loadModel('phase_4/models/modules/tt_m_ara_int_ropes.bam')
#rope.setPos(37.1841, -0.159193, 4.02437)
#rope.reparentTo(render)
Toon = Actor({"torso":"phase_3/models/char/tt_a_chr_dgs_shorts_torso_1000.bam", \
			 "legs":"phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000.bam"}, \
			 {"torso":{"walk": "phase_3/models/char/tt_a_chr_dgs_shorts_torso_1000.bam", \
			 "torsoAnimation":"phase_3/models/char/tt_a_chr_dgs_shorts_torso_neutral.bam"}, \
			 "legs":{"walk":"phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000.bam",
			 "legsAnimation":"phase_3/models/char/tt_a_chr_dgs_shorts_legs_neutral.bam"}})
 
Toon.attach("torso", "legs", "joint_hips")
 
#Animations
Toon.loop("torsoAnimation")
Toon.loop("legsAnimation")
 
#Pos, Hpr, Scale, ReparentTo
Toon.setPos(32.3009, 6.47458, 4.02493)
Toon.setHpr(0, 0, 0)
Toon.setH(90.00)
Toon.reparentTo(render)
 
#Gloves
gloves = Toon.find('**/hands')
gloves.setColor(1, 1, 1, 1)
 
#----------------------------------------Clothes---------------------------------------
  
  #Mouse pointer texture!

#mpointer = loader.loadTexture('phase_3/maps/Toontown_Dog.png')
#mpointer.reparentTo(render2d)

#mpointer.setBin('fixed', 100)

#def mousePointerTask(task):
	#if base.mouseWatcherNode.hasMouse():
		#mousex=base.mouseWatcherNode.getmouseX()
		#mousey=base.mouseWatcherNode.getmousey()
		
	#	mpointer.setx(mousex)
	#	mpointer.setz(mousey)	
	
		#return task.cont

  
  
#Sleeves
mySleeve = loader.loadTexture("phase_4/maps/PJSleeveBlue.jpg")
Toon.find('**/sleeves').setColor(1)
  
#Shirts
myShirt = loader.loadTexture("phase_4/maps/tt_t_chr_shirt_scientistA.jpg")
Toon.find('**/torso-top').setTexture(myShirt, 1)
  
#Shorts
myShort = loader.loadTexture("phase_4/maps/tt_t_chr_shorts_scientistA.jpg")
Toon.find('**/torso-bot').setTexture(myShort, 1)
  
#Shoes/Boots
Toon.find('**/boots_long').hide()
Toon.find('**/shoes').hide()
Toon.find('**/boots_short').hide()
 
#Head
Head = Actor("phase_3/models/char/tt_a_chr_dgs_shorts_head_1000.bam",
			{"anim":"phase_3/models/char/tt_a_chr_dgs_shorts_head_neutral.bam"})
		 
Head.setColor(1,1,1)
Head.loop("anim")
Head.find('**/nose').show()
Head.find('**/ears').setColor(0)
Head.find('**/muzzle').setColor(0.87,0.65,0.47)
tophead = Head.find('**/head')
bottomhead = Head.find('**/head-front')
  
Neck = Toon.find('**/def_head')
Head.reparentTo(Neck)
 
#Colors
tophead.setColor(.2,0.1,2)
bottomhead.setColor(0.2,0.1,2)
Toon.find('**/neck').setColor(0.2,0.1,2)
Toon.find('**/arms').setColor(0.2,0.1,2)
Toon.find('**/legs').setColor(0.2,0.1,2)
Toon.find('**/feet').setColor(0.2,0.1,2)


#Doodle
#doodle = Actor('phase_4/models/char/TT_pets-mod.bam', {"Backflip":'phase_5/models/char/TT_pets-backflip.bam'})
#doodle.loop('Backflip')
#doodle.setPos(-20, 0, 0)
#doodle.find('**/birdTail').remove()
#doodle.find('**/antennae').remove()
#doodle.find('**/dogEars').remove()
#doodle.find('**/catTail').remove()
#doodle.find('**/bunnyTail').remove()
#doodle.find('**/horns').remove()
#doodle.find('**/feathers').remove()
#doodle.find('**/catEars').remove()
#doodle.find('**/clownNose').remove()
#doodle.find('**/dogNose').remove()
#doodle.find('**/pigNose').remove()
#doodle.find('**/eyeWhites').setColor(1, 1, 1, 1)
#doodle.reparentTo(render)

def TP1():
	mouseBody.setZ(500.89)
	mouseBody.setY(59.6964)
	mouseBody.setX(-1.00264)
	if sound.status() == sound.PLAYING:
		sound.stop()
		
	if sound2.status() == sound2.PLAYING:
		sound2.stop()
		
	if sound3.status() == sound3.PLAYING:
		sound3.stop()
		
	if sound4.status() == sound4.PLAYING:
		sound4.stop()
		
	if sound5.status() == sound5.PLAYING:
		sound5.stop()
		
	if sound6.status() == sound6.PLAYING:
		sound6.stop()
		
	if sound7.status() == sound7.PLAYING:
		sound7.stop()
		
	sound1.setLoop(True)
	sound1.play()
	
	Sticker.show()
	PortTTC.hide()
	Open.hide()
	PortDock.hide()
	PortSpeedway.hide()
	PortMM.hide()
	PortDL.hide()
	PortEstate.hide()
	bookOpen1.hide()
	PortBrr.hide()
	PortDG.hide()
	PortSellbot.hide()
	
 
 
ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')
environ = loader.loadModel('phase_6/models/karting/GasolineAlley_TT.bam')
environ.reparentTo(render)
environ.setZ(500)
sky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
sky.setPos(59.6964, -1.00264, 500.89)
sky.reparentTo(render)
tunnel = loader.loadModel('phase_4/models/modules/safe_zone_tunnel_TT.bam')
tunnel.reparentTo(render)
tunnel.setPos(60, 175, 493)
tunnel.setHpr(180, 0, 0)
tunnel.setScale(1)
tunnelsign = loader.loadModel('phase_3.5/models/props/tunnel_sign_orange.bam')
tunnelsign.reparentTo(tunnel)
tunnelsign.setPos(60, 95.01, 523.7)
tunnelsign.setHpr(180, 0, 0)
tunnelsign.setScale(1.6)
SZsign = loader.loadModel('phase_4/models/props/goofySZ.bam')
SZsign.reparentTo(tunnel)
SZsign.setPos(60, 95.025, 523.7)
SZsign.setHpr(180, 0, 0)
SZsign.setScale(4)
kartshop = loader.loadModel('phase_6/models/karting/kartShop.bam')
kartshop.reparentTo(render)
kartshop.setPos(0, 10, 500)
scoreboard = loader.loadModel('phase_6/models/karting/tt_m_ara_gfs_leaderBoardCrashed.bam')
scoreboard.reparentTo(render)
scoreboard.setPos(1, -111, 500)
scoreboard.setHpr(180, 0, 0)
wrench = loader.loadModel('phase_6/models/karting/KartArea_WrenchJack.bam')
wrench.reparentTo(render)
wrench.setPos(-33, 5, 500)
wrench.setHpr(180, 0, 0)
tires = loader.loadModel('phase_6/models/karting/KartArea_Tires.bam')
tires.reparentTo(render)
tires.setPos(33, 5, 500)
trees1 = loader.loadModel('phase_6/models/karting/GoofyStadium_TreeBase.bam')
trees1.reparentTo(render)
trees1.setPos(-13, 58, 499.7)
trees1.setScale(12)
trees2 = loader.loadModel('phase_6/models/karting/GoofyStadium_TreeBase.bam')
trees2 = loader.loadModel('phase_6/models/karting/GoofyStadium_TreeBase.bam')
trees2.reparentTo(render)
trees2.setPos(13, 58, 499.7)
trees2.setScale(12)
trees3 = loader.loadModel('phase_6/models/karting/GoofyStadium_TreeBase.bam')
trees3.reparentTo(render)
trees3.setPos(-13, -35, 499.7)
trees3.setScale(12)
trees4 = loader.loadModel('phase_6/models/karting/GoofyStadium_TreeBase.bam')
trees4.reparentTo(render)
trees4.setPos(13, -35, 499.7)
trees4.setScale(12)
trees5 = loader.loadModel('phase_6/models/karting/GoofyStadium_TreeBase.bam')
trees5.reparentTo(render)
trees5.setPos(-10, -76, 499.7)
trees5.setScale(12)
trees6 = loader.loadModel('phase_6/models/karting/GoofyStadium_TreeBase.bam')
trees6.reparentTo(render)
trees6.setPos(10, -76, 499.7)
trees6.setScale(12)
light1 = loader.loadModel('phase_6/models/karting/GoofyStadium_Lamppost_Base1.bam')
light1.reparentTo(render)
light1.setPos(-10, -52, 499.3)
light1.setScale(14)
light2 = loader.loadModel('phase_6/models/karting/GoofyStadium_Lamppost_Base1.bam')
light2.reparentTo(render)
light2.setPos(10, -52, 499.3)
light2.setScale(14)
box = loader.loadModel('phase_6/models/karting/GoofyStadium_Mailbox.bam')
box.reparentTo(render)
box.setPos(16, -50, 500)
box.setHpr(210, 0, 0)
box.setScale(10)
flag1 = loader.loadModel('phase_6/models/karting/flag.bam')
flag1.reparentTo(render)
flag1.setPos(-18, 6, 499.8)
flag2 = loader.loadModel('phase_6/models/karting/flag.bam')
flag2.reparentTo(render)
flag2.setPos(18, 6, 499.8)
sign = loader.loadModel('phase_6/models/karting/KartShowBlockSign.bam')
sign.reparentTo(render)
sign.setPos(-16, -50, 500)
sign.setHpr(-120, 0, 0)
sign.setScale(26)
announcer1 = loader.loadModel('phase_6/models/karting/announcer.bam')
announcer1.reparentTo(render)
announcer1.setPos(25, -150, 499.3)
announcer1.setHpr(-140, 0, 0)
announcer2 = loader.loadModel('phase_6/models/karting/announcer.bam')
announcer2.reparentTo(render)
announcer2.setPos(-26, -149, 499.3)
announcer2.setHpr(-212, 0, 0)
announcer3 = loader.loadModel('phase_6/models/karting/announcer.bam')
announcer3.reparentTo(render)
announcer3.setPos(-38, -135, 499.3)
announcer3.setHpr(-212, 0, 0)
announcer4 = loader.loadModel('phase_6/models/karting/announcer.bam')
announcer4.reparentTo(render)
announcer4.setPos(37, -137.5, 499.3)
announcer4.setHpr(-140, 0, 0)
cone1 = loader.loadModel('phase_6/models/karting/cone.bam')
cone1.reparentTo(render)
cone1.setPos(13, -4, 499.7)
cone2 = loader.loadModel('phase_6/models/karting/cone.bam')
cone2.reparentTo(render)
cone2.setPos(13, 20, 499.7)
cone3 = loader.loadModel('phase_6/models/karting/cone.bam')
cone3.reparentTo(render)
cone3.setPos(-14, 18, 499.7)
cone4 = loader.loadModel('phase_6/models/karting/cone.bam')
cone4.reparentTo(render)
cone4.setPos(-14, -3, 499.7)
cone5 = loader.loadModel('phase_6/models/karting/cone.bam')
cone5.reparentTo(render)
cone5.setPos(-23, 9, 499.7)
cone6 = loader.loadModel('phase_6/models/karting/cone.bam')
cone6.reparentTo(render)
cone6.setPos(45, -138, 499.4)
cone7 = loader.loadModel('phase_6/models/karting/cone.bam')
cone7.reparentTo(render)
cone7.setPos(25, -109, 500)
cone8 = loader.loadModel('phase_6/models/karting/cone.bam')
cone8.reparentTo(render)
cone8.setPos(24, -111, 500)
cone8.setHpr(45, 0, 0)
cone9 = loader.loadModel('phase_6/models/karting/cone.bam')
cone9.reparentTo(render)
cone9.setPos(75, -106, 500)
cone9.setHpr(0, 0, -120)
cone10 = loader.loadModel('phase_6/models/karting/cone.bam')
cone10.reparentTo(render)
cone10.setPos(76.5, -107.5, 500)
cone10.setHpr(0, 120, 0)
cone11 = loader.loadModel('phase_6/models/karting/cone.bam')
cone11.reparentTo(render)
cone11.setPos(26, -154, 499.3)
cone11.setHpr(42, 0, 0)
cone12 = loader.loadModel('phase_6/models/karting/cone.bam')
cone12.reparentTo(render)
cone12.setPos(1, -187, 501.22)
cone12.setHpr(42, 0, 0)
krate1 = loader.loadModel('phase_6/models/karting/krate.bam')
krate1.reparentTo(render)
krate1.setPos(1, -187, 499.3)
krate1.setScale(1.2)
krate2 = loader.loadModel('phase_6/models/karting/krate.bam')
krate2.reparentTo(render)
krate2.setPos(-48, -115, 499.3)
krate2.setScale(1.2)
krate3 = loader.loadModel('phase_6/models/karting/krate.bam')
krate3.reparentTo(render)
krate3.setPos(-50, -113, 499.3)
krate3.setHpr(45, 0, 0)
krate3.setScale(1.2)
krate4 = loader.loadModel('phase_6/models/karting/krate.bam')
krate4.reparentTo(render)
krate4.setPos(-49, -114, 501.22)
krate4.setHpr(60, 0, 0)
krate4.setScale(1.2)


def TP2():
	mouseBody.setZ(0)
	mouseBody.setX(0)
	mouseBody.setY(0)
	if sound1.status() == sound.PLAYING:
			sound1.stop()
			
	if sound2.status() == sound2.PLAYING:
		sound2.stop()
		
	if sound3.status() == sound3.PLAYING:
		sound3.stop()
		
	if sound4.status() == sound4.PLAYING:
		sound4.stop()
		
	if sound5.status() == sound5.PLAYING:
		sound5.stop()
		
	if sound6.status() == sound6.PLAYING:
		sound6.stop()
		
	if sound7.status() == sound7.PLAYING:
		sound7.stop()
		
	sound.setLoop(True)
	sound.play()
	
	Sticker.show()
	PortTTC.hide()
	Open.hide()
	PortDock.hide()
	PortSpeedway.hide()
	PortSpeedway.hide()
	PortMM.hide()
	PortDL.hide()
	PortEstate.hide()
	bookOpen1.hide()
	PortBrr.hide()
	PortDG.hide()
	PortSellbot.hide()
 
ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')
lord = Actor('phase_3/models/char/mickey-1200.bam', {'walk': 'phase_3/models/char/mickey-walk.bam'})
lord.reparentTo(render)
lord.loop('walk')
lord.setX(106.58)
lord.setY(-1.37)
lord.setZ(4.46)
lord.setH(104.62)
cs = CollisionSphere(0, 0, 1, 1)
cnodePath = lord.attachNewNode(CollisionNode('cnode'))
cnodePath.node().addSolid(cs)
pandaPosInterval1 = lord.posInterval(3, Point3(96.3312, 0.553801, 4.025), startPos=Point3(96.3312, 0.553801, 4.025))
pandaHprInterval1 = lord.hprInterval(3, Point3(96.3312, 0.553801, 4.025), startHpr=Point3(96.3312, 0.553801, 4.025))
pandaPosInterval2 = lord.posInterval(3, Point3(54.1032, 10.1371, 4.025), startPos=Point3(96.3312, 0.553801, 4.025))
pandaHprInterval2 = lord.hprInterval(3, Point3(172.798, 0, 0), startHpr=Point3(96.3312, 0.553801, 4.025))
pandaPosInterval3 = lord.posInterval(3, Point3(62.9905, -21.4791, 6.05112), startPos=Point3(54.1032, 10.1371, 4.025))
pandaHprInterval3 = lord.hprInterval(3, Point3(438.492, 0, 0), startHpr=Point3(172.798, 0, 0))
lord.pandaPace = Sequence(pandaPosInterval1, pandaHprInterval1, pandaPosInterval2, pandaHprInterval2, pandaPosInterval3, pandaHprInterval3)
lord.pandaPace.loop()
terrain = loader.loadModel('phase_15/hood/toontown_central.bam')
terrain.setPos(9.15527e-005, -1.90735e-006, 2.6226e-006)
terrain.setHpr(0, 0, 0)
terrain.reparentTo(render)
terrain.setTransparency(TransparencyAttrib.MBinary, 1)

sky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
sky.reparentTo(render)


#Cog
#cog = Actor('phase_3.5/models/char/suitA-mod.bam', {"Walk":'phase_4/models/char/suitA-walk.bam'})
#cog.loop('Walk')
#cog.setPos(-10, 0, 0)
#cog.reparentTo(render)
#myTex = loader.loadTexture('phase_3.5/maps/l_blazer.jpg')
#cog.findAllMatches('**/torso').setTexture(myTex, 1)
#myTex2 = loader.loadTexture('phase_3.5/maps/l_leg.jpg')
#cog.findAllMatches('**/legs').setTexture(myTex2, 1)
#myTex3 = loader.loadTexture('phase_3.5/maps/l_sleeve.jpg')
#cog.findAllMatches('**/arms').setTexture(myTex3, 1)
#head = loader.loadModel('phase_4/models/char/suitA-heads.bam').find('**/numbercruncher')
#head.reparentTo(cog.find('**/joint_head'))
#cog.find('**/hands').setColor(0.75, 0.75, 0.95, 1.0)



def TP3():
	mouseBody.setZ(509.622)
	mouseBody.setX(475.71)
	mouseBody.setY(502.166)
	if sound.status() == sound.PLAYING:
		sound.stop()
	sound2.setLoop(True)
	sound2.play()
	
	if sound3.status() == sound3.PLAYING:
		sound3.stop()
	
	if sound1.status() == sound1.PLAYING:
		sound1.stop()
		
	if sound4.status() == sound4.PLAYING:
		sound4.stop()
	
	if sound5.status() == sound5.PLAYING:
		sound5.stop()
		
	if sound6.status() == sound6.PLAYING:
		sound6.stop()
		
	if sound7.status() == sound7.PLAYING:
		sound7.stop()
		
		sound2.setLoop(True)
		sound2.play()
		
	Sticker.show()
	PortTTC.hide()
	Open.hide()
	PortDock.hide()
	PortSpeedway.hide()
	PortMM.hide()
	PortDL.hide()
	PortEstate.hide()
	bookOpen1.hide()
	PortBrr.hide()
	PortDG.hide()
	PortSellbot.hide()
	
ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')
terrain = loader.loadModel('phase_15/hood/donalds_dock.bam')
terrain.setPos(475, 510, 500)
terrain.setHpr(180, 0, 0)
terrain.reparentTo(render)
terrain.setTransparency(TransparencyAttrib.MBinary, 1)

#DG Sky
sky = loader.loadModel('phase_3.5/models/props/BR_sky.bam')
sky.setPos(500, 500, 500)
sky.reparentTo(render)



#----------------------Minnie's Melodyland-----------------

def TP4():
	mouseBody.setZ(1000)
	mouseBody.setX(1000)
	mouseBody.setY(1000)
	if sound.status() == sound.PLAYING:
		sound.stop()
	if sound1.status() == sound.PLAYING:
		sound1.stop()
	if sound2.status() == sound2.PLAYING:
		sound2.stop()
	if sound4.status() == sound4.PLAYING:
		sound4.stop()
	if sound5.status() == sound5.PLAYING:
		sound5.stop()
	if sound6.status() == sound6.PLAYING:
		sound6.stop()
		
	if sound7.status() == sound7.PLAYING:
		sound7.stop()
	sound3.setLoop(True)
	sound3.play()
	
	Sticker.show()
	PortTTC.hide()
	Open.hide()
	PortDock.hide()
	PortSpeedway.hide()
	PortMM.hide()
	PortDL.hide()
	PortEstate.hide()
	bookOpen1.hide()
	PortBrr.hide()
	PortDG.hide()
	PortSellbot.hide()
	
	
ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')


#MM Terrain
terrain = loader.loadModel('phase_15/hood/minnies_melody_land.bam')
terrain.setPos(1060, 980, 1000)
terrain.setHpr(-90, 0, 0)
terrain.reparentTo(render)
terrain.setTransparency(TransparencyAttrib.MBinary, 1)

#MM sky
sky = loader.loadModel('phase_6/models/props/MM_sky.bam')
sky.setX(1000)
sky.setY(1000)
sky.setZ(1000)
sky.reparentTo(render)



#----------------------Donald's Dream land---------------------------------------------------------------------------------------------------------

def TP5():
	mouseBody.setZ(-1000)
	mouseBody.setX(-1000)
	mouseBody.setY(-1000)
	if sound.status() == sound.PLAYING:
		sound.stop()
	if sound1.status() == sound.PLAYING:
		sound1.stop()
	if sound2.status() == sound2.PLAYING:
		sound2.stop()
	if sound3.status() == sound3.PLAYING:
		sound3.stop()
	if sound5.status() == sound5.PLAYING:
		sound5.stop()
	if sound6.status() == sound6.PLAYING:
		sound6.stop()
		
	if sound7.status() == sound7.PLAYING:
		sound7.stop()
	sound4.setLoop(True)
	sound4.play()
	
	Sticker.show()
	PortTTC.hide()
	Open.hide()
	PortDock.hide()
	PortSpeedway.hide()
	PortMM.hide()
	PortDL.hide()
	PortEstate.hide()
	bookOpen1.hide()
	PortBrr.hide()
	PortDG.hide()
	PortSellbot.hide()
	
	
ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')

#Donald's Dream land terrain
terrain = loader.loadModel('phase_15/hood/donalds_dreamland.bam')
terrain.setPos(-1000, -1000, -1000)
terrain.setHpr(0, 0, 0)
terrain.reparentTo(render)

sky = loader.loadModel('phase_8/models/props/DL_sky.bam')
sky.setPos(-1000, -1000, -1000)
sky.reparentTo(render)


#---------------------------------------------ESTATE------------------------------------------------------------------------	

def TP6():
	mouseBody.setZ(10002.28882e-005)
	mouseBody.setX(9995.00011)
	mouseBody.setY(9999.999847412)
	if sound.status() == sound.PLAYING:
		sound.stop()
	if sound1.status() == sound.PLAYING:
		sound1.stop()
	if sound2.status() == sound2.PLAYING:
		sound2.stop()
	if sound3.status() == sound3.PLAYING:
		sound3.stop()
	if sound4.status() == sound4.PLAYING:
		sound4.stop()
	if sound6.status() == sound6.PLAYING:
		sound6.stop()
		
	if sound7.status() == sound7.PLAYING:
		sound7.stop()
	sound5.setLoop(True)
	sound5.play()
	
	Sticker.show()
	PortTTC.hide()
	Open.hide()
	PortDock.hide()
	PortSpeedway.hide()
	PortMM.hide()
	PortDL.hide()
	PortEstate.hide()
	bookOpen1.hide()
	PortBrr.hide()
	PortDG.hide()
	PortSellbot.hide()

	
ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')


#Terrain
terrain = loader.loadModel('phase_5.5/models/estate/terrain.bam')
terrain.setPos(9995.00011, 9999.999847412, 10002.28882e-005)
terrain.setHpr(0, 0, 0)
terrain.reparentTo(render)
terrain.setTransparency(TransparencyAttrib.MBinary, 1)
terrain.find('**/terrain').setColor(0.304688, 0.96875, 0.402344, 1.0)

sky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
sky.setPos(9995.00011, 9999.999847412, 10002.28882e-005)
sky.reparentTo(render)


House = loader.loadModel('phase_5.5/models/estate/house.bam')
House.reparentTo(render)
House.setPos(9899.00011, 9930.999847412,  10100.28882e-005)



#-----------------------------------------BRRRGH------------------------------------------------
def TP7():
	mouseBody.setX(500005)
	mouseBody.setY(500005)
	mouseBody.setZ(500005)
	
	if sound.status() == sound.PLAYING:
		sound.stop()
	if sound1.status() == sound.PLAYING:
		sound1.stop()
	if sound2.status() == sound2.PLAYING:
		sound2.stop()
	if sound3.status() == sound3.PLAYING:
		sound3.stop()
	if sound4.status() == sound4.PLAYING:
		sound4.stop()
	if sound6.status() == sound6.PLAYING:
		sound6.stop()
		
	if sound5.status() == sound5.PLAYING:
		sound5.stop()
	sound7.setLoop(True)
	sound7.play()
	
	Sticker.show()
	PortTTC.hide()
	Open.hide()
	PortDock.hide()
	PortSpeedway.hide()
	PortMM.hide()
	PortDL.hide()
	PortEstate.hide()
	bookOpen1.hide()
	PortBrr.hide()
	PortDG.hide()
	PortSellbot.hide()
	
	
terrain = loader.loadModel('phase_15/hood/the_burrrgh.bam')
terrain.setPos(500000, 500000, 500000)
terrain.setHpr(0, 0, 0)
terrain.reparentTo(render)
terrain.setTransparency(TransparencyAttrib.MBinary, 1)

sky = loader.loadModel('phase_3.5/models/props/BR_sky.bam')
sky.setPos(500000, 500000, 500000)
sky.reparentTo(render)



#-------------------------------------Daisy Garden---------------------------------------------
def TP8():
	mouseBody.setX(-500005)
	mouseBody.setY(-500005)
	mouseBody.setZ(-500005)
	
	if sound.status() == sound.PLAYING:
		sound.stop()
	if sound1.status() == sound.PLAYING:
		sound1.stop()
	if sound2.status() == sound2.PLAYING:
		sound2.stop()
	if sound3.status() == sound3.PLAYING:
		sound3.stop()
	if sound4.status() == sound4.PLAYING:
		sound4.stop()
	if sound5.status() == sound6.PLAYING:
		sound5.stop()
		
	if sound7.status() == sound7.PLAYING:
		sound7.stop()
	sound6.setLoop(True)
	sound6.play()
	
	Sticker.show()
	PortTTC.hide()
	Open.hide()
	PortDock.hide()
	PortSpeedway.hide()
	PortMM.hide()
	PortDL.hide()
	PortEstate.hide()
	bookOpen1.hide()
	PortBrr.hide()
	PortDG.hide()
	PortSellbot.hide()

terrain = loader.loadModel('phase_15/hood/daisys_garden.bam')
terrain.setPos(-500000, -500000, -500000)
terrain.setHpr(0, 0, 0)
terrain.reparentTo(render)
terrain.setTransparency(TransparencyAttrib.MBinary, 1)

sky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
sky.setPos(-500000, -500000, -500000)
sky.reparentTo(render)

#-----------------------------------------SellBotHQ------------------------------------------------
def TP9():
	mouseBody.setX(899900)
	mouseBody.setY(899900)
	mouseBody.setZ(899900)
	mouseBody.setHpr(180, 0 ,0)
	
	if sound.status() == sound.PLAYING:
		sound.stop()
	if sound1.status() == sound.PLAYING:
		sound1.stop()
	if sound2.status() == sound2.PLAYING:
		sound2.stop()
	if sound3.status() == sound3.PLAYING:
		sound3.stop()
	if sound4.status() == sound4.PLAYING:
		sound4.stop()
	if sound6.status() == sound6.PLAYING:
		sound6.stop()
		
	if sound5.status() == sound5.PLAYING:
		sound5.stop()
	if sound7.status() == sound7.PLAYING:
		sound7.stop()
	
	Sticker.show()
	PortTTC.hide()
	Open.hide()
	PortDock.hide()
	PortSpeedway.hide()
	PortMM.hide()
	PortDL.hide()
	PortEstate.hide()
	bookOpen1.hide()
	PortBrr.hide()
	PortDG.hide()
	PortSellbot.hide()
	
	
terrain = loader.loadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')
terrain.setPos(900000, 900000, 900000)
terrain.setHpr(0, 0, 0)
terrain.reparentTo(render)

	

#FRIENDS
localAvatar = base.localAvatar

def Friend():
	aFriendsList.show()
	bFriendsList.hide()
	CloseOut.show()
	
def Close():
	bFriendsList.show()
	aFriendsList.hide()
	CloseOut.hide()
	
	
	
friendsGui = loader.loadModel('phase_3.5/models/gui/friendslist_gui.bam')
friendsButtonOpen = friendsGui.find('**/FriendsBox_Open')
friendsButtonNormal = friendsGui.find('**/FriendsBox_Closed')
friendsButtonPressed = friendsGui.find('**/FriendsBox_Rollover')
friendsButtonRollover = friendsGui.find('**/FriendsBox_Rollover')
CloseOut = loader.loadModel('phase_3.5/models/gui/chat_input_gui.bam').find('**/CloseBtn_UP')
CloseOutRllvr = loader.loadModel('phase_3.5/models/gui/chat_input_gui.bam').find('**/CloseBtn_Rllvr')
CloseOutClick = loader.loadModel('phase_3.5/models/gui/chat_input_gui.bam').find('**/CloseBtn_DN')
newScale = oldScale = 0.8
bFriendsList = DirectButton(image=(friendsButtonNormal, friendsButtonPressed, friendsButtonRollover), relief=None, command=Friend, pos=(1.5, 0, 0.875), scale=newScale, text_scale=0.09, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(0, -0.18))
bFriendsList.show()
aFriendsList = OnscreenImage(image = (friendsButtonOpen), pos = (1.5, 0, 0.6), scale=newScale)
aFriendsList.hide()
CloseOut = DirectButton(image=(CloseOut, CloseOutRllvr, CloseOutClick), relief=None, command=Close, pos=(1.512, 0, 0.298), scale=.95, text_scale=0.09, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(0, -0.18))
CloseOut.hide()


#STICKER BOOK 

def OpenBook():
    booksoundOpen = loader.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_open.mp3')
    booksoundOpen.play()
    Sticker.hide()
    Open.show()
    Open.setPos(0, 0, 0)
    Open.setScale(2)
    PortTTC.show()
    PortDock.show()
    PortSpeedway.show()
    PortMM.show()
    PortDL.show()
    PortEstate.show()
    bookOpen1.show()
    PortBrr.show()
    PortDG.show()
    PortSellbot.show()




def CloseBook():
	Open.hide()
	booksoundOpen2 = loader.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_delete.mp3')
	booksoundOpen2.play()
	Sticker.show()
	PortTTC.hide()
	PortDock.hide()
	PortSpeedway.hide()
	PortMM.hide()
	PortDL.hide()
	PortEstate.hide()
	bookOpen1.hide()
	PortBrr.hide()
	PortDG.hide()
	PortSellbot.hide()
	
	
	
book = loader.loadModel('phase_3.5/models/gui/stickerbook_gui.bam')
bookClosed = book.find('**/BookIcon_CLSD')
bookOpen = book.find('**/BookIcon_OPEN')
bookRollover1 = book.find('**/BookIcon_RLVR')
bookRollover2 = book.find('**/BookIcon_RLVR2')
bookOpened = loader.loadModel('phase_3.5/models/gui/toontown_map.bam')
newScale = oldScale = 0.4
Sticker = DirectButton(image=(bookClosed, bookOpen, bookRollover1, bookRollover2), relief=None, command=OpenBook, pos=(1.52, 0, -.825), scale=.3, text_scale=0.09, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(0, -0.18))
Sticker.show()
Open = OnscreenImage(image=(bookOpened), pos=(1.45, 0, -.775), scale=newScale) 
Open.hide()
Cloud = loader.loadModel('phase_3.5/models/gui/cloud.bam')
bookOpen1 = DirectButton(image=(bookOpen, bookRollover2), relief=None, command=CloseBook, pos=(1.52, 0, -.825), scale=.3, text_scale=0.09, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(0, -0.18))
bookOpen1.hide()

ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')
PortTTC = DirectButton(frameSize=None, text='TTC', image=(ButtonImage.find('**/QuitBtn_UP'), ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=TP2, text_pos=(0, -0.015), geom=None, pad=(0.02, 0.02), suppressKeys=0, pos=(0, 0, -.2), text_scale=0.059, borderWidth=(0.13, 0.01), scale=0.7, color=(0, 1, 0))	
PortTTC.hide()

ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')
PortDock = DirectButton(frameSize=None, text='Dock', image=(ButtonImage.find('**/QuitBtn_UP'), ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=TP3, text_pos=(0, -0.015), geom=None, pad=(0.02, 0.02), suppressKeys=0, pos=(.6, 0, -.2), text_scale=0.059, borderWidth=(0.13, 0.01), scale=0.7, color=(0, 1, 0))	
PortDock.hide()

ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')
PortSpeedway = DirectButton(frameSize=None, text='Speedway', image=(ButtonImage.find('**/QuitBtn_UP'), ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=TP1, text_pos=(0, -0.015), geom=None, pad=(0.02, 0.02), suppressKeys=0, pos=(-.5, 0, .0), text_scale=0.059, borderWidth=(0.13, 0.01), scale=0.7, color=(0, 1, 0))	
PortSpeedway.hide()

ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')
PortMM = DirectButton(frameSize=None, text='Melodyland', image=(ButtonImage.find('**/QuitBtn_UP'), ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=TP4, text_pos=(0, -0.015), geom=None, pad=(0.02, 0.02), suppressKeys=0, pos=(.1, 0, .3), text_scale=0.059, borderWidth=(0.13, 0.01), scale=0.7, color=(0, 1, 0))	
PortMM.hide()

ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')
PortDL = DirectButton(frameSize=None, text='Dreamland', image=(ButtonImage.find('**/QuitBtn_UP'), ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=TP5, text_pos=(0, -0.015), geom=None, pad=(0.02, 0.02), suppressKeys=0, pos=(-.1, 0, .7), text_scale=0.059, borderWidth=(0.13, 0.01), scale=0.7, color=(0, 1, 0))	
PortDL.hide()

ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')
PortEstate = DirectButton(frameSize=None, text='Go Home', image=(ButtonImage.find('**/QuitBtn_UP'), ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=TP6, text_pos=(0, -0.015), geom=None, pad=(0.02, 0.02), suppressKeys=0, pos=(.4, 0, -.8), text_scale=0.059, borderWidth=(0.13, 0.01), scale=0.7, color=(0, 1, 0))	
PortEstate.hide()

ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')
PortBrr = DirectButton(frameSize=None, text='The Brrrgh', image=(ButtonImage.find('**/QuitBtn_UP'), ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=TP7, text_pos=(0, -0.015), geom=None, pad=(0.02, 0.02), suppressKeys=0, pos=(.6, 0, .47), text_scale=0.059, borderWidth=(0.13, 0.01), scale=0.7, color=(0, 1, 0))	
PortBrr.hide()

ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')
PortDG = DirectButton(frameSize=None, text='Daisy Garden', image=(ButtonImage.find('**/QuitBtn_UP'), ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=TP8, text_pos=(0, -0.015), geom=None, pad=(0.02, 0.02), suppressKeys=0, pos=(-.4, 0, -.6), text_scale=0.059, borderWidth=(0.13, 0.01), scale=0.7, color=(0, 1, 0))	
PortDG.hide()

ButtonImage = loader.loadModel('phase_3/models/gui/quit_button.bam')
PortSellbot = DirectButton(frameSize=None, text='SellBot HQ', image=(ButtonImage.find('**/QuitBtn_UP'), ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=TP9, text_pos=(0, -0.015), geom=None, pad=(0.02, 0.02), suppressKeys=0, pos=(-.7, 0, -.6), text_scale=0.059, borderWidth=(0.13, 0.01), scale=0.7, color=(0, 1, 0))	
PortSellbot.hide()


#LAFF METER
laff = loader.loadModel('phase_3/models/gui/laff_o_meter.bam')
mousemeter = laff.find('**/mousehead')
mousemeter.setColor(0.347656, 0.820312, 0.953125, 1.0)
smile = laff.find('**/smile')
smile.reparentTo(mousemeter)
eyes = laff.find('**/eyes')
eyes.setColor(1, 1, 1, 1)
eyes.reparentTo(mousemeter)
newScale = oldScale = 0.08

MouseLaff = OnscreenImage(image = (mousemeter), pos = (-1.57, 0, -.85), scale=newScale) #text='15', text_scale=.5, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(-.48, 0.1))
MouseLaff.show()


#Green Chat
dialog = loader.loadModel('phase_3.5/models/gui/chat_input_gui.bam')
chat = dialog.find('**/ChtBx_ChtBtn_DN')
rollover = dialog.find('**/ChtBx_ChtBtn_RLVR')
newScale = oldScale = 1
Speech = DirectButton(image=(rollover, chat), relief=None, pos=(-1.50, 0, .95), scale=newScale, text_scale=.09, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(0, -0.18))
Speech.show()
Speech.setColor(0.242188, 0.742188, 0.515625, 1.0)


#Blue Chat
class ToonTAGS:
 
    def setTalk(self, message):
        if hasattr(self, 'chatbubble'):
            self.chatbubble.removeNode()
        self.chatbubble = loader.loadModel('phase_3/models/props/chatbox.bam')
        self.chatbubble.reparentTo(localAvatar)
        self.chatbubble.setPos(0,0,3.5)
        self.chatbubble.setBillboardAxis(1)
        self.chatbubble.setScale(0.3)
        self.chatbubble.find('**/chatBalloon').setPos(0,0.05,0)
        self.chatbubble.find('**/chatBalloon').setSx(0.8)
        self.talk = OnscreenText(scale=.70,font=loader.loadFont('phase_3/models/fonts/ImpressBT.ttf'),pos=(0.9,3),text=message,wordwrap=10,decal=True,parent=self.chatbubble,align=TextNode.ALeft)
        self.tag.hide()
        Sequence(Wait(5),Func(self.chatbubble.removeNode),Func(self.tag.show)).start()
 
    def toonSound(self, species, type):
        loader.loadSfx("phase_3.5/audio/dial/AV_{0}_{1}".format(species, type)).play()
 
    def sendChat(self, message):
        self.toonSpecies = 'mouse'
 
        try:
            self.setTalk(message)
            if len(message) <= 4:
                if '?' in message:
                    self.toonSound(self.toonSpecies,'question.mp3')
                elif 'ooo' in message:
                    self.toonSound(self.toonSpecies,'howl.mp3')
                elif '!' in message:
                    self.toonSound(self.toonSpecies,'exclaim.mp3')
                else:
                    self.toonSound(self.toonSpecies,'short.mp3')
 
            elif len(message) >= 5 and len(message) <=9:
                if '?' in message:
                    self.toonSound(self.toonSpecies,'question.mp3')
                elif 'ooo' in message:
                    self.toonSound(self.toonSpecies,'howl.mp3')
                elif '!' in message:
                    self.toonSound(self.toonSpecies,'exclaim.mp3')
                else:
                    self.toonSound(self.toonSpecies,'med.mp3')
 
            elif len(message) >= 10:
                if '?' in message:
                    self.toonSound(self.toonSpecies,'question.mp3')
                elif 'ooo' in message:
                    self.toonSound(self.toonSpecies,'howl.mp3')
                elif '!' in message:
                    self.toonSound(self.toonSpecies,'exclaim.mp3')
                else:
                    self.toonSound(self.toonSpecies,'long.mp3')
        except Exception, e:print e#base.localAvatar.ToonTAGS.setName('Sliiy Peppy MacSpeed')
 
    def setName(self, name):
        if hasattr(self, 'tag'):
            self.tag.removeNode()
        self.tag = OnscreenText(scale=.30,font=loader.loadFont('phase_3/models/fonts/ImpressBT.ttf'),pos=(0,3.25),text=name,bg=(.9,.9,.9,.3),fg=(0,0,1,1),wordwrap=7,decal=True,parent=mouseBody)
        self.tag.setBillboardAxis(2)
 
    def __init__(self):
        self.setName('Master Max')

class ClassicChatBox(ToonTAGS):
 
    ChatBox = loader.loadModel("phase_3.5/models/gui/chat_input_gui.bam")
    SlipOpen = loader.loadSfx("phase_3.5/audio/sfx/GUI_quicktalker.mp3")
 
    def __setNone__(self):
 
        text = self.OldChatBoxEntry['text']
        self.OldChatBoxEntry.set(text)
 
        return True
 
    def __action__(self, message):
 
        self.OldChatBoxGui.removeNode()
        self.OldChatBoxEntry.removeNode()
        self.OldChatBoxClose.removeNode()
        self.OldChatBoxBack.removeNode()
        self.OldChatBoxTalk.removeNode()
 
        self.__addOnButton__()
 
        if message != '':
            base.localAvatar.ToonTAGS.sendChat(message)
        else:return None
 
        return True
 
    def __delNavs__(self):
 
        self.OldChatBoxGui.removeNode()
        self.OldChatBoxEntry.removeNode()
        self.OldChatBoxClose.removeNode()
        self.OldChatBoxBack.removeNode()
        self.OldChatBoxTalk.removeNode()
 
        self.__addOnButton__()
 
        return True
 
    def __sayIt__(self):
 
        self.OldChatBoxGui.removeNode()
        self.OldChatBoxEntry.removeNode()
        self.OldChatBoxClose.removeNode()
        self.OldChatBoxBack.removeNode()
        self.OldChatBoxTalk.removeNode()
 
        self.__addOnButton__()
 
        base.localAvatar.ToonTAGS.sendChat(self.OldChatBoxEntry.get(1.0))
 
        return True
 
    def __addNavs__(self):
 
        self.OldChatBoxOpen.removeNode()
        self.OldChatBoxGui = DirectFrame(pos=(-0.4, 0,0.901), scale=1, frameSize=(0,0,0,0), image=self.ChatBox.find("**/quick_talker"))
 
        self.OldChatBoxEntry = DirectEntry(text = "", \
        scale=.04, \
        command=self.__action__, \
        frameSize = (-.0, 32.6, 1, -0.5), \
        frameColor=(0,0,0,0), \
        cursorKeys = 1, \
        initialText = '', \
        numLines = 1, \
        width = 21.5,  \
        focus=1, \
        text_scale=1.5, \
        pos = (-1.05,0,0.900))
 
        self.OldChatBoxBack = DirectButton(frameSize=None, \
        image=(self.ChatBox.find('**/ChtBx_BackBtn_UP'), \
        self.ChatBox.find('**/ChtBx_BackBtn_DN'), \
        self.ChatBox.find('**/ChtBx_BackBtn_Rllvr')), \
        relief=None, \
        command=self.__setNone__, \
        text = ("", "Clear", "Clear", "Clear"), \
        text_pos=(0, -0.09), \
        geom=None, scale=1.1, \
        pad=(0.01, 0.01), \
        suppressKeys=0, \
        pos = (0.305,0,0.912), \
        hpr = (0,0,0), \
        text_scale=0.05, \
        borderWidth=(0.015, 0.01))
 
        self.OldChatBoxClose = DirectButton(frameSize=None, \
        image=(self.ChatBox.find('**/CloseBtn_UP'), \
        self.ChatBox.find('**/CloseBtn_DN'), \
        self.ChatBox.find('**/CloseBtn_Rllvr')), \
        relief=None, \
        command=self.__delNavs__, \
        text = ("", "Cancel", "Cancel", "Cancel"), \
        text_pos=(0, -0.09), \
        geom=None, \
        scale=1.1, \
        pad=(0.01, 0.01), \
        suppressKeys=0, \
        pos = (-1.186,0,0.911), \
        hpr = (0,0,0), \
        text_scale=0.05, \
        borderWidth=(0.015, 0.01))
 
        self.OldChatBoxTalk = DirectButton(frameSize=None, \
        image=(self.ChatBox.find('**/ChtBx_ChtBtn_UP'), \
        self.ChatBox.find('**/ChtBx_ChtBtn_DN'), \
        self.ChatBox.find('**/ChtBx_ChtBtn_RLVR')), \
        relief=None, \
        command=self.__sayIt__, \
        text = ("", "Say It", "Say It", "Say It"), \
        text_pos=(0, -0.09), \
        geom=None, \
        scale=1.1, \
        pad=(0.01, 0.01), \
        suppressKeys=0, \
        pos = (0.4,0,0.912), \
        hpr = (0,0,0), \
        text_scale=0.05, \
        borderWidth=(0.015, 0.01))
 
        return True
 
    def __addOnButton__(self):
 
        self.OldChatBoxOpen = DirectButton(frameSize=None, \
        image=(self.ChatBox.find('**/ChtBx_ChtBtn_UP'), \
        self.ChatBox.find('**/ChtBx_ChtBtn_DN'), \
        self.ChatBox.find('**/ChtBx_ChtBtn_RLVR')), \
        command=self.__addNavs__, \
        relief=None, \
        text = ("", "Chat", "Chat", "Chat"), \
        text_pos=(0, -0.09), \
        clickSound=self.SlipOpen, \
        geom=None, \
        scale=1.2, \
        pad=(0.01, 0.01), \
        suppressKeys=0, \
        pos = (-1.21,0,0.928), \
        hpr = (0,0,0), \
        text_scale=0.059999999999999998, \
        borderWidth=(0.015, 0.01))
 
        return True
 
    def __init__(self):
 
        self.__addOnButton__()
 
class CameraViews:
    def changeView(self):
        if self.objectId != 7:
            base.camera.posHprInterval(0.5, self.posList[self.objectId], self.hprList[self.objectId]).start()
            self.objectId += 1
        else:
            self.objectId = 0
            base.camera.posHprInterval(0.5, self.posList[self.objectId], self.hprList[self.objectId]).start()
            self.objectId += 1
 
    def changeViewRev(self):
        if self.objectId != -1:
            base.camera.posHprInterval(0.5, self.posList[self.objectId], self.hprList[self.objectId]).start()
            self.objectId -= 1
        else:
            self.objectId = 6
            base.camera.posHprInterval(0.5, self.posList[self.objectId], self.hprList[self.objectId]).start()
            self.objectId -= 1
 
    def __init__(self):
        self.objectId = 0
 
        self.posList = [(0,-6,3),
                        (0, 1, 3.5),
                        (8, 15, 5.5),
                        (0, 17, 2.5),
                        (0, -26, 7),
                        (0, -19, 6.5),
                        (0, -13.5, 3.0),
                        (0, -13.5, 3.0)]
 
        self.hprList = [(0,15,0),
                         (0, 0, 0),
                         (150, -5.5, 0),
                         (180, 5.5, 0),
                         (0, -5.5, 0),
                         (0, -8.0, 0),
                         (0, 0, 0),
                         (0, 0, 0)]
 
        base.accept('tab', self.changeView, [])
        base.accept('shift-tab', self.changeViewRev, [])

base.localAvatar.ToonTAGS = ToonTAGS()

base.localAvatar.ClassicChatBox = ClassicChatBox()

base.localAvatar.CameraViews = CameraViews()

localAvatar = mouseBody
base.localAvatar = localAvatar

base.disableMouse()
camera.setPos(0, -10.0 - offset, offset)

#Ice Cream
icecream = loader.loadModel('phase_4/models/props/icecream.bam')
icecream.setPos(33.8931, -135.402, 2.525)
icecream.setHpr(374.329, 0, 0)
icecream.reparentTo(render)

icecream1 = loader.loadModel('phase_4/models/props/icecream.bam')
icecream1.setPos(-73.2766, -71.1291, .025)
icecream1.setHpr(323.033, 0, 0)
icecream1.reparentTo(render)

icecream2 = loader.loadModel('phase_4/models/props/icecream.bam')
icecream2.setPos(-61.2689, -11.6767, 1.22666)
icecream2.setHpr(269.712, 0, 0)
icecream2.reparentTo(render)

icecream3 = loader.loadModel('phase_4/models/props/icecream.bam')
icecream3.setPos(-90.5682, 76.528, .025)
icecream3.setHpr(582.685, 0, 0)
icecream3.reparentTo(render)

icecream4 = loader.loadModel('phase_4/models/props/icecream.bam')
icecream4.setPos(32.6103, 137.525, 2.525)
icecream4.setHpr(525.159, 0, 0)
icecream4.reparentTo(render)

icecream5 = loader.loadModel('phase_4/models/props/icecream.bam')
icecream5.setPos(78.3009, 3.58855, 4.025)
icecream5.setHpr(450.976, 0, 0)
icecream5.reparentTo(render)

#Changes the camera angle
class CameraViews:
    def changeView(self):
        if self.objectId != 7:
            base.camera.posHprInterval(0.5, self.posList[self.objectId], self.hprList[self.objectId]).start()
            self.objectId += 1
        else:
            self.objectId = 0
            base.camera.posHprInterval(0.5, self.posList[self.objectId], self.hprList[self.objectId]).start()
            self.objectId += 1
 
    def changeViewRev(self):
        if self.objectId != -1:
            base.camera.posHprInterval(0.5, self.posList[self.objectId], self.hprList[self.objectId]).start()
            self.objectId -= 1
        else:
            self.objectId = 6
            base.camera.posHprInterval(0.5, self.posList[self.objectId], self.hprList[self.objectId]).start()
            self.objectId -= 1
 
    def __init__(self):
        self.objectId = 0
 
        self.posList = [(0,-6,3),
                        (0, 1, 3.5),
                        (8, 15, 5.5),
                        (0, 17, 2.5),
                        (0, -26, 7),
                        (0, -19, 6.5),
                        (0, -13.5, 3.0),
                        (0, -13.5, 3.0)]
 
        self.hprList = [(0,15,0),
                         (0, 0, 0),
                         (150, -5.5, 0),
                         (180, 5.5, 0),
                         (0, -5.5, 0),
                         (0, -8.0, 0),
                         (0, 0, 0),
                         (0, 0, 0)]
 
        base.accept('tab', self.changeView, [])
        base.accept('shift-tab', self.changeViewRev, [])
        
        
#frame = loader.loadModel('phase_3.5/models/gui/frame.bam')
#row = loader.loadModel('phase_3.5/models/gui/inventory_gui.bam').find('**/InventoryRow')


#Gags = OnscreenImage(image = (frame), pos = (0, 0, 0), scale=.2) #text='15', text_scale=.5, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(-.48, 0.1))
#Gags.hide()
#Row = OnscreenImage(image = (row), pos = (0, 0, 0), scale=.8) #text='15', text_scale=.5, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(-.48, 0.1))
#Row.hide()

#def GagsList():
	#Gags.show()
	
	
	
	
        

run()
