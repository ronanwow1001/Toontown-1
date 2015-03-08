from pandac.PandaModules import *
import __builtin__
import os
import sys
import time
import string
from direct.showbase.MessengerGlobal import *
from direct.showbase.DirectObject import DirectObject
from direct.showbase.EventManagerGlobal import *
from direct.task.MiniTask import MiniTask, MiniTaskManager
from direct.directnotify.DirectNotifyGlobal import *
from direct.showbase import *
import direct.directbase.DirectStart
from panda3d.core import *
from direct.task import Task
from direct.actor.Actor import Actor

base.setFrameRateMeter(True)

def destroy():
	base.destroy()
base.accept("escape", destroy)

run()
