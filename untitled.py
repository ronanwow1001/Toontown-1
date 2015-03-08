import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.gui.DirectGui import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText



class World(DirectObject):
    def __init__(self):
        self.loadDefaultTerrain()
    def loadDefaultTerrain(self):
        self.terrain = loader.loadModel('phase_4/models/neighborhoods/toontown_central_full.bam')
        self.terrain.reparentTo(render)
    def removeTerrain(self):
        self.terrain.removeNode()


class CTBase(DirectObject):
    def __init__(self):
        world = World()
        self.loadChar()
        self.SetupKeyControl()
    def loadChar(self):

        self.model = Actor(
            {"head":"phase_3/models/char/mouse-heads-1000.bam",
             "torso":"phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000.bam",
             "legs":"phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam"},

            {"torso":{"run":"phase_3/models/char/tt_a_chr_dgm_shorts_torso_run.bam",
                      "neutral":"phase_3/models/char/tt_a_chr_dgm_shorts_torso_neutral.bam"},
             "legs":{"run":"phase_3/models/char/tt_a_chr_dgm_shorts_legs_run.bam",
                     "neutral":"phase_3/models/char/tt_a_chr_dgm_shorts_legs_neutral.bam"}
            })
        self.model.reparentTo(render)

        self.fishingshirt = loader.loadTexture("phase_4/maps/tt_t_chr_avt_shirt_fishing1.jpg")
        self.sleeve = loader.loadTexture("phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing1.jpg")
        self.shorts = loader.loadTexture("phase_3/maps/desat_shorts_10.jpg")

        self.model.attach("head", "torso", "joint_head")
        self.model.attach("torso", "legs", "joint_hips")
        self.model.find('**/arms').setColor(0, 0, 255)
        self.model.find('**/head-short').setColor(0, 255, 255)
        self.model.find('**/neck').setColor(0, 255, 255)
        self.model.find('**/head-front-short').setColor(0, 255, 255)
        self.model.find('**/ears-short').setColor(0, 255, 255)
        self.model.find('**/hands').setColor(255, 255, 255)
        self.model.find('**/legs').setColor(255, 0, 0)
        self.model.find('**/feet').setColor(255, 0, 0)
        self.model.find('**/torso-top').setTexture(self.fishingshirt, 1)
        self.model.find('**/sleeves').setTexture(self.sleeve, 1)
        self.model.find('**/torso-bot').setTexture(self.shorts, 1)
        self.model.setHpr(-90,0,0)
        self.model.find('**/muzzle-short-smile').removeNode()
        self.model.find('**/muzzle-short-surprise').removeNode()
        self.model.find('**/muzzle-short-angry').removeNode()
        self.model.find('**/muzzle-short-laugh').removeNode()
        self.model.find('**/muzzle-short-sad').removeNode()
        self.model.find('**/head-long').removeNode()
        self.model.find('**/head-front-long').removeNode()
        self.model.find('**/eyes-long').removeNode()
        self.model.find('**/ears-long').removeNode()
        self.model.loop('neutral', 'legs')
        self.model.loop('neutral', 'torso')
        base.disableMouse()
        base.camera.setPos(self.model, 0, -8, 4)
        base.camera.setHpr(-90, 0, 0)



    def SetupKeyControl(self):
        self.accept('arrow_up', self.ArrowUpPress)
        self.accept('arrow_up-repeat', self.ArrowUpPress)
        self.accept('arrow_up-up', self.ArrowUpRelease)
        self.accept('arrow_left', self.ArrowLeftPress)
        self.accept('arrow_left-repeat', self.ArrowLeftPress)
        self.accept('arrow_right', self.ArrowRightPress)
        self.accept('arrow_right-repeat', self.ArrowRightPress)
        self.accept('arrow_down', self.ArrowDownPress)
        self.accept('arrow_down-repeat', self.ArrowDownPress)

    def ArrowUpPress(self):
        self.model.setPos(self.model, 0, 1, 0)
        self.animName = self.model.getCurrentAnim()
        base.camera.setPos(self.model, 0, -8, 4)
        if self.animName == "run":
            pass
        else :
            self.model.loop('run', 'legs')
            self.model.loop('run', 'torso')

    def ArrowDownPress(self):
        self.model.setPos(self.model, 0, -.5, 0)
        base.camera.setPos(self.model, 0, -8, 4)

    def ArrowRightPress(self):
        base.camera.setHpr(base.camera,-3, 0, 0)
        self.model.setHpr(self.model, -3, 0, 0)
        base.camera.setPos(self.model, 0, -8, 4)


    def ArrowLeftPress(self):
        base.camera.setHpr(base.camera,3, 0, 0)
        self.model.setHpr(self.model, 3, 0, 0)
        base.camera.setPos(self.model, 0, -8, 4)

    def ArrowUpRelease(self):
        self.model.loop('neutral', 'legs')
        self.model.loop('neutral', 'torso')

Game = CTBase()
run()