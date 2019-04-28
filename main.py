import time
# start time of main.py
start = time.time()

# Panda3D Imports
from panda3d.core import loadPrcFileData
from panda3d.core import loadPrcFile
from direct.actor.Actor import Actor
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from pandac.PandaModules import *
loadPrcFileData("", "window-title Cog Training v1.1")
loadPrcFileData("", "win-size 1920 1080")
loadPrcFileData("", "show-frame-rate-meter True")
from direct.interval.ActorInterval import ActorInterval
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import WindowProperties
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
import sys
import webbrowser

""""""

"""Character customization of Big Cheese"""

"""
MAJOR BUGS:
None :)
"""


class MyApp(ShowBase):
        def __init__(self):
                ShowBase.__init__(self)
                self.load_models()
                self.load_cog()
                self.load_cam()
                self.load_gui()
                self.animations()
                self.music()
                self.screen_text()
                self.accept('m', self.music.stop)
                self.accept('m-repeat', self.music.play)

                # labels for buttons
                self.hat_button_label = OnscreenText(text='Hats',
                                                     pos=(-.05, .225, 1),
                                                     scale=.05,
                                                     font=self.font_1,
                                                     bg=(0, 255, 0, .1)
                                                     )
                self.scale_button_label = OnscreenText(text='Scale',
                                                       pos=(-.475, .225, 1),
                                                       scale=.05,
                                                       font=self.font_1,
                                                       bg=(255, 0, 255, .1)
                                                       )
                self.color_button_label = OnscreenText(text='Color',
                                                       pos=(-.05, .46, 1),
                                                       scale=.05,
                                                       font=self.font_1,
                                                       bg=(255, 0, 0, .1)
                                                       )
                self.texture_button_label = OnscreenText(text='Texture',
                                                         pos=(-.475, .46, 1),
                                                         scale=.05,
                                                         font=self.font_1,
                                                         bg=(0, 0, 255, .1)
                                                         )

        # music
        def music(self):
                self.music = self.loader.loadSfx('phase_3/audio/bgm\create_a_toon.ogg')
                self.music.setVolume(.3)
                self.music.play()

        # cogs/goons/bosses
        def load_cog(self):
                # cog_1
                self.cog_1 = Actor('phase_3.5\models\char\suitA-mod.bam',
                                   {'Flail': 'phase_4\models\char\suitA-flailing.bam',
                                    'Stand': 'phase_4\models\char\suitA-neutral.bam',
                                    'Walk': 'phase_4\models\char\suitA-walk.bam',
                                    'Golf': 'phase_5\models\char\suitA-golf-club-swing.bam',
                                    'Victory': 'phase_4\models\char\suitA-victory.bam'}
                                   )
                # self.cog_1.loop('Stand')
                self.cog_1.reparentTo(self.render)
                self.cog_1.setBlend(frameBlend=True)

                # cog_1 shadow
                self.cogshadow_1 = self.loader.loadModel('phase_3/models/props/drop_shadow.bam')
                self.cogshadow_1.reparentTo(self.cog_1.find('**/joint_shadow'))
                self.cogshadow_1.setScale(.5)
                self.cogshadow_1.setColor(0, 0, 0, .5)
                self.cogshadow_1.setBin('fixed', 0, 1)

                # cog head
                self.coghead_1 = self.loader.loadModel('phase_4\models\char\suitA-heads.bam').find('**/bigcheese')
                self.coghead_1.reparentTo(self.cog_1.find('**/joint_head'))
                self.coghead_1.setPos(0, 0, -.05)

                # cog_1 hat
                self.hat1 = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_hat_fez.bam')
                self.hat1.reparentTo(self.coghead_1)
                self.hat1.setPosHprScale((0, -0.1, 1.5), (30, -10, 0), (.4, .4, .4))

                # cog position/hpr/scale
                self.cog_1.setPosHprScale((130, -13.5, 70.75), (65, 0, 0), (1, 1, 1))

                # cog_2
                self.cog_2 = Actor('phase_3.5\models\char\suitC-mod.bam',
                                   {'Sit': 'phase_11\models\char\suitC-sit.bam'})
                self.cog_2.loop('Sit')
                self.cog_2.reparentTo(self.chair)
                self.cog_2.setBlend(frameBlend=True)

                # cog_2 head
                self.coghead_2 = self.loader.loadModel('phase_3.5\models\char\suitC-heads.bam').find('**/coldcaller')
                self.coghead_2.reparentTo(self.cog_2.find('**/joint_head'))
                self.coghead_2.setPos(0, 0, -.05)

                # cog_2 textures
                self.cogtorso_2 = self.loader.loadTexture('phase_3.5\maps\s_blazer.jpg')
                self.cog_2.find('**/torso').setTexture(self.cogtorso_2, 1)

                self.cogarms_2 = self.loader.loadTexture('phase_3.5\maps\s_sleeve.jpg')
                self.cog_2.find('**/arms').setTexture(self.cogarms_2, 1)

                self.coglegs_2 = self.loader.loadTexture('phase_3.5\maps\s_leg.jpg')
                self.cog_2.find('**/legs').setTexture(self.coglegs_2, 1)

                # cog_2 hat
                self.hat = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_hat_fedora.bam')
                self.hat.reparentTo(self.coghead_2)
                self.hat.setPosHprScale((0, 0, .9), (0, 0, 0), (.5, .5, .5))

                # cog_2 position/hpr/scale
                self.cog_2.setPosHprScale((0, -2, 0), (180, 0, 0), (.8, .8, .8))

                # goon
                self.goon = Actor('phase_9\models\char\Cog_Goonie-zero.bam',
                                  {'Walk': 'phase_9\models\char\Cog_Goonie-walk.bam'})
                self.goon.reparentTo(self.render)
                self.goon.setBlend(frameBlend=True)

                # goon position/hpr/scale
                self.goon.setPosHprScale((150, -30, 70.65), (180, 0, 0), (2, 2, 2))

        # models
        def load_models(self):
                self.training = self.loader.loadModel('phase_10\models\cogHQ\MidVault.bam')
                self.training.reparentTo(self.render)

                self.desk = self.loader.loadModel('phase_3.5\models\modules\desk_only_wo_phone.bam')
                self.desk.reparentTo(self.render)
                self.desk.setPosHprScale((130, 7.5, 70.75), (120, 0, 0), (1.5, 1.5, 1.5))

                self.chair = self.loader.loadModel('phase_5.5\models\estate\deskChair.bam')
                self.chair.reparentTo(self.render)
                self.chair.setPosHprScale((135, 7, 70.75), (-60, 0, 0), (1.5, 1.5, 1.5))

        # animations
        def animations(self):
                # actor intervals
                stand = self.cog_1.actorInterval('Stand', duration=7.5, loop=1)
                victory = self.cog_1.actorInterval('Victory', duration=7.5, loop=0)
                scared = self.cog_1.actorInterval('Flail', duration=1.5, loop=0)

                walk_1 = self.goon.actorInterval('Walk', duration=6, loop=1)
                walk_2 = self.goon.actorInterval('Walk', duration=1.5, loop=1)

                sit = self.cog_2.actorInterval('Sit', duration=10, loop=1)

                # goon hpr/pos intervals
                move_1 = self.goon.posInterval(6, Point3(150, 12.5, 70.65))
                turn_1 = self.goon.hprInterval(1.5, Vec3(0, 0, 0))
                move_2 = self.goon.posInterval(6, Point3(150, -30, 70.65))
                turn_2 = self.goon.hprInterval(1.5, Vec3(180, 0, 0))

                # head hpr intervals
                head_1_1 = self.coghead_1.hprInterval(2.5, Vec3(30, 10, 0))
                head_2_1 = self.coghead_1.hprInterval(2.5, Vec3(0, 0, 0))
                head_3_1 = self.coghead_1.hprInterval(2.5, Vec3(-30, 20, 0))
                head_4_1 = self.coghead_1.hprInterval(2.5, Vec3(-0, 0, 0))

                # head hpr intervals
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
        def load_cam(self):
                self.disable_mouse()
                self.camera.reparentTo(self.render)
                self.camera.setPosHpr((90, 0, 75), (80, 180, -180))

        def screen_text(self):
                self.screentext_1 = OnscreenText(text='Author: Christian Diaz',
                                                 pos=(-1.75, .95),
                                                 font=self.font_1,
                                                 fg=(255, 255, 255, 1),
                                                 scale=.05,
                                                 align=TextNode.A_left,
                                                 )

                self.screentext_2 = OnscreenText(text='Engine Build: Panda3D 1.10.2',
                                                 pos=(-1.75, .875),
                                                 font=self.font_1,
                                                 fg=(255, 255, 255, 1),
                                                 scale=.05,
                                                 align=TextNode.A_left,
                                                 )

                self.screentext_3 = OnscreenText(text='Current Version: v1.1-beta',
                                                 pos=(-1.75, .8),
                                                 font=self.font_1,
                                                 fg=(255, 255, 255, 1),
                                                 scale=.05,
                                                 align=TextNode.A_left,
                                                 )

                self.screentext_4 = OnscreenText(text='Current Time: ',
                                                 pos=(-1.75, .65),
                                                 font=self.font_1,
                                                 fg=(255, 255, 255, 1),
                                                 scale=.05,
                                                 align=TextNode.A_left,
                                                 )

                self.screentext_5 = OnscreenText(text=(str(self.time_now)),
                                                 pos=(-1.45, .65),
                                                 font=self.font_1,
                                                 fg=(255, 255, 255, 1),
                                                 scale=.05,
                                                 align=TextNode.A_left,
                                                 )

                self.screentext_6 = OnscreenText(text='Contact: christianmigueldiaz@gmail.com',
                                                 pos=(-1.75, .725),
                                                 font=self.font_1,
                                                 fg=(255, 255, 255, 1),
                                                 scale=.05,
                                                 align=TextNode.A_left,
                                                 )

                self.screentext_7 = OnscreenText(text='Contact: christianmigueldiaz@gmail.com',
                                                 pos=(-1.75, .725),
                                                 font=self.font_1,
                                                 fg=(255, 255, 255, 1),
                                                 scale=.05,
                                                 align=TextNode.A_left,
                                                 )

                self.info_frame = DirectFrame(frameSize=(-1.85, -.85, .6, 1),
                                              frameColor=(254, 255, 255, 0.1))

        # GUI settings
        def load_gui(self):
                # gui audio & images files
                self.chat_box = self.loader.loadModel \
                        ('phase_3\models\props\chatbox.bam')

                self.font_1 = self.loader.loadFont('Impress.ttf')
                self.font_2 = self.loader.loadFont('CogFont.ttf')

                self.click = self.loader.loadSfx('phase_3/audio\sfx\GUI_create_toon_fwd.ogg')
                self.click.setVolume(.75)

                self.roll_over = self.loader.loadSfx('phase_3/audio\sfx\GUI_rollover.ogg')
                self.roll_over.setVolume(1)

                self.grunt = self.loader.loadSfx('phase_3.5/audio\dial\COG_VO_grunt.ogg')

                self.img_1 = self.loader.loadModel('phase_3\models\gui\ChatPanel.bam')
                self.img_2 = self.loader.loadModel('phase_3.5\models\gui\QT_buttons.bam')
                self.img_3 = self.loader.loadModel('phase_3.5\models\gui\QT_buttons.bam')

                self.gui_image = self.loader.loadModel('phase_3\models\gui\dialog_box_gui.bam')

                # function for time in hours & seconds
                self.date = datetime.datetime.now()
                self.time_now = self.date.strftime('%H:%M')

                # background of textbox
                self.textbox_bg = DirectLabel(parent=self.aspect2d,
                                              text='',
                                              text_wordwrap=10,
                                              relief=None,
                                              text_scale=1,
                                              pos=(1.525, .1, .4),
                                              hpr=(190, 0, 0),
                                              image=self.gui_image,
                                              image_pos=(.1, .1, .1),
                                              image_scale=(.6, .5, .8),
                                              textMayChange=1,
                                              text_font=self.font_1
                                              )

                # textbox
                self.entry = DirectEntry(text='',
                                         scale=.05,
                                         command=self.setText,
                                         initialText='',
                                         numLines=10,
                                         focus=1,
                                         parent=self.aspect2d,
                                         pos=(1.45, .05, .7),
                                         entryFont=self.font_1,
                                         relief=None,
                                         clickSound=self.click,
                                         rolloverSound=self.roll_over,
                                         text_align=TextNode.ACenter
                                         )

                self.entry_title = OnscreenText(text='Type here, then press Enter to delete the text.',
                                                wordwrap=12,
                                                pos=(1.45, .825, 1),
                                                bg=(255, 255, 0, .25),
                                                scale=.0475,
                                                font=self.font_1
                                                )

                # cog_1 tag
                self.cogtag_1 = DirectButton(text='Big Cheese    lvl 12',
                                             text_wordwrap=7.5,
                                             parent=self.aspect2d,
                                             pos=(.565, .45, .475),
                                             relief=None,
                                             text_scale=.05,
                                             hpr=(0, 0, 0),
                                             text_bg=(255, 255, 255, 0.4),
                                             text_font=self.font_2,
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
                                             text_font=self.font_2,
                                             text_fg=(0, 0, 0, 1),
                                             clickSound=self.grunt,
                                             textMayChange=1,
                                             )


                # main gui panel
                self.guipanel = DirectLabel(parent=self.render,
                                            text_wordwrap=10,
                                            relief=None,
                                            text_scale=.5,
                                            pos=(0, 0, 0),
                                            hpr=(0, 0, 0),
                                            image=self.gui_image,
                                            image_pos=(130, -4, 78),
                                            image_scale=(10, 5, 5),
                                            image_hpr=(85, 0, 0),
                                            textMayChange=1,
                                            text_font=self.font_1
                                            )

                # gui buttons
                self.hat1_button = DirectButton(text=('Fez', 'Loading...', 'Change Hat', ''),
                                                text_scale=.05,
                                                text_font=self.font_1,
                                                text_pos=(-.05, .125, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click,
                                                rolloverSound=self.roll_over,
                                                textMayChange=1,
                                                image=self.img_1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(-.175, 0, .19),
                                                command=self.add_hat1,

                                                )

                self.des_text_button = DirectButton(text=('Delete Top-left text.', 'Loading...',
                                                    'This will delete the top-left text.', ''),
                                                    text_scale=.05,
                                                    text_font=self.font_1,
                                                    text_pos=(-.625, .925),
                                                    pressEffect=1,
                                                    geom_scale=(1, 6, 1),
                                                    relief=None,
                                                    clickSound=self.click,
                                                    rolloverSound=self.roll_over,
                                                    image=self.img_1,
                                                    image_scale=(.65, .09, .09),
                                                    image_pos=(-.95, .2, .975),
                                                    textMayChange=1,
                                                    command=self.screen_text_destroy
                                                    )

                self.normal_cog_button = DirectButton(text=('Normal Cog', 'Loading...', 'Change Size', ''),
                                                      text_scale=.05,
                                                      text_font=self.font_1,
                                                      text_pos=(-.475, .125, 1),
                                                      pressEffect=1,
                                                      geom_scale=(1, 6, 1),
                                                      relief=None,
                                                      clickSound=self.click,
                                                      rolloverSound=self.roll_over,
                                                      textMayChange=1,
                                                      image=self.img_1,
                                                      image_scale=(.25, .09, .09),
                                                      image_pos=(-.6, 0, .19),
                                                      command=self.decrease_scale
                                                      )

                self.white_button = DirectButton(text=('White', 'Loading...', 'Next Color', ''),
                                                 text_scale=.05,
                                                 text_font=self.font_1,
                                                 text_pos=(-.05, .365, 1),
                                                 pressEffect=1,
                                                 geom_scale=(1, 6, 1),
                                                 relief=None,
                                                 clickSound=self.click,
                                                 rolloverSound=self.roll_over,
                                                 textMayChange=1,
                                                 image=self.img_1,
                                                 image_scale=(.25, .09, .09),
                                                 image_pos=(-.175, 0, .425),
                                                 command=self.change_color_purple
                                                 )

                self.exit_popup_button = DirectButton(text=('Exit', 'Loading...', 'Exit App', ''),
                                                      text_scale=.05,
                                                      text_font=self.font_1,
                                                      text_pos=(1.375, -.81, 1),
                                                      pressEffect=1,
                                                      geom_scale=(1, 6, 1),
                                                      relief=None,
                                                      clickSound=self.click,
                                                      rolloverSound=self.roll_over,
                                                      textMayChange=1,
                                                      image=self.img_1,
                                                      image_scale=(.20, .09, .09),
                                                      image_pos=(1.275, 0, -.75),
                                                      command=self.exit_popup
                                                      )

                self.bossbot_button = DirectButton(text=('Bossbot', 'Loading...', 'Change Type', ''),
                                                   text_scale=.05,
                                                   text_font=self.font_1,
                                                   text_pos=(-.475, .3625, .1),
                                                   pressEffect=1,
                                                   geom_scale=(1, 6, 1),
                                                   relief=None,
                                                   clickSound=self.click,
                                                   rolloverSound=self.roll_over,
                                                   textMayChange=1,
                                                   image=self.img_1,
                                                   image_scale=(.25, .09, .09),
                                                   image_pos=(-.6, 0, .425),
                                                   command=self.cash_texture
                                                   )

                self.help_button = DirectButton(geom_scale=(1, 1, 1),
                                                relief=None,
                                                clickSound=self.click,
                                                rolloverSound=self.roll_over,
                                                textMayChange=1,
                                                image=self.img_2,
                                                image_scale=(.1, .1, .1),
                                                image_pos=(-1.1, 0, .5),
                                                command=self.help_box
                                                )

                self.wiki_button = DirectButton(text=('Official Wiki', 'Loading...', 'Go to Wiki', ''),
                                                text_scale=.05,
                                                text_font=self.font_1,
                                                text_pos=(1.375, -.65, -.45),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click,
                                                rolloverSound=self.roll_over,
                                                textMayChange=1,
                                                image=self.img_1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(1.25, 0, -.585),
                                                command=self.github_link
                                                )

        def github_link(self):
                webbrowser.open('http://github.com/chrisd149/Cog-Training/wiki/')

        def setText(self, textEntered):
                self.textbox_bg.setText(textEntered)
                self.textbox_bg.destroy()
                del self.textbox_bg
                self.entry.destroy()
                del self.entry
                self.entry_title.destroy()
                del self.entry_title

        # func to destroy onscreentext objects
        def screen_text_destroy(self):
                self.screentext_1.removeNode()
                del self.screentext_1
                self.screentext_2.removeNode()
                del self.screentext_2
                self.screentext_3.removeNode()
                del self.screentext_3
                self.screentext_4.removeNode()
                del self.screentext_4
                self.screentext_5.removeNode()
                del self.screentext_5
                self.screentext_6.removeNode()
                del self.screentext_6
                self.screentext_7.removeNode()
                del self.screentext_7
                self.info_frame.destroy()
                self.des_text_button.destroy()
                del self.des_text_button

                self.info_button = DirectButton(
                        text=('Add top-left text.', 'Loading...', 'This will add the top-left text.', ''),
                        text_scale=.05,
                        text_font=self.font_1,
                        text_pos=(-1.45, .925),
                        pressEffect=1,
                        geom_scale=(1, 6, 1),
                        relief=None,
                        clickSound=self.click,
                        rolloverSound=self.roll_over,
                        image=self.img_1,
                        image_scale=(.6, .09, .09),
                        image_pos=(-1.75, .2, .975),
                        textMayChange=1,
                        command=self.screen_text_load
                )

        # func to add back Screentext objects
        def screen_text_load(self):
                self.screen_text()
                self.info_button.destroy()
                del self.info_button

        # func to add hat
        def add_hat1(self):
                self.hat1.removeNode()
                del self.hat1
                self.hat2 = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_hat_band.bam')
                self.hat2.setPosHprScale((0, -0.1, 1.5), (180, 0, 0), (.25, .25, .25))
                self.hat2.reparentTo(self.coghead_1)
                self.hat1_button.destroy()
                del self.hat1_button

                self.hat2_button = DirectButton(text=('Grand Band Hat', 'Loading...', 'Change Hat', ''),
                                                text_scale=.05,
                                                text_font=self.font_1,
                                                text_pos=(-.05, .125, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click,
                                                rolloverSound=self.roll_over,
                                                image=self.img_1,
                                                image_scale=(.3, .09, .09),
                                                image_pos=(-.2, 0, .19),
                                                textMayChange=1,
                                                command=self.add_hat2
                                                )

        # func to add hat
        def add_hat2(self):
                self.hat2.removeNode()
                del self.hat2
                self.hat3 = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_hat_cowboyHat.bam')
                self.hat3.reparentTo(self.coghead_1)
                self.hat3.setPosHprScale((0, -0.1, 1.5), (10, 10, 0), (.35, .35, .35))
                self.hat2_button.destroy()
                del self.hat2_button

                self.hat3_button = DirectButton(text=('Cowboy Hat', 'Loading...', 'Change Hat', ''),
                                                text_scale=.05,
                                                text_font=self.font_1,
                                                text_pos=(-.05, .125, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click,
                                                rolloverSound=self.roll_over,
                                                textMayChange=1,
                                                image=self.img_1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(-.175, 0, .19),
                                                command=self.add_hat3
                                                )

        # func to add hat
        def add_hat3(self):
                self.hat3.removeNode()
                del self.hat3
                self.hat1 = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_hat_fez.bam')
                self.hat1.reparentTo(self.coghead_1)
                self.hat1.setPosHprScale((0, -0.1, 1.5), (30, -10, 0), (.4, .4, .4))
                self.hat3_button.destroy()
                del self.hat3_button

                self.hat1_button = DirectButton(text=('Fez Hat', 'Loading...', 'Change Hat', ''),
                                                text_scale=.05,
                                                text_font=self.font_1,
                                                text_pos=(-.05, .125, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click,
                                                rolloverSound=self.roll_over,
                                                textMayChange=1,
                                                image=self.img_1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(-.175, 0, .19),
                                                command=self.add_hat1
                                                )

        # functions that change scale of cog_1
        def decrease_scale(self):

                cog_1_scale1 = self.cog_1.scaleInterval(.25, Point3(.5, .5, .5))
                cogtag_1_scale = self.cogtag_1.scaleInterval(.25, Point3(.5, .5, .5))
                cogtag_1_pos = self.cogtag_1.posInterval(.25, Point3(.565, .45, .05))

                self.normal_cog_button.destroy()
                del self.normal_cog_button

                seq1 = Parallel(cog_1_scale1,
                                cogtag_1_scale,
                                cogtag_1_pos
                                )
                seq1.start()

                self.small_cog_button = DirectButton(text=('Small Cog', 'Loading...', 'Change Size', ''),
                                                     text_scale=.05,
                                                     text_font=self.font_1,
                                                     text_pos=(-.475, .125, 1),
                                                     pressEffect=1,
                                                     geom_scale=(1, 6, 1),
                                                     relief=None,
                                                     clickSound=self.click,
                                                     rolloverSound=self.roll_over,
                                                     textMayChange=1,
                                                     image=self.img_1,
                                                     image_scale=(.25, .09, .09),
                                                     image_pos=(-.6, 0, .19),
                                                     command=self.increase_scale
                                                     )

        def increase_scale(self):
                cog_1_scale2 = self.cog_1.scaleInterval(.25, Point3(1, 1, 1))
                cogtag_1_scale2 = self.cogtag_1.scaleInterval(.25, Point3(1, 1, 1))
                cogtag_1_pos2 = self.cogtag_1.posInterval(.25, Point3(.565, .45, .475))
                self.small_cog_button.destroy()
                del self.small_cog_button

                seq2 = Parallel(cog_1_scale2,
                                cogtag_1_scale2,
                                cogtag_1_pos2,
                                )
                seq2.start()
                self.normal_cog_button = DirectButton(text=('Normal Cog', 'Loading...', 'Change Size', ''),
                                                      text_scale=.05,
                                                      text_font=self.font_1,
                                                      text_pos=(-.475, .125, 1),
                                                      pressEffect=1,
                                                      geom_scale=(1, 6, 1),
                                                      relief=None,
                                                      clickSound=self.click,
                                                      rolloverSound=self.roll_over,
                                                      textMayChange=1,
                                                      image=self.img_1,
                                                      image_scale=(.25, .09, .09),
                                                      image_pos=(-.6, 0, .19),
                                                      command=self.decrease_scale
                                                      )

        # glove color functions
        # purple
        def change_color_purple(self):
                self.cog_1.find("**/hands").setColor(255, 0, 255)
                self.white_button.destroy()
                del self.white_button

                self.purple_button = DirectButton(text=('Purple', 'Loading...', 'Next Color', ''),
                                                  text_scale=.05,
                                                  text_font=self.font_1,
                                                  text_pos=(-.05, .365, 1),
                                                  pressEffect=1,
                                                  geom_scale=(1, 6, 1),
                                                  relief=None,
                                                  clickSound=self.click,
                                                  rolloverSound=self.roll_over,
                                                  textMayChange=1,
                                                  image=self.img_1,
                                                  image_scale=(.25, .09, .09),
                                                  image_pos=(-.175, 0, .425),
                                                  command=self.change_color_yellow
                                                  )

        # yellow
        def change_color_yellow(self):
                self.cog_1.find("**/hands").setColor(255, 255, 0)
                self.purple_button.destroy()
                del self.purple_button

                self.yellow_button = DirectButton(text=('Yellow', 'Loading...', 'Change Color', ''),
                                                  text_scale=.05,
                                                  text_font=self.font_1,
                                                  text_pos=(-.05, .365, 1),
                                                  pressEffect=1,
                                                  geom_scale=(1, 6, 1),
                                                  relief=None,
                                                  clickSound=self.click,
                                                  rolloverSound=self.roll_over,
                                                  textMayChange=1,
                                                  image=self.img_1,
                                                  image_scale=(.25, .09, .09),
                                                  image_pos=(-.175, 0, .425),
                                                  command=self.change_color_cyan
                                                  )

        # cyan
        def change_color_cyan(self):
                self.cog_1.find("**/hands").setColor(0, 255, 255)
                self.yellow_button.destroy()
                del self.yellow_button

                self.cyan_button = DirectButton(text=('Cyan', 'Loading...', 'Change Color', ''),
                                                text_scale=.05,
                                                text_font=self.font_1,
                                                text_pos=(-.05, .365, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click,
                                                rolloverSound=self.roll_over,
                                                textMayChange=1,
                                                image=self.img_1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(-.175, 0, .425),
                                                command=self.change_color_white
                                                )

        # white
        def change_color_white(self):
                self.cog_1.find("**/hands").setColor(255, 255, 255)
                self.cyan_button.destroy()
                del self.cyan_button

                self.white_button = DirectButton(text=('White', 'Loading...', 'Change Color', ''),
                                                 text_scale=.05,
                                                 text_font=self.font_1,
                                                 text_pos=(-.05, .365, 1),
                                                 pressEffect=1,
                                                 geom_scale=(1, 6, 1),
                                                 relief=None,
                                                 clickSound=self.click,
                                                 rolloverSound=self.roll_over,
                                                 textMayChange=1,
                                                 image=self.img_1,
                                                 image_scale=(.25, .09, .09),
                                                 image_pos=(-.175, 0, .425),
                                                 command=self.change_color_purple
                                                 )
        # texture functions
        # cashbot
        def cash_texture(self):
                self.cogtorso_1 = self.loader.loadTexture('phase_3.5\maps\m_blazer.jpg')
                self.cog_1.find('**/torso').setTexture(self.cogtorso_1, 1)

                self.cogarms_1 = self.loader.loadTexture('phase_3.5\maps\m_sleeve.jpg')
                self.cog_1.find('**/arms').setTexture(self.cogarms_1, 1)

                self.coglegs_1 = self.loader.loadTexture('phase_3.5\maps\m_leg.jpg')
                self.cog_1.find('**/legs').setTexture(self.coglegs_1, 1)

                self.bossbot_button.destroy()
                del self.bossbot_button

                self.cashbot_button = DirectButton(text=('Cashbot', 'Loading...', 'Change Type', ''),
                                                   text_scale=.05,
                                                   text_font=self.font_1,
                                                   text_pos=(-.475, .3625, .1),
                                                   pressEffect=1,
                                                   geom_scale=(1, 6, 1),
                                                   relief=None,
                                                   clickSound=self.click,
                                                   rolloverSound=self.roll_over,
                                                   textMayChange=1,
                                                   image=self.img_1,
                                                   image_scale=(.25, .09, .09),
                                                   image_pos=(-.6, 0, .425),
                                                   command=self.law_texture
                                                   )

        # lawbot
        def law_texture(self):
                self.cogtorso_1 = self.loader.loadTexture('phase_3.5\maps\l_blazer.jpg')
                self.cog_1.find('**/torso').setTexture(self.cogtorso_1, 1)

                self.cogarms_1 = self.loader.loadTexture('phase_3.5\maps\l_sleeve.jpg')
                self.cog_1.find('**/arms').setTexture(self.cogarms_1, 1)

                self.coglegs_1 = self.loader.loadTexture('phase_3.5\maps\l_leg.jpg')
                self.cog_1.find('**/legs').setTexture(self.coglegs_1, 1)

                self.cashbot_button.destroy()
                del self.cashbot_button

                self.lawbot_button = DirectButton(text=('Lawbot', 'Loading...', 'Change Type', ''),
                                                  text_scale=.05,
                                                  text_font=self.font_1,
                                                  text_pos=(-.475, .3625, .1),
                                                  pressEffect=1,
                                                  geom_scale=(1, 6, 1),
                                                  relief=None,
                                                  clickSound=self.click,
                                                  rolloverSound=self.roll_over,
                                                  textMayChange=1,
                                                  image=self.img_1,
                                                  image_scale=(.25, .09, .09),
                                                  image_pos=(-.6, 0, .425),
                                                  command=self.sell_texture
                                                  )
        # sellbot
        def sell_texture(self):
                self.cogtorso_1 = self.loader.loadTexture('phase_3.5\maps\s_blazer.jpg')
                self.cog_1.find('**/torso').setTexture(self.cogtorso_1, 1)

                self.cogarms_1 = self.loader.loadTexture('phase_3.5\maps\s_sleeve.jpg')
                self.cog_1.find('**/arms').setTexture(self.cogarms_1, 1)

                self.coglegs_1 = self.loader.loadTexture('phase_3.5\maps\s_leg.jpg')
                self.cog_1.find('**/legs').setTexture(self.coglegs_1, 1)

                self.lawbot_button.destroy()
                del self.lawbot_button

                self.sellbot_button = DirectButton(text=('Sellbot', 'Loading...', 'Change Type', ''),
                                                   text_scale=.05,
                                                   text_font=self.font_1,
                                                   text_pos=(-.475, .3625, .1),
                                                   pressEffect=1,
                                                   geom_scale=(1, 6, 1),
                                                   relief=None,
                                                   clickSound=self.click,
                                                   rolloverSound=self.roll_over,
                                                   textMayChange=1,
                                                   image=self.img_1,
                                                   image_scale=(.25, .09, .09),
                                                   image_pos=(-.6, 0, .425),
                                                   command=self.boss_texture
                                                   )

        # bossbot
        def boss_texture(self):
                self.cogtorso_1 = self.loader.loadTexture('phase_3.5\maps\c_blazer.jpg')
                self.cog_1.find('**/torso').setTexture(self.cogtorso_1, 1)

                self.cogarms_1 = self.loader.loadTexture('phase_3.5\maps\c_sleeve.jpg')
                self.cog_1.find('**/arms').setTexture(self.cogarms_1, 1)

                self.coglegs_1 = self.loader.loadTexture('phase_3.5\maps\c_leg.jpg')
                self.cog_1.find('**/legs').setTexture(self.coglegs_1, 1)

                self.sellbot_button.destroy()
                del self.sellbot_button

                self.bossbot_button = DirectButton(text=('Bossbot', 'Loading...', 'Change Type', ''),
                                                   text_scale=.05,
                                                   text_font=self.font_1,
                                                   text_pos=(-.475, .3625, .1),
                                                   pressEffect=1,
                                                   geom_scale=(1, 6, 1),
                                                   relief=None,
                                                   clickSound=self.click,
                                                   rolloverSound=self.roll_over,
                                                   textMayChange=1,
                                                   image=self.img_1,
                                                   image_scale=(.25, .09, .09),
                                                   image_pos=(-.6, 0, .425),
                                                   command=self.cash_texture
                                                   )

        # help box
        def help_box(self):
                self.help_button.destroy()
                del self.help_button
                self.help_panel = DirectLabel(parent=self.aspect2d,
                                              text='To change the appearance of the Big Cheese, click the buttons '
                                                   'to the left in the box. '
                                                   'Report any bugs to christianmigueldiaz@gmail.com',
                                              text_align=TextNode.A_left,
                                              text_wordwrap=13.25,
                                              relief=None,
                                              text_scale=.04,
                                              text_pos=(.185, .83, .75),
                                              hpr=(0, 0, 0),
                                              image=self.gui_image,
                                              image_pos=(.5, .5, .75),
                                              image_scale=(.7, .5, .3),
                                              image_hpr=(0, 0, 0),
                                              textMayChange=1,
                                              text_font=self.font_1
                                              )

                self.des_help_button = DirectButton(geom_scale=(1, 1, 1),
                                                    parent=self.aspect2d,
                                                    relief=None,
                                                    clickSound=self.click,
                                                    rolloverSound=self.roll_over,
                                                    textMayChange=1,
                                                    image=self.img_3,
                                                    image_scale=(.075, .075, .075),
                                                    image_pos=(.8, 0, .65),
                                                    command=self.destroy_helpbox
                                                    )

        def destroy_helpbox(self):
                self.help_panel.destroy()
                del self.help_panel
                self.des_help_button.destroy()
                del self.des_help_button

                self.help_button = DirectButton(geom_scale=(1, 1, 1),
                                                relief=None,
                                                clickSound=self.click,
                                                rolloverSound=self.roll_over,
                                                textMayChange=1,
                                                image=self.img_2,
                                                image_scale=(.1, .1, .1),
                                                image_pos=(-1.1, 0, .5),
                                                command=self.help_box
                                                )

        # exit function
        def exit_popup(self):
                self.exit_popup_button.destroy()
                del self.exit_popup_button

                self.warning_text = OnscreenText(text='WARNING',
                                                 scale=.25,
                                                 fg=(255, 0, 0, 1),
                                                 bg=(255, 255, 255, .15),
                                                 pos=(0, .625, .5),
                                                 font=self.font_1
                                                 )

                self.exit_panel = DirectLabel(text='This will close the application.  Are you sure you want to exit?',
                                              text_wordwrap=7.5,
                                              text_scale=.175,
                                              text_pos=(-.85, .25, 0.25),
                                              relief=None,
                                              text_fg=(255, 0, 0, 1),
                                              image=self.gui_image,
                                              image_scale=(1.75, 1, 1),
                                              text_align=TextNode.A_left,
                                              text_font=self.font_1
                                              )

                self.exit_button = DirectButton(text=('Yes', 'Closing App', 'Close App', ''),
                                                scale=.1,
                                                relief=None,
                                                text_pos=(5, -1.75, 0),
                                                image=self.img_1,
                                                image_scale=(5, 1, 1.5),
                                                image_pos=(2.5, 0, -.75),
                                                clickSound=self.click,
                                                rolloverSound=self.roll_over,
                                                command=self.exit_app,
                                                text_font=self.font_1
                                                )

                self.exit_back_button = DirectButton(text=('No', 'Loading...', 'Close Pop-up', ''),
                                                     scale=.1,
                                                     relief=None,
                                                     text_pos=(5, -4, 0),
                                                     image=self.img_1,
                                                     image_scale=(5, 1, 1.5),
                                                     image_pos=(2.5, 0, -3),
                                                     clickSound=self.click,
                                                     rolloverSound=self.roll_over,
                                                     command=self.close_exit,
                                                     text_font=self.font_1
                                                     )

        def close_exit(self):
                self.warning_text.destroy()
                del self.warning_text
                self.exit_panel.destroy()
                del self.exit_panel
                self.exit_button.destroy()
                del self.exit_button
                self.exit_back_button.destroy()
                del self.exit_back_button

                self.exit_popup_button = DirectButton(text=('Exit', 'Loading...', 'Exit App', ''),
                                                      text_scale=.05,
                                                      text_font=self.font_1,
                                                      text_pos=(1.375, -.81, 1),
                                                      pressEffect=1,
                                                      geom_scale=(1, 6, 1),
                                                      relief=None,
                                                      clickSound=self.click,
                                                      rolloverSound=self.roll_over,
                                                      textMayChange=1,
                                                      image=self.img_1,
                                                      image_scale=(.25, .09, .09),
                                                      image_pos=(1.25, 0, -.75),
                                                      command=self.exit_popup
                                                      )

        @staticmethod
        def exit_app():
                sys.exit()


class AppInfo:
        # current app information
        def __init__(self, devs, ver, tim):
                self.authors = devs
                self.version = ver
                self.runtime = tim
                self.app_data = 'Authors: {} | ' \
                                'Version: {} | ' \
                                'Script Time: {} seconds'\
                                .format(devs, ver, tim)
                self.total_time = 'Runtime: {} seconds'.format(tim)


# end time of main.py
end = time.time()
elapsed_time = (end - start)

data = AppInfo('Christian Diaz', 'v1.1 Beta', elapsed_time)

print('Thanks for playing!')
print('GitHub Link: https://github.com/chrisd149/Cog-Training')
print(data.app_data)

# creates a game log file if it already isn't made
f = open("game_log.txt", "w+")

f.write(str(data.total_time))

if elapsed_time < 1:
        f.write("   |   The program is running under a second, which is good.")
elif elapsed_time > 1 < 1.5:
        f.write("   |   The program is running slower than normal, but isn't significantly affecting performance.")
elif elapsed_time > 2:
        f.write("   |   The program is running very slow, try restarting your computer to decrease run time.")

app = MyApp()
app.run()


