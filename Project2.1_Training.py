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
import os
from direct.gui.DirectGui import *

"""Character customaztion of Big Cheese"""

"""

MAJOR BUGS:
1. Nametag clips thorugh it's background when viewed at an angle
2. Mouse is locked, and may cause issues w/camera and/or GUI

"""


class MyApp(ShowBase):
        def __init__(self):
                ShowBase.__init__(self)
                self.loadModels()
                self.loadCog()
                self.loadCam()
                self.loadGUI()


        #models
        def loadModels(self):
                self.training = self.loader.loadModel('phase_10\models\cogHQ\MidVault.bam')
                self.training.reparentTo(self.render)

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
                self.Cog.setPosHprScale((130, -12.5, 70.75),(65, 0, 0),(1, 1, 1))
                self.Cog.loop('Stand')

        #camera settings        
        def loadCam(self):
                self.disable_mouse()
                self.camera.reparentTo(self.render)
                self.camera.setPosHpr((90, 0, 75), (80, 180, -180))



        #GUI seetings
        def loadGUI(self):

                self.txtb1 = loader.loadModel \
                        ('phase_3\models\props\chatbox.bam')

                self.font1 = loader.loadFont('Impress.egg')
                
                #cog tag
                self.textob = DirectLabel(parent=self.Cog,
                                           text= 'Big Cheese',
                                           pos=(0, 0, 9),
                                           relief=None,
                                           text_scale=(.6),
                                           hpr=(180,0,0),
                                           text_bg = (255, 255, 255, 0.5),
                                           text_font=self.font1,
                                           text_fg=(0,0,0,1)
                                           #text_fg=()
                                           )

                self.textob.component('text0').textNode.setCardDecal(1)
                self.textob['text'] = 'Big Cheese'
                
                #Main GUI panel
                self.guiimage = loader.loadModel('phase_3\models\gui\dialog_box_gui.bam')

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
                                            textMayChange=1)
              #Buttons will be added at a later time
        
app = MyApp()
app.run()
