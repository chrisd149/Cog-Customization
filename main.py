# This is a simple interactive Panda3D project using Python 3.7.2
# This game lets you customize a Big Cheese cog via DirectButtons and functions
# This game uses several assets made by the Disney Interactive Media Group and Toontown Rewritten

# Authors: Christian Diaz
# Engine Build: Panda3D 1.10.2
# Python 3.7.2
# Cog Customization v1.1.1

# start time of main.py
import time
start = time.time()

# Panda3D Imports
from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from panda3d.core import TextNode
from panda3d.core import Vec3
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
import datetime
import sys
import webbrowser
import time

# PrcFileData
loadPrcFileData("", "window-title Cog Training v1.1.2")  # titles the app
loadPrcFileData("", "win-size 1280 720")  # makes the app run in 720p
loadPrcFileData("", "show-frame-rate-meter True")  # displays frame rate


class MyApp(ShowBase):
        def __init__(self):
                ShowBase.__init__(self)
                self.load_models()
                self.load_cog()
                self.load_gui()
                self.animations()
                self.screen_text()

                # labels for buttons
                self.accessories_button_label = OnscreenText(text='Accessories',
                                                             pos=(-.05, .225, 1),
                                                             scale=.05,
                                                             font=self.font1,
                                                             bg=(0, 255, 0, .1)
                                                             )
                self.scale_button_label = OnscreenText(text='Scale',
                                                       pos=(-.475, .225, 1),
                                                       scale=.05,
                                                       font=self.font1,
                                                       bg=(255, 0, 255, .1)
                                                       )
                self.color_button_label = OnscreenText(text='Glove Color',
                                                       pos=(-.05, .46, 1),
                                                       scale=.05,
                                                       font=self.font1,
                                                       bg=(255, 0, 0, .1)
                                                       )
                self.texture_button_label = OnscreenText(text='Texture',
                                                         pos=(-.475, .46, 1),
                                                         scale=.05,
                                                         font=self.font1,
                                                         bg=(0, 0, 255, .1)
                                                         )

                self.music1 = self.loader.loadSfx('phase_3/audio/bgm\create_a_toon.ogg')
                self.music1.setVolume(.3)
                self.music1.play()

                self.accept('m', self.music1.stop)
                self.accept('m-repeat', self.music1.play)

                # camera settings
                self.disable_mouse()
                self.camera.reparentTo(self.render)
                self.camera.setPosHpr((90, 0, 75), (80, 180, -180))

        # cogs/goons/bosses
        def load_cog(self):
                # cog_1 actor
                self.cog1 = Actor('phase_3.5\models\char\suitA-mod.bam',
                                  {'Flail': 'phase_4\models\char\suitA-flailing.bam',
                                   'Stand': 'phase_4\models\char\suitA-neutral.bam',
                                   'Walk': 'phase_4\models\char\suitA-walk.bam',
                                   'Golf': 'phase_5\models\char\suitA-golf-club-swing.bam',
                                   'Victory': 'phase_4\models\char\suitA-victory.bam'}
                                  )

                self.cog1.reparentTo(self.render)
                self.cog1.setBlend(frameBlend=True)  # smooths frames

                # cog_1 shadow
                self.cog_shadow1 = self.loader.loadModel('phase_3/models/props/drop_shadow.bam')
                self.cog_shadow1.reparentTo(self.cog1.find('**/joint_shadow'))
                self.cog_shadow1.setScale(.5)
                self.cog_shadow1.setColor(0, 0, 0, .5)
                self.cog_shadow1.setBin('fixed', 0, 1)

                # cog head
                self.cog_head1 = self.loader.loadModel('phase_4\models\char\suitA-heads.bam').find('**/bigcheese')
                self.cog_head1.reparentTo(self.cog1.find('**/joint_head'))
                self.cog_head1.setPos(0, 0, -.05)

                # cog_1 hat
                self.hat1 = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_hat_fez.bam')
                self.hat1.reparentTo(self.cog_head1)
                self.hat1.setPosHprScale((0, -0.1, 1.5), (30, -10, 0), (.4, .4, .4))

                # cog position/hpr/scale
                self.cog1.setPosHprScale((130, -13.5, 70.75), (65, 0, 0), (1, 1, 1))

                # cog_2 actor
                self.cog2 = Actor('phase_3.5\models\char\suitC-mod.bam',
                                  {'Sit': 'phase_11\models\char\suitC-sit.bam'})
                self.cog2.loop('Sit')
                self.cog2.reparentTo(self.chair)
                self.cog2.setBlend(frameBlend=True)  # smooths frames

                # cog_2 head
                self.cog_head2 = self.loader.loadModel('phase_3.5\models\char\suitC-heads.bam').find('**/coldcaller')
                self.cog_head2.reparentTo(self.cog2.find('**/joint_head'))
                self.cog_head2.setPos(0, 0, -.05)

                # cog_2 textures
                self.cog_torso2 = self.loader.loadTexture('phase_3.5\maps\s_blazer.jpg')
                self.cog2.find('**/torso').setTexture(self.cog_torso2, 1)

                self.cog_arms2 = self.loader.loadTexture('phase_3.5\maps\s_sleeve.jpg')
                self.cog2.find('**/arms').setTexture(self.cog_arms2, 1)

                self.cog_legs2 = self.loader.loadTexture('phase_3.5\maps\s_leg.jpg')
                self.cog2.find('**/legs').setTexture(self.cog_legs2, 1)

                # cog_2 hat
                self.hat = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_hat_fedora.bam')
                self.hat.reparentTo(self.cog_head2)
                self.hat.setPosHprScale((0, 0, .9), (0, 0, 0), (.5, .5, .5))

                # cog_2 position/hpr/scale
                self.cog2.setPosHprScale((0, -2, 0), (180, 0, 0), (.8, .8, .8))

                # goon actor
                self.goon = Actor('phase_9\models\char\Cog_Goonie-zero.bam',
                                  {'Walk': 'phase_9\models\char\Cog_Goonie-walk.bam'})
                self.goon.reparentTo(self.render)
                self.goon.setBlend(frameBlend=True)  # smooths frames

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
                stand = self.cog1.actorInterval('Stand', duration=7.5, loop=1)
                victory = self.cog1.actorInterval('Victory', duration=7.5, loop=0)
                scared = self.cog1.actorInterval('Flail', duration=1.5, loop=0)

                walk_1 = self.goon.actorInterval('Walk', duration=6, loop=1)
                walk_2 = self.goon.actorInterval('Walk', duration=1.5, loop=1)

                sit = self.cog2.actorInterval('Sit', duration=10, loop=1)

                # goon hpr/pos intervals
                move_1 = self.goon.posInterval(6, Point3(150, 12.5, 70.65))
                turn_1 = self.goon.hprInterval(1.5, Vec3(0, 0, 0))
                move_2 = self.goon.posInterval(6, Point3(150, -30, 70.65))
                turn_2 = self.goon.hprInterval(1.5, Vec3(180, 0, 0))

                # head hpr intervals
                head_1_1 = self.cog_head1.hprInterval(2.5, Vec3(30, 10, 0))
                head_2_1 = self.cog_head1.hprInterval(2.5, Vec3(0, 0, 0))
                head_3_1 = self.cog_head1.hprInterval(2.5, Vec3(-30, 20, 0))
                head_4_1 = self.cog_head1.hprInterval(2.5, Vec3(-0, 0, 0))

                # head hpr intervals
                head_1_2 = self.cog_head2.hprInterval(2.5, Vec3(15, 10, 0))
                head_2_2 = self.cog_head2.hprInterval(2.5, Vec3(0, 0, 0))
                head_3_2 = self.cog_head2.hprInterval(2.5, Vec3(-15, 10, 5))
                head_4_2 = self.cog_head2.hprInterval(2.5, Vec3(-0, 0, 0))

                # sequences
                # goon sequence
                pace1 = Sequence(
                        Parallel(walk_1, move_1),
                        Parallel(turn_1, walk_2),
                        Parallel(move_2, walk_1),
                        Parallel(walk_2, turn_2)
                )
                pace1.loop()

                # cog1 sequence
                pace2 = Sequence(
                        stand,
                        Parallel(stand, head_1_1),
                        Parallel(stand, head_2_1),
                        scared,
                        Parallel(stand, head_3_1),
                        Parallel(stand, head_4_1),
                        victory, stand,
                )
                pace2.loop()

                # cog2 sequence
                pace3 = Sequence(
                        sit,
                        Parallel(sit, head_1_2),
                        Parallel(sit, head_2_2),
                        Parallel(sit, head_3_2),
                        Parallel(sit, head_4_2)
                )
                pace3.loop()

        # loads OnscreenText
        def screen_text(self):
                self.screentext1 = OnscreenText(text='Author: Christian Diaz',
                                                pos=(-1.75, .95),
                                                font=self.font1,
                                                fg=(255, 255, 255, 1),
                                                scale=.05,
                                                align=TextNode.A_left,
                                                )

                self.screentext2 = OnscreenText(text='Engine Build: Panda3D 1.10.2',
                                                pos=(-1.75, .875),
                                                font=self.font1,
                                                fg=(255, 255, 255, 1),
                                                scale=.05,
                                                align=TextNode.A_left,
                                                )

                self.screentext3 = OnscreenText(text='Current Version: v1.1.2-beta',
                                                pos=(-1.75, .8),
                                                font=self.font1,
                                                fg=(255, 255, 255, 1),
                                                scale=.05,
                                                align=TextNode.A_left,
                                                )

                self.screentext4 = OnscreenText(text='Current Time: ',
                                                pos=(-1.75, .65),
                                                font=self.font1,
                                                fg=(255, 255, 255, 1),
                                                scale=.05,
                                                align=TextNode.A_left,
                                                )

                self.screentext5 = OnscreenText(text=(str(self.time_now)),
                                                pos=(-1.45, .65),
                                                font=self.font1,
                                                fg=(255, 255, 255, 1),
                                                scale=.05,
                                                align=TextNode.A_left,
                                                )

                self.screentext6 = OnscreenText(text='Contact: christianmigueldiaz@gmail.com',
                                                pos=(-1.75, .725),
                                                font=self.font1,
                                                fg=(255, 255, 255, 1),
                                                scale=.05,
                                                align=TextNode.A_left,
                                                )

                self.screentext7 = OnscreenText(text='Contact: christianmigueldiaz@gmail.com',
                                                pos=(-1.75, .725),
                                                font=self.font1,
                                                fg=(255, 255, 255, 1),
                                                scale=.05,
                                                align=TextNode.A_left,
                                                )

                self.info_frame = DirectFrame(frameSize=(-1.85, -.85, .6, 1),
                                              frameColor=(254, 255, 255, 0.1))

        # gui
        def load_gui(self):
                # gui audio & images files
                self.chat_box = self.loader.loadModel \
                        ('phase_3\models\props\chatbox.bam')

                # fonts
                self.font1 = self.loader.loadFont('Impress.ttf')
                self.font2 = self.loader.loadFont('CogFont.ttf')

                # sound effects
                self.click_sound = self.loader.loadSfx(
                        'phase_3/audio\sfx\GUI_create_toon_fwd.ogg')  # click sound effect
                self.click_sound.setVolume(.75)
                self.rollover_sound = self.loader.loadSfx('phase_3/audio\sfx\GUI_rollover.ogg')  # rollover sound effect
                self.grunt_sound = self.loader.loadSfx(
                        'phase_3.5/audio\dial\COG_VO_grunt.ogg')  # cog grunt sound effect

                self.img1 = self.loader.loadModel('phase_3\models\gui\ChatPanel.bam')  # img used for buttons
                self.img2 = self.loader.loadModel('phase_3.5\models\gui\QT_buttons.bam')  # img used for help box button
                self.gui_image = self.loader.loadModel('phase_3\models\gui\dialog_box_gui.bam')  # img used for gui bg

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
                                              text_font=self.font1
                                              )

                # textbox
                self.entry = DirectEntry(text='',
                                         scale=.05,
                                         command=self.set_text,
                                         initialText='',
                                         numLines=10,
                                         focus=1,
                                         parent=self.aspect2d,
                                         pos=(1.45, .05, .7),
                                         entryFont=self.font1,
                                         relief=None,
                                         clickSound=self.click_sound,
                                         rolloverSound=self.rollover_sound,
                                         text_align=TextNode.ACenter
                                         )

                self.entry_title = OnscreenText(text='Type here, then press Enter to delete the text.',
                                                wordwrap=12,
                                                pos=(1.45, .825, 1),
                                                bg=(255, 255, 0, .25),
                                                scale=.0475,
                                                font=self.font1
                                                )

                # cog1 tag
                self.cog_tag1 = DirectButton(text='Big Cheese    Level 12',
                                             text_wordwrap=7.5,
                                             parent=self.aspect2d,
                                             pos=(.565, .45, .475),
                                             relief=None,
                                             text_scale=.05,
                                             hpr=(0, 0, 0),
                                             text_bg=(255, 255, 255, 0.4),
                                             text_font=self.font2,
                                             text_fg=(0, 0, 0, 1),
                                             clickSound=self.grunt_sound,
                                             textMayChange=1,
                                             )

                # cog2 tag
                self.cog_tag2 = DirectButton(text='Cold Caller          Level 5',
                                             text_wordwrap=8,
                                             parent=self.aspect2d,
                                             pos=(-1.225, .45, .425),
                                             relief=None,
                                             text_scale=(.05),
                                             hpr=(0, 0, 0),
                                             text_bg=(254, 255, 255, 0.4),
                                             text_font=self.font2,
                                             text_fg=(0, 0, 0, 1),
                                             clickSound=self.grunt_sound,
                                             textMayChange=1,
                                             )

                # main gui panel
                self.gui_panel = DirectLabel(parent=self.render,
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
                                             text_font=self.font1
                                             )

                # gui buttons
                self.hat1_button = DirectButton(text=('Fez Hat', 'Loading...', 'Change Hat', ''),
                                                text_scale=.05,
                                                text_font=self.font1,
                                                text_pos=(-.05, .125, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                textMayChange=1,
                                                image=self.img1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(-.175, 0, .19),
                                                command=self.destroy_hat1,

                                                )

                # button that destroys OnScreenText
                self.des_text_button = DirectButton(text=('Delete Top-left text.', 'Loading...',
                                                          'This will delete the top-left text.', ''),
                                                    text_scale=.05,
                                                    text_font=self.font1,
                                                    text_pos=(-.625, .925),
                                                    pressEffect=1,
                                                    geom_scale=(1, 6, 1),
                                                    relief=None,
                                                    clickSound=self.click_sound,
                                                    rolloverSound=self.rollover_sound,
                                                    image=self.img1,
                                                    image_scale=(.65, .09, .09),
                                                    image_pos=(-.95, .2, .975),
                                                    textMayChange=1,
                                                    command=self.screen_text_destroy
                                                    )

                # changes cog1 scale from normal to small
                self.normal_cog_button = DirectButton(text=('Normal Cog', 'Loading...', 'Change Size', ''),
                                                      text_scale=.05,
                                                      text_font=self.font1,
                                                      text_pos=(-.475, .125, 1),
                                                      pressEffect=1,
                                                      geom_scale=(1, 6, 1),
                                                      relief=None,
                                                      clickSound=self.click_sound,
                                                      rolloverSound=self.rollover_sound,
                                                      textMayChange=1,
                                                      image=self.img1,
                                                      image_scale=(.25, .09, .09),
                                                      image_pos=(-.6, 0, .19),
                                                      command=self.small_scale
                                                      )

                # changes cog1 gloves' color from white to purple
                self.white_button = DirectButton(text=('White', 'Loading...', 'Next Color', ''),
                                                 text_scale=.05,
                                                 text_font=self.font1,
                                                 text_pos=(-.05, .365, 1),
                                                 pressEffect=1,
                                                 geom_scale=(1, 6, 1),
                                                 relief=None,
                                                 clickSound=self.click_sound,
                                                 rolloverSound=self.rollover_sound,
                                                 textMayChange=1,
                                                 image=self.img1,
                                                 image_scale=(.25, .09, .09),
                                                 image_pos=(-.175, 0, .425),
                                                 command=self.change_color_purple
                                                 )

                self.bossbot_button = DirectButton(text=('Bossbot', 'Loading...', 'Change Type', ''),
                                                   text_scale=.05,
                                                   text_font=self.font1,
                                                   text_pos=(-.475, .3625, .1),
                                                   pressEffect=1,
                                                   geom_scale=(1, 6, 1),
                                                   relief=None,
                                                   clickSound=self.click_sound,
                                                   rolloverSound=self.rollover_sound,
                                                   textMayChange=1,
                                                   image=self.img1,
                                                   image_scale=(.25, .09, .09),
                                                   image_pos=(-.6, 0, .425),
                                                   command=self.cash_texture
                                                   )

                # opens exit popup
                self.exit_popup_button = DirectButton(text=('Exit', 'Loading...', 'Exit App', ''),
                                                      text_scale=.05,
                                                      text_font=self.font1,
                                                      text_pos=(1.375, -.81, 1),
                                                      pressEffect=1,
                                                      geom_scale=(1, 6, 1),
                                                      relief=None,
                                                      clickSound=self.click_sound,
                                                      rolloverSound=self.rollover_sound,
                                                      textMayChange=1,
                                                      image=self.img1,
                                                      image_scale=(.20, .09, .09),
                                                      image_pos=(1.275, 0, -.75),
                                                      command=self.exit_popup
                                                      )

                # opens help box
                self.help_button = DirectButton(geom_scale=(1, 1, 1),
                                                relief=None,
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                textMayChange=1,
                                                image=self.img2,
                                                image_scale=(.1, .1, .1),
                                                image_pos=(-1.1, 0, .5),
                                                command=self.help_box
                                                )

                # opens the wiki for this project
                self.wiki_button = DirectButton(text=('Official Wiki', 'Loading...', 'Go to Wiki', ''),
                                                text_scale=.05,
                                                text_font=self.font1,
                                                text_pos=(1.375, -.65, -.45),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                textMayChange=1,
                                                image=self.img1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(1.25, 0, -.585),
                                                command=self.github_link
                                                )

        @staticmethod
        def github_link():
                webbrowser.open('http://github.com/chrisd149/Cog-Customization/wiki/help')  # opens the GitHub wiki

        # destroys textbox and entry objects
        def set_text(self, textEntered):
                self.textbox_bg.setText(textEntered)
                self.textbox_bg.destroy()
                del self.textbox_bg
                self.entry.destroy()
                del self.entry
                self.entry_title.destroy()
                del self.entry_title

        # destroys Onscreentext objects
        def screen_text_destroy(self):
                self.screentext1.removeNode()
                del self.screentext1
                self.screentext2.removeNode()
                del self.screentext2
                self.screentext3.removeNode()
                del self.screentext3
                self.screentext4.removeNode()
                del self.screentext4
                self.screentext5.removeNode()
                del self.screentext5
                self.screentext6.removeNode()
                del self.screentext6
                self.screentext7.removeNode()
                del self.screentext7
                self.info_frame.destroy()
                self.des_text_button.destroy()
                del self.des_text_button

                # adds back OnScreenText
                self.info_button = DirectButton(
                        text=('Add top-left text.', 'Loading...', 'This will add the top-left text.', ''),
                        text_scale=.05,
                        text_font=self.font1,
                        text_pos=(-1.45, .925),
                        pressEffect=1,
                        geom_scale=(1, 6, 1),
                        relief=None,
                        clickSound=self.click_sound,
                        rolloverSound=self.rollover_sound,
                        image=self.img1,
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

        # destroys hat1 and adds hat2
        def destroy_hat1(self):
                self.hat1.removeNode()
                del self.hat1
                self.hat1_button.destroy()
                del self.hat1_button

                self.hat2 = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_hat_band.bam')
                self.hat2.setPosHprScale((0, -0.1, 1.5), (180, 0, 0), (.25, .25, .25))
                self.hat2.reparentTo(self.cog_head1)

                self.hat2_button = DirectButton(text=('Grand Band Hat', 'Loading...', 'Change Hat', ''),
                                                text_scale=.05,
                                                text_font=self.font1,
                                                text_pos=(-.05, .125, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                image=self.img1,
                                                image_scale=(.3, .09, .09),
                                                image_pos=(-.2, 0, .19),
                                                textMayChange=1,
                                                command=self.destroy_hat2
                                                )

        # destroys hat2 and adds hat3
        def destroy_hat2(self):
                self.hat2.removeNode()
                del self.hat2
                self.hat2_button.destroy()
                del self.hat2_button

                self.hat3 = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_hat_cowboyHat.bam')
                self.hat3.reparentTo(self.cog_head1)
                self.hat3.setPosHprScale((0, -0.1, 1.5), (10, 10, 0), (.35, .35, .35))

                self.hat3_button = DirectButton(text=('Cowboy Hat', 'Loading...', 'Change Hat', ''),
                                                text_scale=.05,
                                                text_font=self.font1,
                                                text_pos=(-.05, .125, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                textMayChange=1,
                                                image=self.img1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(-.175, 0, .19),
                                                command=self.destroy_hat3
                                                )

        # destroys hat3 and adds hat4
        def destroy_hat3(self):
                self.hat3.removeNode()
                del self.hat3
                self.hat3_button.destroy()
                del self.hat3_button

                self.hat4 = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_msk_dorkGlasses.bam')
                self.hat4.reparentTo(self.cog_head1)
                self.hat4.setPosHprScale((0, -0.1, .65), (180, 10, 0), (.35, .35, .35))

                self.hat4_button = DirectButton(text=('Glasses', 'Loading...', 'Change Hat', ''),
                                                text_scale=.05,
                                                text_font=self.font1,
                                                text_pos=(-.05, .125, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                textMayChange=1,
                                                image=self.img1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(-.175, 0, .19),
                                                command=self.destroy_hat4
                                                )

        # destroys hat4 and adds hat5
        def destroy_hat4(self):
                self.hat4.removeNode()
                del self.hat4
                self.hat4_button.destroy()
                del self.hat4_button

                self.hat5 = self.loader.loadModel('phase_4\models/accessories/ttr_m_chr_acc_msk_moostacheC.bam')
                self.hat5.reparentTo(self.cog_head1)
                self.hat5.setPosHprScale((0, .825, .65), (180, 0, 0), (1, 1, 1))

                self.hat5_button = DirectButton(text=('Moustache', 'Loading...', 'Change Hat', ''),
                                                text_scale=.05,
                                                text_font=self.font1,
                                                text_pos=(-.05, .125, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                textMayChange=1,
                                                image=self.img1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(-.175, 0, .19),
                                                command=self.destroy_hat5
                                                )

        # destroys hat5 and adds hat1
        def destroy_hat5(self):
                self.hat5.removeNode()
                del self.hat5
                self.hat5_button.destroy()
                del self.hat5_button

                self.hat6 = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_hat_dinosaur.bam')
                self.hat6.reparentTo(self.cog_head1)
                self.hat6.setPosHprScale((0, -0.1, 1.25), (180, 0, 0), (.3, .3, .3))

                self.hat6_button = DirectButton(text=('Dinosaur Hat', 'Loading...', 'Change Hat', ''),
                                                text_scale=.05,
                                                text_font=self.font1,
                                                text_pos=(-.05, .125, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                textMayChange=1,
                                                image=self.img1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(-.175, 0, .19),
                                                command=self.destroy_hat6
                                                )

        def destroy_hat6(self):
                self.hat6.removeNode()
                del self.hat6
                self.hat6_button.destroy()
                del self.hat6_button

                self.hat1 = self.loader.loadModel('phase_4\models/accessories/tt_m_chr_avt_acc_hat_fez.bam')
                self.hat1.reparentTo(self.cog_head1)
                self.hat1.setPosHprScale((0, -0.1, 1.5), (30, -10, 0), (.4, .4, .4))

                self.hat1_button = DirectButton(text=('Fez Hat', 'Loading...', 'Change Hat', ''),
                                                text_scale=.05,
                                                text_font=self.font1,
                                                text_pos=(-.05, .125, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                textMayChange=1,
                                                image=self.img1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(-.175, 0, .19),
                                                command=self.destroy_hat1
                                                )

        # shrinks cog to scale .5
        def small_scale(self):
                cog1_scale1 = self.cog1.scaleInterval(.25, Point3(.5, .5, .5))
                cog_tag1_scale1 = self.cog_tag1.scaleInterval(.25, Point3(.5, .5, .5))
                cog_tag1_pos1 = self.cog_tag1.posInterval(.25, Point3(.565, .45, .05))

                self.normal_cog_button.destroy()
                del self.normal_cog_button

                seq1 = Parallel(cog1_scale1,
                                cog_tag1_scale1,
                                cog_tag1_pos1
                                )
                seq1.start()

                self.small_cog_button = DirectButton(text=('Small Cog', 'Loading...', 'Change Size', ''),
                                                     text_scale=.05,
                                                     text_font=self.font1,
                                                     text_pos=(-.475, .125, 1),
                                                     pressEffect=1,
                                                     geom_scale=(1, 6, 1),
                                                     relief=None,
                                                     clickSound=self.click_sound,
                                                     rolloverSound=self.rollover_sound,
                                                     textMayChange=1,
                                                     image=self.img1,
                                                     image_scale=(.25, .09, .09),
                                                     image_pos=(-.6, 0, .19),
                                                     command=self.normal_scale
                                                     )

        # returns scale to normal scale
        def normal_scale(self):
                cog1_scale2 = self.cog1.scaleInterval(.25, Point3(1, 1, 1))
                cog_tag1_scale2 = self.cog_tag1.scaleInterval(.25, Point3(1, 1, 1))
                cog_tag1_pos2 = self.cog_tag1.posInterval(.25, Point3(.565, .45, .475))
                self.small_cog_button.destroy()
                del self.small_cog_button

                seq2 = Parallel(cog1_scale2,
                                cog_tag1_scale2,
                                cog_tag1_pos2,
                                )
                seq2.start()
                self.normal_cog_button = DirectButton(text=('Normal Cog', 'Loading...', 'Change Size', ''),
                                                      text_scale=.05,
                                                      text_font=self.font1,
                                                      text_pos=(-.475, .125, 1),
                                                      pressEffect=1,
                                                      geom_scale=(1, 6, 1),
                                                      relief=None,
                                                      clickSound=self.click_sound,
                                                      rolloverSound=self.rollover_sound,
                                                      textMayChange=1,
                                                      image=self.img1,
                                                      image_scale=(.25, .09, .09),
                                                      image_pos=(-.6, 0, .19),
                                                      command=self.large_scale
                                                      )

        # returns scale to normal scale
        def large_scale(self):
                cog1_scale3 = self.cog1.scaleInterval(.25, Point3(1.5, 1.5, 1.5))
                cog_tag1_scale3 = self.cog_tag1.scaleInterval(.25, Point3(1.5, 1.5, 1.5))
                cog_tag1_pos3 = self.cog_tag1.posInterval(.25, Point3(.565, .45, .9))
                self.normal_cog_button.destroy()
                del self.normal_cog_button

                seq3 = Parallel(cog1_scale3,
                                cog_tag1_scale3,
                                cog_tag1_pos3,
                                )
                seq3.start()

                self.large_cog_button = DirectButton(text=('Large Cog', 'Loading...', 'Change Size', ''),
                                                     text_scale=.05,
                                                     text_font=self.font1,
                                                     text_pos=(-.475, .125, 1),
                                                     pressEffect=1,
                                                     geom_scale=(1, 6, 1),
                                                     relief=None,
                                                     clickSound=self.click_sound,
                                                     rolloverSound=self.rollover_sound,
                                                     textMayChange=1,
                                                     image=self.img1,
                                                     image_scale=(.25, .09, .09),
                                                     image_pos=(-.6, 0, .19),
                                                     command=self.normal_scale2
                                                     )

        # returns scale to normal scale
        def normal_scale2(self):
                cog1_scale4 = self.cog1.scaleInterval(.25, Point3(1, 1, 1))
                cog_tag1_scale4 = self.cog_tag1.scaleInterval(.25, Point3(1, 1, 1))
                cog_tag1_pos4 = self.cog_tag1.posInterval(.25, Point3(.565, .45, .475))
                self.large_cog_button.destroy()
                del self.large_cog_button

                seq4 = Parallel(cog1_scale4,
                                cog_tag1_scale4,
                                cog_tag1_pos4,
                                )
                seq4.start()

                self.normal_cog_button = DirectButton(text=('Normal Cog', 'Loading...', 'Change Size', ''),
                                                      text_scale=.05,
                                                      text_font=self.font1,
                                                      text_pos=(-.475, .125, 1),
                                                      pressEffect=1,
                                                      geom_scale=(1, 6, 1),
                                                      relief=None,
                                                      clickSound=self.click_sound,
                                                      rolloverSound=self.rollover_sound,
                                                      textMayChange=1,
                                                      image=self.img1,
                                                      image_scale=(.25, .09, .09),
                                                      image_pos=(-.6, 0, .19),
                                                      command=self.small_scale
                                                      )


        # glove color functions
        # purple color
        def change_color_purple(self):
                self.cog1.find("**/hands").setColor(255, 0, 255)
                self.white_button.destroy()
                del self.white_button

                self.purple_button = DirectButton(text=('Purple', 'Loading...', 'Next Color', ''),
                                                  text_scale=.05,
                                                  text_font=self.font1,
                                                  text_pos=(-.05, .365, 1),
                                                  pressEffect=1,
                                                  geom_scale=(1, 6, 1),
                                                  relief=None,
                                                  clickSound=self.click_sound,
                                                  rolloverSound=self.rollover_sound,
                                                  textMayChange=1,
                                                  image=self.img1,
                                                  image_scale=(.25, .09, .09),
                                                  image_pos=(-.175, 0, .425),
                                                  command=self.change_color_yellow
                                                  )

        # yellow color
        def change_color_yellow(self):
                self.cog1.find("**/hands").setColor(255, 255, 0)
                self.purple_button.destroy()
                del self.purple_button

                self.yellow_button = DirectButton(text=('Yellow', 'Loading...', 'Change Color', ''),
                                                  text_scale=.05,
                                                  text_font=self.font1,
                                                  text_pos=(-.05, .365, 1),
                                                  pressEffect=1,
                                                  geom_scale=(1, 6, 1),
                                                  relief=None,
                                                  clickSound=self.click_sound,
                                                  rolloverSound=self.rollover_sound,
                                                  textMayChange=1,
                                                  image=self.img1,
                                                  image_scale=(.25, .09, .09),
                                                  image_pos=(-.175, 0, .425),
                                                  command=self.change_color_cyan
                                                  )

        # cyan color
        def change_color_cyan(self):
                self.cog1.find("**/hands").setColor(0, 255, 255)
                self.yellow_button.destroy()
                del self.yellow_button

                self.cyan_button = DirectButton(text=('Cyan', 'Loading...', 'Change Color', ''),
                                                text_scale=.05,
                                                text_font=self.font1,
                                                text_pos=(-.05, .365, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                textMayChange=1,
                                                image=self.img1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(-.175, 0, .425),
                                                command=self.change_color_red
                                                )

        # red color
        def change_color_red(self):
                self.cog1.find("**/hands").setColor(255, 0, 0)
                self.cyan_button.destroy()
                del self.cyan_button

                self.red_button = DirectButton(text=('Red', 'Loading...', 'Change Color', ''),
                                               text_scale=.05,
                                               text_font=self.font1,
                                               text_pos=(-.05, .365, 1),
                                               pressEffect=1,
                                               geom_scale=(1, 6, 1),
                                               relief=None,
                                               clickSound=self.click_sound,
                                               rolloverSound=self.rollover_sound,
                                               textMayChange=1,
                                               image=self.img1,
                                               image_scale=(.25, .09, .09),
                                               image_pos=(-.175, 0, .425),
                                               command=self.change_color_blue
                                               )

        # blue color
        def change_color_blue(self):
                self.cog1.find("**/hands").setColor(0, 0, 255)
                self.red_button.destroy()
                del self.red_button

                self.blue_button = DirectButton(text=('Blue', 'Loading...', 'Change Color', ''),
                                                text_scale=.05,
                                                text_font=self.font1,
                                                text_pos=(-.05, .365, 1),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                textMayChange=1,
                                                image=self.img1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(-.175, 0, .425),
                                                command=self.change_color_green
                                                )

        # green color
        def change_color_green(self):
                self.cog1.find("**/hands").setColor(0, 255, 0)
                self.blue_button.destroy()
                del self.blue_button

                self.green_button = DirectButton(text=('Green', 'Loading...', 'Change Color', ''),
                                                 text_scale=.05,
                                                 text_font=self.font1,
                                                 text_pos=(-.05, .365, 1),
                                                 pressEffect=1,
                                                 geom_scale=(1, 6, 1),
                                                 relief=None,
                                                 clickSound=self.click_sound,
                                                 rolloverSound=self.rollover_sound,
                                                 textMayChange=1,
                                                 image=self.img1,
                                                 image_scale=(.25, .09, .09),
                                                 image_pos=(-.175, 0, .425),
                                                 command=self.change_color_white
                                                 )

        # white color
        def change_color_white(self):
                self.cog1.find("**/hands").setColor(255, 255, 255)
                self.green_button.destroy()
                del self.green_button

                self.white_button = DirectButton(text=('White', 'Loading...', 'Change Color', ''),
                                                 text_scale=.05,
                                                 text_font=self.font1,
                                                 text_pos=(-.05, .365, 1),
                                                 pressEffect=1,
                                                 geom_scale=(1, 6, 1),
                                                 relief=None,
                                                 clickSound=self.click_sound,
                                                 rolloverSound=self.rollover_sound,
                                                 textMayChange=1,
                                                 image=self.img1,
                                                 image_scale=(.25, .09, .09),
                                                 image_pos=(-.175, 0, .425),
                                                 command=self.change_color_purple
                                                 )

        # texture functions
        # cashbot text
        def cash_texture(self):
                # sets cog1 textures to Cashbot
                self.cog_torso1 = self.loader.loadTexture('phase_3.5\maps\m_blazer.jpg')
                self.cog1.find('**/torso').setTexture(self.cog_torso1, 1)

                self.cog_arms1 = self.loader.loadTexture('phase_3.5\maps\m_sleeve.jpg')
                self.cog1.find('**/arms').setTexture(self.cog_arms1, 1)

                self.cog_legs1 = self.loader.loadTexture('phase_3.5\maps\m_leg.jpg')
                self.cog1.find('**/legs').setTexture(self.cog_legs1, 1)

                self.bossbot_button.destroy()
                del self.bossbot_button

                self.cashbot_button = DirectButton(text=('Cashbot', 'Loading...', 'Change Type', ''),
                                                   text_scale=.05,
                                                   text_font=self.font1,
                                                   text_pos=(-.475, .3625, .1),
                                                   pressEffect=1,
                                                   geom_scale=(1, 6, 1),
                                                   relief=None,
                                                   clickSound=self.click_sound,
                                                   rolloverSound=self.rollover_sound,
                                                   textMayChange=1,
                                                   image=self.img1,
                                                   image_scale=(.25, .09, .09),
                                                   image_pos=(-.6, 0, .425),
                                                   command=self.law_texture
                                                   )

        # lawbot text
        def law_texture(self):
                # sets cog1 textures to Lawbot
                self.cog_torso1 = self.loader.loadTexture('phase_3.5\maps\l_blazer.jpg')
                self.cog1.find('**/torso').setTexture(self.cog_torso1, 1)

                self.cog_arms1 = self.loader.loadTexture('phase_3.5\maps\l_sleeve.jpg')
                self.cog1.find('**/arms').setTexture(self.cog_arms1, 1)

                self.cog_legs1 = self.loader.loadTexture('phase_3.5\maps\l_leg.jpg')
                self.cog1.find('**/legs').setTexture(self.cog_legs1, 1)

                self.cashbot_button.destroy()
                del self.cashbot_button

                self.lawbot_button = DirectButton(text=('Lawbot', 'Loading...', 'Change Type', ''),
                                                  text_scale=.05,
                                                  text_font=self.font1,
                                                  text_pos=(-.475, .3625, .1),
                                                  pressEffect=1,
                                                  geom_scale=(1, 6, 1),
                                                  relief=None,
                                                  clickSound=self.click_sound,
                                                  rolloverSound=self.rollover_sound,
                                                  textMayChange=1,
                                                  image=self.img1,
                                                  image_scale=(.25, .09, .09),
                                                  image_pos=(-.6, 0, .425),
                                                  command=self.sell_texture
                                                  )

        # sellbot text
        def sell_texture(self):
                # sets cog1 textures to Sellbot
                self.cog_torso1 = self.loader.loadTexture('phase_3.5\maps\s_blazer.jpg')
                self.cog1.find('**/torso').setTexture(self.cog_torso1, 1)

                self.cog_arms1 = self.loader.loadTexture('phase_3.5\maps\s_sleeve.jpg')
                self.cog1.find('**/arms').setTexture(self.cog_arms1, 1)

                self.cog_legs1 = self.loader.loadTexture('phase_3.5\maps\s_leg.jpg')
                self.cog1.find('**/legs').setTexture(self.cog_legs1, 1)

                self.lawbot_button.destroy()
                del self.lawbot_button

                self.sellbot_button = DirectButton(text=('Sellbot', 'Loading...', 'Change Type', ''),
                                                   text_scale=.05,
                                                   text_font=self.font1,
                                                   text_pos=(-.475, .3625, .1),
                                                   pressEffect=1,
                                                   geom_scale=(1, 6, 1),
                                                   relief=None,
                                                   clickSound=self.click_sound,
                                                   rolloverSound=self.rollover_sound,
                                                   textMayChange=1,
                                                   image=self.img1,
                                                   image_scale=(.25, .09, .09),
                                                   image_pos=(-.6, 0, .425),
                                                   command=self.boss_texture
                                                   )

        # bossbot text
        def boss_texture(self):
                # sets cog1 textures to Bossbot
                self.cog_torso1 = self.loader.loadTexture('phase_3.5\maps\c_blazer.jpg')
                self.cog1.find('**/torso').setTexture(self.cog_torso1, 1)

                self.cog_arms1 = self.loader.loadTexture('phase_3.5\maps\c_sleeve.jpg')
                self.cog1.find('**/arms').setTexture(self.cog_arms1, 1)

                self.cog_legs1 = self.loader.loadTexture('phase_3.5\maps\c_leg.jpg')
                self.cog1.find('**/legs').setTexture(self.cog_legs1, 1)

                self.sellbot_button.destroy()
                del self.sellbot_button

                self.bossbot_button = DirectButton(text=('Bossbot', 'Loading...', 'Change Type', ''),
                                                   text_scale=.05,
                                                   text_font=self.font1,
                                                   text_pos=(-.475, .3625, .1),
                                                   pressEffect=1,
                                                   geom_scale=(1, 6, 1),
                                                   relief=None,
                                                   clickSound=self.click_sound,
                                                   rolloverSound=self.rollover_sound,
                                                   textMayChange=1,
                                                   image=self.img1,
                                                   image_scale=(.25, .09, .09),
                                                   image_pos=(-.6, 0, .425),
                                                   command=self.cash_texture
                                                   )

        # spawns the help box
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
                                              text_font=self.font1
                                              )

                self.des_help_button = DirectButton(geom_scale=(1, 1, 1),
                                                    parent=self.aspect2d,
                                                    relief=None,
                                                    clickSound=self.click_sound,
                                                    rolloverSound=self.rollover_sound,
                                                    textMayChange=1,
                                                    image=self.img2,
                                                    image_scale=(.075, .075, .075),
                                                    image_pos=(.8, 0, .65),
                                                    command=self.destroy_help_box
                                                    )

        # destroys the help box
        def destroy_help_box(self):
                self.help_panel.destroy()
                del self.help_panel
                self.des_help_button.destroy()
                del self.des_help_button

                self.help_button = DirectButton(geom_scale=(1, 1, 1),
                                                relief=None,
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                textMayChange=1,
                                                image=self.img2,
                                                image_scale=(.1, .1, .1),
                                                image_pos=(-1.1, 0, .5),
                                                command=self.help_box
                                                )

        # spawns the exit popup
        def exit_popup(self):
                self.exit_popup_button.destroy()
                del self.exit_popup_button

                # title of exit panel text
                self.warning_text = OnscreenText(text='WARNING',
                                                 scale=.25,
                                                 fg=(255, 0, 0, 1),
                                                 bg=(255, 255, 255, .15),
                                                 pos=(0, .625, .5),
                                                 font=self.font1
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
                                              text_font=self.font1
                                              )

                # closes the application
                self.exit_button = DirectButton(text=('Yes', 'Closing App', 'Close App', ''),
                                                scale=.1,
                                                relief=None,
                                                text_pos=(5, -1.75, 0),
                                                image=self.img1,
                                                image_scale=(5, 1, 1.5),
                                                image_pos=(2.5, 0, -.75),
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                command=self.exit_app,
                                                text_font=self.font1
                                                )

                # closes exit pop up
                self.exit_back_button = DirectButton(text=('No', 'Loading...', 'Close Pop-up', ''),
                                                     scale=.1,
                                                     relief=None,
                                                     text_pos=(5, -4, 0),
                                                     image=self.img1,
                                                     image_scale=(5, 1, 1.5),
                                                     image_pos=(2.5, 0, -3),
                                                     clickSound=self.click_sound,
                                                     rolloverSound=self.rollover_sound,
                                                     command=self.destroy_exit_popup,
                                                     text_font=self.font1
                                                     )

        # destroys exit popup
        def destroy_exit_popup(self):
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
                                                      text_font=self.font1,
                                                      text_pos=(1.375, -.81, 1),
                                                      pressEffect=1,
                                                      geom_scale=(1, 6, 1),
                                                      relief=None,
                                                      clickSound=self.click_sound,
                                                      rolloverSound=self.rollover_sound,
                                                      textMayChange=1,
                                                      image=self.img1,
                                                      image_scale=(.25, .09, .09),
                                                      image_pos=(1.25, 0, -.75),
                                                      command=self.exit_popup
                                                      )

        # func that exits program
        @staticmethod
        def exit_app():
                sys.exit()


class AppInfo:  # formats information about main.py
        def __init__(self, devs, ver, tim):
                self.authors = devs
                self.version = ver
                self.runtime = tim
                self.app_data = 'Authors: {} | ' \
                                'Version: {} | ' \
                                'Script Time: {} seconds' \
                                .format(devs, ver, tim)
                self.total_time = 'Runtime: {} seconds'.format(tim)


# end time of main.py
end = time.time()
elapsed_time = (end - start)  # total script time

data = AppInfo('Christian Diaz', 'v1.1.2 Beta', elapsed_time)

print('GitHub Link: https://github.com/chrisd149/Cog-Customization')
print(data.app_data)
print('Thanks for playing!')

# creates a game log file if it already isn't made
log = open("game_log.txt", "w+")

log.write(str(data.total_time))  # writes the runtime formatted

# checks elapsed time
if elapsed_time < 1:
        log.write("  |  The program is running under a second.\n")
elif elapsed_time > 1 < 1.5:
        log.write("   |   The program is running slower than normal.\n")
elif elapsed_time > 2:
        log.write("   |   The program is running very slow.\n")

# program specs
# version
log.write("Cog Customization ")
log.write(data.version + "\n")

# authors
log.write("Authors: ")
log.write(data.authors + "\n")

# misc
log.write("Game Engine: Panda3D 1.10.2\n\
Programming Language: Python 3.7.2\n\
Language: English\n \n")

# short summery of project
log.write("This is a simple interactive Panda3D project using Python 3.7.2.\n\
This game lets you customize a Big Cheese cog via DirectButtons and functions.\n\
This game uses several assets made by the Disney Interactive Media Group and Toontown Rewritten\n\
and all credit goes to both entities for all models, images, sounds used in this project.\n\
The project's main page is at https://github.com/chrisd149/Cog-Customization")

app = MyApp()
app.run()