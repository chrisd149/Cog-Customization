# Panda3D Imports
from panda3d.core import loadPrcFileData
from panda3d.core import loadPrcFile
loadPrcFileData("", "win-title TITLE GOES HERE")
from direct.actor.Actor import Actor
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from pandac.PandaModules import *
from direct.interval.ActorInterval import ActorInterval
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import WindowProperties
loadPrcFileData("", "window-title Cog Training v0.3-alpha")
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
import datetime

""""""

"""Character customization of Big Cheese"""

"""
MAJOR BUGS:
1. Text Box doesnt change text of other objects
"""



class MyApp(ShowBase):

        def __init__(self):
                ShowBase.__init__(self)
                self.loadModels()
                self.loadCog()
                self.loadCam()
                self.loadGUI()
                self.animations()
                self.music()

        # models
        def loadModels(self):
                self.training = self.loader.loadModel('phase_10\models\cogHQ\MidVault.bam')
                self.training.reparentTo(self.render)

                self.desk = self.loader.loadModel('phase_3.5\models\modules\desk_only_wo_phone.bam')
                self.desk.reparentTo(self.render)
                self.desk.setPosHprScale((130, 7.5, 70.75), (120, 0, 0), (1.5, 1.5, 1.5))

                self.chair = self.loader.loadModel('phase_5.5\models\estate\deskChair.bam')
                self.chair.reparentTo(self.render)
                self.chair.setPosHprScale((135, 7, 70.75), (-60, 0, 0), (1.5, 1.5, 1.5))

        # music
        def music(self):
            self.music = self.loader.loadSfx('phase_3/audio/bgm\create_a_toon.ogg')
            self.music.setVolume(.3)
            self.music.play()

        # cogs/goons/bosses
        def loadCog(self):
                # cog_1
                self.cog_1 = Actor('phase_3.5\models\char\suitA-mod.bam',
                                 {'Flail': 'phase_4\models\char\suitA-flailing.bam',
                                  'Stand': 'phase_4\models\char\suitA-neutral.bam',
                                  'Walk': 'phase_4\models\char\suitA-walk.bam',
                                  'Golf': 'phase_5\models\char\suitA-golf-club-swing.bam',
                                  'Victory': 'phase_4\models\char\suitA-victory.bam'}
                                 )
                self.cog_1.loop('Stand')
                self.cog_1.reparentTo(self.render)
                self.cog_1.setBlend(frameBlend=True)

                # cog head
                self.coghead_1 = self.loader.loadModel('phase_4\models\char\suitA-heads.bam').find('**/bigcheese')
                self.coghead_1.reparentTo(self.cog_1.find('**/joint_head'))
                self.coghead_1.setPos(0, 0, -.05)

                # textures
                self.cogtorso_1 = self.loader.loadTexture('phase_3.5\maps\c_blazer.jpg')
                self.cog_1.find('**/torso').setTexture(self.cogtorso_1, 1)

                #cog position/hpr/scale
                self.cog_1.setPosHprScale((130, -12.5, 70.75), (65, 0, 0), (1, 1, 1))

                #cog hat
                self.hat1 = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_hat_fez.bam')
                self.hat1.reparentTo(self.coghead_1)
                self.hat1.setPosHprScale((0, -0.1, 1.5), (30, -10, 0), (.4, .4, .4))


                # cog_2
                self.cog_2 = Actor('phase_3.5\models\char\suitC-mod.bam',
                                  {'Sit': 'phase_11\models\char\suitC-sit.bam'})
                self.cog_2.loop('Sit')
                self.cog_2.reparentTo(self.chair)
                self.cog_2.setBlend(frameBlend=True)

                # cog position/hpr/scale
                self.cog_2.setPosHprScale((0, -2, 0), (180, 0, 0), (.8, .8, .8))


                # cog head
                self.coghead_2 = self.loader.loadModel('phase_3.5\models\char\suitC-heads.bam').find('**/coldcaller')
                self.coghead_2.reparentTo(self.cog_2.find('**/joint_head'))
                self.coghead_2.setPos(0, 0, -.05)

                #cog hat
                self.hat2 = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_hat_fedora.bam')
                self.hat2.reparentTo(self.coghead_2)
                self.hat2.setPosHprScale((0, 0, .9), (0, 0, 0), (.5, .5, .5))


                # goon
                self.goon = Actor('phase_9\models\char\Cog_Goonie-zero.bam', \
                                  {'Walk': 'phase_9\models\char\Cog_Goonie-walk.bam'})
                self.goon.reparentTo(self.render)
                self.goon.setBlend(frameBlend=True)

                # goon position/hpr/scale
                self.goon.setPosHprScale((150, -30, 70.65), (180, 0, 0), (2, 2, 2))

        # animations
        def animations(self):
                #actor intervals
                stand = self.cog_1.actorInterval('Stand', duration=7.5, loop=1)
                victory = self.cog_1.actorInterval('Victory', duration=7.5, loop=0)
                scared = self.cog_1.actorInterval('Flail', duration=1.5, loop=0)

                walk_1 = self.goon.actorInterval('Walk', duration=6, loop=1)
                walk_2 = self.goon.actorInterval('Walk', duration=1.5, loop=1)

                sit = self.cog_2.actorInterval('Sit', duration=10, loop=1)

                #goon hpr/pos intervals
                move_1 = self.goon.posInterval(6, Point3(150, 12.5, 70.65))
                turn_1 = self.goon.hprInterval(1.5, Vec3(0, 0, 0))
                move_2 = self.goon.posInterval(6, Point3(150, -30, 70.65))
                turn_2 = self.goon.hprInterval(1.5, Vec3(180, 0, 0))

                #head hpr intervals
                head_1_1 = self.coghead_1.hprInterval(2.5, Vec3(30, 10, 0))
                head_2_1 = self.coghead_1.hprInterval(2.5, Vec3(0, 0, 0))
                head_3_1 = self.coghead_1.hprInterval(2.5, Vec3(-30, 20, 0))
                head_4_1 = self.coghead_1.hprInterval(2.5, Vec3(-0, 0, 0))

                #head hpr intervals
                head_1_2 = self.coghead_2.hprInterval(2.5, Vec3(15, 10, 0))
                head_2_2 = self.coghead_2.hprInterval(2.5, Vec3(0, 0, 0))
                head_3_2 = self.coghead_2.hprInterval(2.5, Vec3(-15, 10, 5))
                head_4_2 = self.coghead_2.hprInterval(2.5, Vec3(-0, 0, 0))

                # sequences

                # goon sequence
                pace_1 = Sequence(
                        Parallel(walk_1, move_1),
                        Parallel(turn_1, walk_2),
                        Parallel(move_2, walk_1),
                        Parallel(walk_2, turn_2)
                )
                pace_1.loop()

                # cog_1 sequence
                pace_2 = Sequence(
                        stand,
                        Parallel(stand, head_1_1),
                        Parallel(stand, head_2_1),
                        scared,
                        Parallel(stand, head_3_1),
                        Parallel(stand, head_4_1),
                        victory, stand,
                )
                pace_2.loop()

                # cog_2 sequence
                pace_3 = Sequence(
                        sit,
                        Parallel(sit, head_1_2),
                        Parallel(sit, head_2_2),
                        Parallel(sit, head_3_2),
                        Parallel(sit, head_4_2)
                )
                pace_3.loop()


        # camera settings
        def loadCam(self):
                self.disable_mouse()
                self.camera.reparentTo(self.render)
                self.camera.setPosHpr((90, 0, 75), (80, 180, -180))


        # GUI settings
        def loadGUI(self):
                # gui audio & images
                self.chatbox = self.loader.loadModel \
                        ('phase_3\models\props\chatbox.bam')

                self.font_1 = self.loader.loadFont('Impress.ttf')

                self.click = self.loader.loadSfx('phase_3/audio\sfx\GUI_create_toon_fwd.ogg')
                self.click.setVolume(.75)

                self.rollover = self.loader.loadSfx('phase_3/audio\sfx\GUI_rollover.ogg')
                self.rollover.setVolume(1)

                self.grunt = self.loader.loadSfx('phase_3.5/audio\dial\COG_VO_grunt.ogg')

                self.img_1 = self.loader.loadModel('phase_3\models\gui\ChatPanel.bam')

                self.guiimage = self.loader.loadModel('phase_3\models\gui\dialog_box_gui.bam')

                self.date = datetime.datetime.now()

                self.time_now = self.date.strftime('%H:%M')

                # general information


                self.screentext_1 = OnscreenText(text='Author: Christian Diaz',
                                                 pos=(-1.8, .95),
                                                 font=self.font_1,
                                                 fg=(255, 255, 255, 1),
                                                 scale=.05,
                                                 align=TextNode.A_left,
                                                 )

                self.screentext_2 = OnscreenText(text='Engine Build: Panda3D 1.10.2',
                                                 pos=(-1.8, .875),
                                                 font=self.font_1,
                                                 fg=(255, 255, 255, 1),
                                                 scale=.05,
                                                 align=TextNode.A_left,
                                                 )

                self.screentext_3 =  OnscreenText(text='Current Version: v0.3-alpha',
                                                 pos=(-1.8, .8),
                                                 font=self.font_1,
                                                 fg=(255, 255, 255, 1),
                                                 scale=.05,
                                                 align=TextNode.A_left,
                                                 )

                self.screentext_4 = OnscreenText(text='Current Time: ',
                                                 pos=(-1.8, .65),
                                                 font=self.font_1,
                                                 fg=(255, 255, 255, 1),
                                                 scale=.05,
                                                 align=TextNode.A_left,
                                                 )

                self.screentext_5 = OnscreenText(text=(str(self.time_now)),
                                                 pos=(-1.5, .65),
                                                 font=self.font_1,
                                                 fg=(255, 255, 255, 1),
                                                 scale=.05,
                                                 align=TextNode.A_left,
                                                 )

                self.screentext_6 = OnscreenText(text='Contact: christianmigueldiaz@gmail.com',
                                                 pos=(-1.8, .725),
                                                 font=self.font_1,
                                                 fg=(255, 255, 255, 1),
                                                 scale=.05,
                                                 align=TextNode.A_left,
                                                 )

                self.info_frame = DirectFrame(frameSize=(-1.9, -.9, .6, 1),
                                              frameColor=(254, 255, 255, 0.1))


                # background of textbox
                self.textbox_bg = DirectLabel(parent=self.cog_1,
                                           text='',
                                           text_wordwrap=10,
                                           relief=None,
                                           text_scale=1,
                                           pos=(-5, 10, 10),
                                           hpr=(190, 0, 0),
                                           image=self.guiimage,
                                           image_pos=(4.25, .3, -1.25),
                                           image_scale=(4.1, 3, 5.5),
                                           textMayChange=1,
                                           text_font=self.font_1)


                # textbox
                self.entry = DirectEntry(text='',
                                         scale=.05,
                                         command=self.textbox_bg.setText(),
                                         initialText='You can type here.  It will not affect anything.',
                                         numLines=10,
                                         focus=1,
                                         focusInCommand=self.textbox_bg.clearText(),
                                         parent=self.aspect2d,
                                         pos=(1.45, .1, .8),
                                         entryFont=self.font_1,
                                         relief=None,
                                         clickSound=self.click,
                                         rolloverSound=self.rollover,
                                         text_align=TextNode.ACenter
                                         )


                # cog_1 tag
                self.cogtag_1 = DirectButton(text='Big Cheese    lvl 12',
                                             text_wordwrap=5,
                                             parent=self.aspect2d,
                                             pos=(.485, .45, .475),
                                             relief=None,
                                             text_scale=.05,
                                             hpr=(0, 0, 0),
                                             text_bg=(255, 255, 255, 0.4),
                                             text_font=self.font_1,
                                             text_fg=(0, 0, 0, 1),
                                             clickSound=self.grunt,
                                             textMayChange=1,
                                             )

                # cog_2 tag
                self.cogtag_2 = DirectButton(text='Cold Caller          lvl 5',
                                            text_wordwrap=8,
                                            parent=self.aspect2d,
                                            pos=(-1.225, .45, .425),
                                            relief=None,
                                            text_scale=(.05),
                                            hpr=(0, 0, 0),
                                            text_bg=(254, 255, 255, 0.4),
                                            text_font=self.font_1,
                                            text_fg=(0, 0, 0, 1),
                                            clickSound=self.grunt,
                                            textMayChange=1,
                                            )

                # main gui panel
                self.guipanel = DirectLabel(parent=self.cog_1,
                                            text='Click the arrows below to pick your options.',
                                            text_wordwrap=10,
                                            relief=None,
                                            text_scale=.5,
                                            pos=(8, 10, 8),
                                            hpr=(200, 0, 0),
                                            image=self.guiimage,
                                            image_pos=(2, .3, -1.25),
                                            image_scale=(10, 5, 5),
                                            textMayChange=1,
                                            text_font=self.font_1)


                # gui buttons
                self.button_1 = DirectButton(text=('Next', 'Loading...', 'Go to Next', ''),
                                       text_scale=.05,
                                       text_font=self.font_1,
                                       text_pos=(-.05, .125, 1),
                                       pressEffect=1,
                                       geom_scale=(1, 6, 1),
                                       relief=None,
                                       frameColor=(255, 0, 0, 0.8),
                                       clickSound=self.click,
                                       rolloverSound=self.rollover,
                                       textMayChange=1,
                                       image=self.img_1,
                                       image_scale=(.25, .09, .09),
                                       image_pos=(-.175, 0, .19)
                                       )

                self.button_2 = DirectButton(text=('Back', 'Loading...', 'Go Back', ''),
                                       text_scale=.05,
                                       text_font=self.font_1,
                                       text_pos=(-.55, .125, 1),
                                       pressEffect=1,
                                       geom_scale=(1, 6, 1),
                                       relief=None,
                                       frameColor=(255, 0, 0, 0.8),
                                       clickSound=self.click,
                                       rolloverSound=self.rollover,
                                       image=self.img_1,
                                       image_scale=(.25, .09, .09),
                                       image_pos=(-.675, .2, .19),
                                       textMayChange=1,
                                       )

        def setText(self, textEntered):
                self.textbox_bg.setText(textEntered)

        def clearText(self):
                self.entry.enterText('')


app = MyApp()
app.run()
