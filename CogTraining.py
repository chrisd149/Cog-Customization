# Panda3D Imports
from panda3d.core import loadPrcFileData
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
import os
from direct.gui.DirectGui import *
from direct.gui import DirectGuiGlobals as DGG
loadPrcFileData("", "interpolate-frames 1")


"""PLEASE READ: This project was meant to add full customaziton of Big Cheese, but my motovation
has changed.  As a result I will stop adding content to this project soon.  Before so, I will
try to iron out any bugs, but for the most part this project was mainly an attempt to blend
buttons, sounds, sequences, music as a proof of concept for future projects."""


"""Character customaztion of Big Cheese"""

"""
MAJOR BUGS:
1. (FIXED)Nametag clips thorugh it's background when viewed at an angle
2. (Not a problem in testing)Mouse is locked, and may cause issues w/camera and/or GUI
3. (FIXED)Button textures can't be found error
"""

class MyApp(ShowBase):

        def __init__(self):
                ShowBase.__init__(self)
                self.loadModels()
                self.loadCog()
                self.loadCam()
                self.loadGUI()
                self.animations()


        #models
        def loadModels(self):
                self.training = self.loader.loadModel('phase_10\models\cogHQ\MidVault.bam')
                self.training.reparentTo(self.render)

                self.music = loader.loadSfx('phase_3/audio/bgm\create_a_toon.ogg')
                self.music.setVolume(.3)
                self.music.play()

        #cogs
        def loadCog(self):
                self.Cog = Actor('phase_3.5\models\char\suitA-mod.bam',
                                 {'Flail': 'phase_4\models\char\suitA-flailing.bam',
                                  'Stand': 'phase_4\models\char\suitA-neutral.bam',
                                  'Walk': 'phase_4\models\char\suitA-walk.bam',
                                  'Golf': 'phase_5\models\char\suitA-golf-club-swing.bam',
                                  'Victory' : 'phase_4\models\char\suitA-victory.bam'}
                                 )

                self.Cog.reparentTo(self.render)
                self.CogHead = self.loader.loadModel('phase_4\models\char\suitA-heads.bam').find('**/bigcheese')
                self.CogHead.reparentTo(self.Cog.find('**/joint_head'))
                self.Cog.setPosHprScale((130, -12.5, 70.75),(65, 0, 0),(1, 1, 1))
                self.Cog.loop('Stand')


                self.goon = Actor('phase_9\models\char\Cog_Goonie-zero.bam',\
                                  {'Walk' : 'phase_9\models\char\Cog_Goonie-walk.bam'})
                self.goon.reparentTo(self.render)
                self.goon.setPosHprScale((150, -30, 70.65),(180, 0, 0),(2, 2, 2))

        #animations
        def animations(self):
                stand = self.Cog.actorInterval('Stand', duration=15, loop=1)
                victory = self.Cog.actorInterval('Victory', duration=7.5, loop=0)
                scared = self.Cog.actorInterval('Flail', duration=1.5, loop=0)
                walka = self.goon.actorInterval('Walk', duration=6, loop=1)
                walkb = self.goon.actorInterval('Walk', duration=1.5, loop=1)

                walk1 = self.goon.posInterval(6, Point3(150, 12.5, 70.65))
                turn1 = self.goon.hprInterval(1.5, Vec3(0,0,0))
                walk2 = self.goon.posInterval(6, Point3(150, -30, 70.65))
                turn2 = self.goon.hprInterval(1.5, Vec3(180, 0, 0))

                self.pace = Sequence(
                             Parallel(walka, walk1),
                              Parallel(turn1, walkb),
                                Parallel(walk2, walka),
                                  Parallel(walkb, turn2)
                             )
                self.pace.loop()

                self.pace2 = \
                        Sequence(
                                stand, victory, stand, scared
                        )
                self.pace2.loop()

        #camera settings
        def loadCam(self):
                self.disable_mouse()
                self.camera.reparentTo(self.render)
                self.camera.setPosHpr((90, 0, 75), (80, 180, -180))

        #GUI settings
        def loadGUI(self):

                #gui files
                self.txtb1 = self.loader.loadModel \
                        ('phase_3\models\props\chatbox.bam')

                self.font1 = self.loader.loadFont('Impress.egg')

                self.click = self.loader.loadSfx('phase_3/audio\sfx\GUI_create_toon_fwd.ogg')
                self.click.setVolume(.75)

                self.rollover = self.loader.loadSfx('phase_3/audio\sfx\GUI_rollover.ogg')
                self.rollover.setVolume(1)

                self.grunt = self.loader.loadSfx('phase_3.5/audio\dial\COG_VO_grunt.ogg')

                self.img1 = self.loader.loadModel('phase_3\models\gui\ChatPanel.bam')

                self.textob = DirectButton(text= ('Big Cheese', 'Big Cheese', 'Big Cheese', 'Big Cheese'),
                                           parent=aspect2d,
                                           pos=(.485, .45, .475),
                                           relief=None,
                                           text_scale=(.05),
                                           hpr=(0,0,0),
                                           text_bg = (255, 255, 255, 0.5),
                                           text_font=self.font1,
                                           text_fg=(0,0,0,1),
                                           clickSound=self.grunt
                                           )

                self.textob.component('text0').textNode.setCardDecal(1)
                self.textob['text'] = ('Big Cheese', 'Big Cheese', 'Big Cheese', 'Big Cheese')

                self.guiimage = self.loader.loadModel('phase_3\models\gui\dialog_box_gui.bam')

                self.guipanel = DirectLabel(parent=self.Cog,
                                            text= 'Click the arrows to pick your options.',
                                            text_wordwrap = 10,
                                            relief=None,
                                            text_scale=.5,
                                            pos=(8, 10, 8),
                                            hpr=(200, 0, 0),
                                            image=self.guiimage,
                                            image_pos=(2, .3 , -1.25),
                                            image_scale=(10, 5, 5),
                                            textMayChange=1,
                                            text_font=self.font1)



                self.b1 = DirectButton(text=('Next', 'Loading...', 'Go to Next', ''),
                                      text_scale=.05,
                                      text_font=self.font1,
                                      text_pos=(-.05, .125, 1),
                                      pressEffect=1,
                                      geom_scale=(1, 6, 1),
                                      relief=None,
                                      frameColor=(255, 0, 0, 0.8),
                                      clickSound=self.click,
                                      rolloverSound=self.rollover,
                                      textMayChange=1,
                                      image=self.img1,
                                      image_scale=(.25, .09, .09),
                                      image_pos=(-.175, .2, .19),
                                      )


                self.b2 = DirectButton(text=('Back', 'Loading...', 'Go Back', ''),
                                       text_scale=.05,
                                       text_font=self.font1,
                                       text_pos=(-.55, .125, 1),
                                       pressEffect=1,
                                       geom_scale=(1, 6, 1),
                                       relief=None,
                                       frameColor=(255, 0, 0, 0.8),
                                       clickSound=self.click,
                                       rolloverSound=self.rollover,
                                       image=self.img1,
                                       image_scale=(.25, .09, .09),
                                       image_pos=(-.675, .2, .19),
                                       textMayChange=1,
                                       )




app = MyApp()
app.run()
