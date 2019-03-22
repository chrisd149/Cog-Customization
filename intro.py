# Panda3D Imports
from panda3d.core import loadPrcFile
from direct.actor.Actor import Actor
from pandac.PandaModules import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from pandac.PandaModules import Point3
from pandac.PandaModules import *
from direct.interval.ActorInterval import ActorInterval
from direct.interval.IntervalGlobal import *
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import Filename, AmbientLight, DirectionalLight
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import Vec3, Vec4, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
from direct.gui.DirectGui import *
import os

# scene1
"""Project 2:  Big Cheese's stroll is interrupted by a bug"""

"""Major Bugs:
1. GolfBall will not change startTime to match golf club
2. Explode does not stop looping or slow down
3. (TEMPORARY FIX: Actors moved off screen.) Actors wouldn't be removed.
4. (FIXED: Mouse is now locked.) Camera won't move."""


# these are not all the bugs, just the most annoying ones

class MyApp(ShowBase):

        def __init__(self):
                ShowBase.__init__(self)
                self.loadModels();
                self.loadCog()
                self.SetUpCam()
                self.Sounds()

                # intervals
                Drop = self.tnt.posInterval(1.5, Point3(38, 2, 0))
                # Gone2 = self.tnt.posInterval(.001, Point3(0,0,-100))
                Walk1 = self.Cog.posInterval(2.5, Point3(35, 0, 0))
                Turn1 = self.Cog.hprInterval(2.5, Vec3(-45, 0, 0))
                Gone = self.Cog.posInterval(.01, Point3(0, 0, -100))
                Cam = self.camera.posInterval(0.01, Point3(24.75, 49.75, 110))
                Cam2 = self.camera.hprInterval(.001, Vec3(180, -10, 0))
                Destroy = self.explode.posInterval(.001, Point3(38.5, 3, 12))

                Walk = self.Cog.actorInterval('Walk', duration=2.5, loop=1)
                Stand = self.Cog.actorInterval('Stand', duration=5, loop=1)
                Suprise = self.Cog.actorInterval('Flail', duration=1.5, loop=1)
                Golfing = self.Cog.actorInterval('Golf', duration=5, loop=0)
                Stand2 = self.Cog.actorInterval('Stand', duration=2.5, loop=1)
                Stand3 = self.Cog.actorInterval('Stand', duration=1.5, loop=1)

                # sound intervals
                Speak = SoundInterval(
                        self.speak1,
                        duration=1,
                        loop=0,
                        volume=1,
                        startTime=0
                )

                Explode = SoundInterval(
                        self.explosion,
                        duration=3,
                        loop=0,
                        startTime=0,
                        volume=1
                )

                FootSteps = SoundInterval(
                        self.footsteps,
                        duration=2.5,
                        loop=1,
                        startTime=0,
                        volume=.5
                )

                Speak2 = SoundInterval(
                        self.speak2,
                        duration=1,
                        loop=1,
                        startTime=0,
                        volume=1
                )

                """Golfball = SoundInterval(
                        self.golfball,
                        duration=1,
                        loop=0,
                        startTime=0,
                        volume=1
                )"""
                # Sequence
                self.Pace = Sequence(
                        Parallel(Golfing),
                        Parallel(Walk1, Walk, FootSteps),
                        Parallel(Turn1, Walk, FootSteps),
                        Parallel(Drop, Stand2),
                        Parallel(Speak, Stand3),
                        Parallel(Speak2, Suprise),
                        Parallel(Cam2, Cam, Gone, Destroy, Explode)
                )
                self.Pace.start()

                # props
        def loadModels(self):
                self.bbhq = self.loader.loadModel('phase_12\models/bossbotHQ/CogGolfExterior.bam')
                self.bbhq.reparentTo(self.render)
                self.tnt = Actor('phase_5\models\props/tnt-mod.bam',
                                 {'Explode': 'phase_3.5\models\props\explosion.bam'})

                self.tnt.reparentTo(self.render)
                self.tnt.setPosHpr((38, 3, 100), (0, 0, 0))

                self.explode = Actor('phase_3.5\models\props\explosion.bam')
                self.explode.reparentTo(self.render)
                self.explode.setPosHprScale((38, 3, 100), (120, 0, 0), (2, 2, 2))

                #cogs
        def loadCog(self):
                self.Cog = Actor('phase_3.5\models\char\suitA-mod.bam',
                                 {'Flail': 'phase_4\models\char\suitA-flailing.bam',
                                  'Stand': 'phase_4\models\char\suitA-neutral.bam',
                                  'Walk': 'phase_4\models\char\suitA-walk.bam',
                                  'Golf': 'phase_5\models\char\suitA-golf-club-swing.bam'}
                                 )

                self.Cog.reparentTo(self.render)
                self.CogHead = self.loader.loadModel('phase_4\models\char\suitA-heads.bam').find('**/bigcheese')
                self.CogHead.reparentTo(self.Cog.find('**/joint_head'))
                self.Club = self.loader.loadModel('phase_5/models/props/golf-club.bam')
                self.Club.reparentTo(self.Cog.find('**/joint_Lhold'))
                self.Club.setPosHprScale((-.4, .7, -.35), (-270, 120, -15), (1, 1., 1.5))
                self.Hat = self.loader.loadModel('phase_5\models\props\hat.bam')
                self.Hat.reparentTo(self.CogHead)
                self.Hat.setPosHprScale((0, -.1, 1.90), (0, 20, -70), (1, 1, 1))

                # Cog Setting / Size
                self.Cog.setPosHprScale((25, 0, 0), (-90, 0, 0), (1, 1, 1))

                # sounds
        def Sounds(self):
                self.speak1 = self.loader.loadSfx('phase_3.5/audio\dial\COG_VO_question.ogg')

                self.speak2 = self.loader.loadSfx('phase_3.5/audio\dial\COG_VO_grunt.ogg')

                self.explosion = self.loader.loadSfx('phase_3.5/audio\sfx/ENC_cogfall_apart.ogg')

                self.footsteps = self.loader.loadSfx('phase_3.5/audio\sfx/AV_footstep_walkloop.ogg')

                self.golfball = self.loader.loadSfx('phase_6/audio\sfx\Golf_Hit_Ball.ogg')

                # camera settings
        def SetUpCam(self):
                self.disable_mouse()
                self.camera.reparentTo(self.Cog)
                self.camera.setPosHpr((0, 25, 10), (180, -10, 0))


# frame interpolation
loadPrcFileData("", "interpolate-frames 1")

app = MyApp()
app.run()