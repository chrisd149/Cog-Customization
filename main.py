# This is a simple interactive Panda3D project using Python 3.7.2
# This game lets you customize a Big Cheese cog via DirectButtons and functions
# This game uses several assets made by the Disney Interactive Media Group and Toontown Rewritten

# Authors: Christian Diaz
# Engine Build: Panda3D 1.10.2
# Python 3.7.2
# Cog Customization v2.0 Pre Release

import sys
import webbrowser
import datetime

# Panda3D Imports
from direct.showbase.ShowBase import ShowBase
from direct.interval.IntervalGlobal import *
from panda3d.core import *
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *

# PrcFileDataaaaaaaaa
loadPrcFileData("", "window-title Cog Customization v2.0")  # titles the app
loadPrcFileData("", "win-size 1280 720")  # makes the app run in 720p

# comment this out to hide FPS counter
loadPrcFileData("", "show-frame-rate-meter True")  # displays frame rate


class Cog(ShowBase):
        def __init__(self):
                ShowBase.__init__(self)
                self.load_models()
                self.load_cog()
                self.load_gui()
                self.animations()
                self.screen_text()

                self.win.setClearColor((0, 0, 0, 1))  # sets background as black

                self.isMoving = False

                self.size = 0

                self.keyMap = {
                    "left": 0, "right": 0, "forward": 0, "backward": 0, "change-cam": 0, "sprint": 0}

                # this sets a node in cog1's chest for the camera to look at
                self.floater = NodePath(PandaNode("floater"))
                self.floater.reparentTo(self.cog1)
                self.floater.setZ(5.0)

                # labels for main buttons
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

                # music
                self.music1 = self.loader.loadSfx('source files\phase_3/audio/bgm\create_a_toon.ogg')
                self.music2 = self.loader.loadSfx('source files\phase_4/audio/bgm\MG_TwoDGame.ogg')
                self.music1.setVolume(.2)
                self.music2.setVolume(.2)
                self.music1.setLoop(True)  # loops music if it ends
                self.music1.play()

                # key binds
                self.accept('m', self.music1.stop)  # stops the music
                self.accept('m-repeat', self.music1.play)  # replays the music

                # camera settings
                self.disable_mouse()
                # disables the user from using the mouse to move the camera, which allows the camera to be moved
                self.camera.reparentTo(self.render)
                self.camera.setPosHpr((90, 0, 75), (80, 180, -180))

        # cogs/goons/bosses
        def load_cog(self):
                # cog_1 actor
                self.cog1 = Actor('source files\phase_3.5\models\char\suitA-mod.bam',
                                  {'Flail': 'source files\phase_4\models\char\suitA-flailing.bam',
                                   'Stand': 'source files\phase_4\models\char\suitA-neutral.bam',
                                   'Walk': 'source files\phase_4\models\char\suitA-walk.bam',
                                   'Victory': 'source files\phase_4\models\char\suitA-victory.bam'}
                                  )

                self.cog1.reparentTo(self.render)  # parents the actor as to the 3D environment
                self.cog1.setBlend(frameBlend=True)  # smooths frames

                # cog_1 shadow
                self.cog_shadow1 = self.loader.loadModel('source files\phase_3/models/props/drop_shadow.bam')
                self.cog_shadow1.reparentTo(self.cog1.find('**/joint_shadow'))
                self.cog_shadow1.setScale(.5)
                self.cog_shadow1.setColor(0, 0, 0, .5)
                self.cog_shadow1.setBin('fixed', 0, 1)  # sets the bin of the shadow fixed to the ground

                # cog head
                self.cog_head1 = self.loader.loadModel('source files\phase_4\models\char\suitA-heads.bam').find('**/bigcheese')
                self.cog_head1.reparentTo(self.cog1.find('**/joint_head'))
                # finds the cold caller head model and joints it to the head pos
                self.cog_head1.setPos(0, 0, -.05)

                # cog_1 hat
                self.hat1 = self.loader.loadModel('source files\phase_4\models/accessories/tt_m_chr_avt_acc_hat_fez.bam')
                self.hat1.reparentTo(self.cog_head1)
                self.hat1.setPosHprScale((0, -0.1, 1.5), (30, -10, 0), (.4, .4, .4))

                # cog position/hpr/scale
                self.cog1.setPosHprScale((130, -13.5, 70.75), (65, 0, 0), (1, 1, 1))

                # cog2 actor
                self.cog2 = Actor('source files\phase_3.5\models\char\suitC-mod.bam',
                                  {'Sit': 'source files\phase_11\models\char\suitC-sit.bam'}
                                  )

                self.cog2.loop('Sit')  # loops through the 'Sit' animation
                self.cog2.reparentTo(self.chair)  # parents the actor to the chair model
                self.cog2.setBlend(frameBlend=True)  # smooths frames

                # cog2 head
                self.cog_head2 = self.loader.loadModel('source files\phase_3.5\models\char\suitC-heads.bam').find('**/coldcaller')
                self.cog_head2.reparentTo(self.cog2.find('**/joint_head'))
                # finds the cold caller head model and joints it to the head pos
                self.cog_head2.setPos(0, 0, -.05)

                # cog2 textures
                self.cog_torso2 = self.loader.loadTexture('source files\phase_3.5\maps\s_blazer.jpg')
                self.cog2.find('**/torso').setTexture(self.cog_torso2, 1)

                self.cog_arms2 = self.loader.loadTexture('source files\phase_3.5\maps\s_sleeve.jpg')
                self.cog2.find('**/arms').setTexture(self.cog_arms2, 1)

                self.cog_legs2 = self.loader.loadTexture('source files\phase_3.5\maps\s_leg.jpg')
                self.cog2.find('**/legs').setTexture(self.cog_legs2, 1)
                # sets the textures to the sellbot textures

                # cog2 hat
                self.hat = self.loader.loadModel('source files\phase_4\models/accessories/tt_m_chr_avt_acc_hat_fedora.bam')
                self.hat.reparentTo(self.cog_head2)
                self.hat.setPosHprScale((0, 0, .9), (0, 0, 0), (.5, .5, .5))

                # cog2 position/hpr/scale
                self.cog2.setPosHprScale((0, -2, 0), (180, 0, 0), (.8, .8, .8))

                # goon actor
                self.goon = Actor('source files\phase_9\models\char\Cog_Goonie-zero.bam',
                                  {'Walk': 'source files\phase_9\models\char\Cog_Goonie-walk.bam'})
                self.goon.reparentTo(self.render)
                self.goon.setBlend(frameBlend=True)  # smooths frames

                # goon position/hpr/scale
                self.goon.setPosHprScale((150, -30, 70.65), (180, 0, 0), (2, 2, 2))

        # models
        def load_models(self):
                # loads all models, which don't have animations.

                # this is the main environment area for the game
                self.training = self.loader.loadModel('source files\phase_10\models\cogHQ\MidVault.bam')
                self.training.reparentTo(self.render)

                self.desk = self.loader.loadModel('source files\phase_3.5\models\modules\desk_only_wo_phone.bam')
                self.desk.reparentTo(self.render)
                self.desk.setPosHprScale((130, 7.5, 70.75), (120, 0, 0), (1.5, 1.5, 1.5))

                self.chair = self.loader.loadModel('source files\phase_5.5\models\estate\deskChair.bam')
                self.chair.reparentTo(self.render)
                self.chair.setPosHprScale((135, 7, 70.75), (-60, 0, 0), (1.5, 1.5, 1.5))

        # animations
        def animations(self):
                # actor intervals
                # cog1 actor intervals
                stand = self.cog1.actorInterval('Stand', duration=7.5, loop=1)
                victory = self.cog1.actorInterval('Victory', duration=7.5, loop=0)
                scared = self.cog1.actorInterval('Flail', duration=1.5, loop=0)

                # cog2 actor intervals
                sit = self.cog2.actorInterval('Sit', duration=10, loop=1)

                # goon actor intervals
                walk1 = self.goon.actorInterval('Walk', duration=6, loop=1)
                walk2 = self.goon.actorInterval('Walk', duration=1.5, loop=1)

                # goon hpr/pos intervals
                move1 = self.goon.posInterval(6, Point3(150, 12.5, 70.65))
                turn1 = self.goon.hprInterval(1.5, Vec3(0, 0, 0))
                move2 = self.goon.posInterval(6, Point3(150, -30, 70.65))
                turn2 = self.goon.hprInterval(1.5, Vec3(180, 0, 0))

                # cog1 head hpr intervals
                head1_1 = self.cog_head1.hprInterval(2.5, Vec3(30, 10, 0))
                head1_2 = self.cog_head1.hprInterval(2.5, Vec3(0, 0, 0))
                head1_3 = self.cog_head1.hprInterval(2.5, Vec3(-30, 20, 0))
                head1_4 = self.cog_head1.hprInterval(2.5, Vec3(-0, 0, 0))

                # cog2 head hpr intervals
                head2_1 = self.cog_head2.hprInterval(2.5, Vec3(15, 10, 0))
                head2_2 = self.cog_head2.hprInterval(2.5, Vec3(0, 0, 0))
                head2_3 = self.cog_head2.hprInterval(2.5, Vec3(-15, 10, 5))
                head2_4 = self.cog_head2.hprInterval(2.5, Vec3(-0, 0, 0))

                # sequences
                # goon sequence
                self.pace1 = Sequence(
                        Parallel(walk1, move1),
                        Parallel(turn1, walk2),
                        Parallel(move2, walk1),
                        Parallel(walk2, turn2)
                )
                self.pace1.loop()

                # cog1 head sequence
                self.pace2 = Sequence(
                        stand,
                        Parallel(stand, head1_1),
                        Parallel(stand, head1_2),
                        scared,
                        Parallel(stand, head1_3),
                        Parallel(stand, head1_4),
                        victory, stand,
                )
                self.pace2.loop()

                # cog2 head sequence
                self.pace3 = Sequence(
                        sit,
                        Parallel(sit, head2_1),
                        Parallel(sit, head2_2),
                        Parallel(sit, head2_3),
                        Parallel(sit, head2_4)
                )
                self.pace3.loop()

        # loads OnscreenText
        def screen_text(self):
                # displays all the OnscreenText on the top left of the program screen

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

                self.screentext3 = OnscreenText(text='Current Version: v2.0',
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


                self.info_frame = DirectFrame(frameSize=(-2, -.7, .40, 1),
                                              frameColor=(0, 0, 0, 0.1),
                                             )

        # loads buttons, sound effects, and images
        def load_gui(self):
                # gui audio & images files
                self.chat_box = self.loader.loadModel \
                        ('source files\phase_3\models\props\chatbox.bam')
                self.img1 = self.loader.loadModel('source files\phase_3\models\gui\ChatPanel.bam')  # img used for buttons
                self.img2 = self.loader.loadModel('source files\phase_3.5\models\gui\QT_buttons.bam')  # img used for help box button
                self.gui_image = self.loader.loadModel('source files\phase_3\models\gui\dialog_box_gui.bam')  # img used for gui bg

                # fonts
                self.font1 = self.loader.loadFont('Impress.ttf')  # Impress BT
                self.font2 = self.loader.loadFont('CogFont.ttf')  # VT Portable Remington

                # sound effects
                self.click_sound = self.loader.loadSfx(
                        'source files\phase_3/audio\sfx\GUI_create_toon_fwd.ogg')  # click sound effect
                self.click_sound.setVolume(.75)
                self.rollover_sound = self.loader.loadSfx('source files\phase_3/audio\sfx\GUI_rollover.ogg')  # rollover sound effect
                self.grunt_sound = self.loader.loadSfx(
                        'source files\phase_3.5/audio\dial\COG_VO_grunt.ogg')  # cog grunt sound effect

                # function for time in hours & seconds
                self.date = datetime.datetime.now()
                self.time_now = self.date.strftime('%H:%M')

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
                # destroys hat1 and adds hat2
                self.hat_button = DirectButton(text=('Fez Hat', 'Loading...', 'Change Hat', ''),
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

                # changes cog1 scale from normal to small
                self.scale_button = DirectButton(text=('Normal Cog', 'Loading...', 'Change Size', ''),
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
                self.color_button = DirectButton(text=('White', 'Loading...', 'Next Color', ''),
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

                self.texture_button = DirectButton(text=('Bossbot', 'Loading...', 'Change Type', ''),
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

                #
                self.start_button = DirectButton(text=('Start Game', 'Loading...', 'Start El Gameo', ''),
                                                text_scale=.05,
                                                text_font=self.font1,
                                                text_pos=(1.375, -.25, -.45),
                                                pressEffect=1,
                                                geom_scale=(1, 6, 1),
                                                relief=None,
                                                clickSound=self.click_sound,
                                                rolloverSound=self.rollover_sound,
                                                textMayChange=1,
                                                image=self.img1,
                                                image_scale=(.25, .09, .09),
                                                image_pos=(1.25, 0, -.185),
                                                command=self.start
                                                )

        @staticmethod
        def github_link():
                webbrowser.open('http://github.com/chrisd149/Cog-Customization/wiki/help')  # opens the GitHub wiki

        def start(self):
            self.forward_speed = 30
            # stops all other processes and changes camera PosHpr
            self.start_button.removeNode()
            self.camera.setPos(self.cog1.getX(), self.cog1.getY() - 10, 10)
            self.camera.reparentTo(self.cog1)
            self.camera.lookAt(self.floater)
            pl = base.cam.node().getLens()
            pl.setFov(80)


            self.screentext8 = OnscreenText(text='WASD Controls for movement, Tab for camera',
                                            pos=(-1.75, .575),
                                            font=self.font1,
                                            fg=(255, 255, 255, 1),
                                            scale=.05,
                                            align=TextNode.A_left,
                                            )
            self.screentext9 = OnscreenText(text='Press Shift to sprint forward',
                                            pos=(-1.75, .5),
                                            font=self.font1,
                                            fg=(255, 255, 255, 1),
                                            scale=.05,
                                            align=TextNode.A_left,
                                            )

            world = loader.loadModel('source files\models\world')
            world.reparentTo(self.render)
            world.setScale(2.5)
            self.cog1.setPosHpr((0, 0, 10), (-30, 0, 0))

            self.music2.setLoop(True)
            self.music2.play()

            # removes all 2D and 3D unwanted models
            self.goon.delete()
            self.chair.removeNode()
            self.desk.removeNode()
            self.gui_panel.removeNode()
            self.music1.stop()
            self.pace2.finish()
            self.training.removeNode()
            self.cog2.delete()
            self.cog_tag1.removeNode()
            self.cog_tag2.removeNode()
            self.scale_button.removeNode()
            self.hat_button.removeNode()
            self.texture_button.removeNode()
            self.color_button.removeNode()
            self.accessories_button_label.removeNode()
            self.scale_button_label.removeNode()
            self.color_button_label.removeNode()
            self.texture_button_label.removeNode()
            self.help_button.removeNode()

            # Create some lighting
            ambientLight = AmbientLight("ambientLight")
            ambientLight.setColor((.3, .3, .3, 1))
            directionalLight = DirectionalLight("directionalLight")
            directionalLight.setDirection((-5, -5, -5))
            directionalLight.setColor((1, 1, 1, .1))
            directionalLight.setSpecularColor((1, 1, 1, 1))
            render.setLight(render.attachNewNode(ambientLight))
            render.setLight(render.attachNewNode(directionalLight))

            self.cTrav = CollisionTraverser()

            self.cogGroundRay = CollisionRay()
            self.cogGroundRay.setOrigin(0, 0, 4)
            self.cogGroundRay.setDirection(0, 0, -1)
            self.cogGroundCol = CollisionNode('cog1Ray')
            self.cogGroundCol.addSolid(self.cogGroundRay)
            self.cogGroundCol.setFromCollideMask(CollideMask.bit(0))
            self.cogGroundCol.setIntoCollideMask(CollideMask.allOff())
            self.cog1Node = self.cog1.attachNewNode(self.cogGroundCol)
            self.cogGroundHandler = CollisionHandlerQueue()
            self.cTrav.addCollider(self.cog1Node, self.cogGroundHandler)

            self.camGroundRay = CollisionRay()
            self.camGroundRay.setOrigin(0, 0, 1)
            self.camGroundRay.setDirection(0, 0, -1)
            self.camGroundCol = CollisionNode('camRay')
            self.camGroundCol.addSolid(self.camGroundRay)
            self.camGroundCol.setFromCollideMask(CollideMask.bit(0))
            self.camGroundCol.setIntoCollideMask(CollideMask.allOff())
            self.camGroundColNp = self.camera.attachNewNode(self.camGroundCol)
            self.camGroundHandler = CollisionHandlerQueue()
            self.cTrav.addCollider(self.camGroundColNp, self.camGroundHandler)

            # binds keys to movement, WASD format
            self.accept("escape", sys.exit)
            self.accept("a", self.setKey, ["left", True])
            self.accept("d", self.setKey, ["right", True])
            self.accept("w", self.setKey, ["forward", True])
            self.accept("s", self.setKey, ["backward", True])
            self.accept("tab", self.setKey, ["change-cam", True])
            self.accept("shift", self.setKey, ["sprint", True])
            self.accept("a-up", self.setKey, ["left", False])
            self.accept("d-up", self.setKey, ["right", False])
            self.accept("w-up", self.setKey, ["forward", False])
            self.accept("s-up", self.setKey, ["backward", False])
            self.accept("tab-up", self.setKey, ["change-cam", False])
            self.accept("shift-up", self.setKey, ["sprint", False])

            taskMgr.add(self.move, "moveTask")  # adds movement task to taskMgr
            taskMgr.add(self.extra_move, "addmoveTask")  # adds movement task to taskMgr

            self.dev_button = DirectButton(text=('Show Collisions', 'Loading...', 'Show Collisions', ''),
                                             text_scale=.05,
                                             text_font=self.font1,
                                             text_pos=(1.375, -.25, -.45),
                                             pressEffect=1,
                                             geom_scale=(1, 6, 1),
                                             relief=None,
                                             clickSound=self.click_sound,
                                             rolloverSound=self.rollover_sound,
                                             textMayChange=1,
                                             image=self.img1,
                                             image_scale=(.25, .09, .09),
                                             image_pos=(1.25, 0, -.185),
                                             command=self.show_collisons
                                             )

        # destroys hat1 and adds hat2
        def destroy_hat1(self):
                self.hat1.removeNode()
                del self.hat1
                self.hat_button.destroy()
                del self.hat_button

                self.hat2 = self.loader.loadModel('source files\phase_4\models/accessories/tt_m_chr_avt_acc_hat_band.bam')
                self.hat2.setPosHprScale((0, -0.1, 1.5), (180, 0, 0), (.25, .25, .25))
                self.hat2.reparentTo(self.cog_head1)

                self.hat_button = DirectButton(text=('Grand Band Hat', 'Loading...', 'Change Hat', ''),
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
                self.hat_button.destroy()
                del self.hat_button

                self.hat3 = self.loader.loadModel('source files\phase_4\models/accessories/tt_m_chr_avt_acc_hat_cowboyHat.bam')
                self.hat3.reparentTo(self.cog_head1)
                self.hat3.setPosHprScale((0, -0.1, 1.5), (10, 10, 0), (.35, .35, .35))

                self.hat_button = DirectButton(text=('Cowboy Hat', 'Loading...', 'Change Hat', ''),
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
                self.hat_button.destroy()
                del self.hat_button

                self.hat4 = self.loader.loadModel('source files\phase_4\models/accessories/tt_m_chr_avt_acc_msk_dorkGlasses.bam')
                self.hat4.reparentTo(self.cog_head1)
                self.hat4.setPosHprScale((0, -0.1, .65), (180, 10, 0), (.35, .35, .35))

                self.hat_button = DirectButton(text=('Glasses', 'Loading...', 'Change Hat', ''),
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
                self.hat_button.destroy()
                del self.hat_button

                self.hat5 = self.loader.loadModel('source files\phase_4\models/accessories/ttr_m_chr_acc_msk_moostacheC.bam')
                self.hat5.reparentTo(self.cog_head1)
                self.hat5.setPosHprScale((0, .825, .65), (180, 0, 0), (1, 1, 1))

                self.hat_button = DirectButton(text=('Moustache', 'Loading...', 'Change Hat', ''),
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
                self.hat_button.destroy()
                del self.hat_button

                self.hat6 = self.loader.loadModel('source files\phase_4\models/accessories/tt_m_chr_avt_acc_hat_dinosaur.bam')
                self.hat6.reparentTo(self.cog_head1)
                self.hat6.setPosHprScale((0, -0.1, 1.25), (180, 0, 0), (.3, .3, .3))

                self.hat_button = DirectButton(text=('Dinosaur Hat', 'Loading...', 'Change Hat', ''),
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

        # destroys hat6 and adds hat1
        def destroy_hat6(self):
                self.hat6.removeNode()
                del self.hat6
                self.hat_button.destroy()
                del self.hat_button

                self.hat1 = self.loader.loadModel('source files\phase_4\models/accessories/tt_m_chr_avt_acc_hat_fez.bam')
                self.hat1.reparentTo(self.cog_head1)
                self.hat1.setPosHprScale((0, -0.1, 1.5), (30, -10, 0), (.4, .4, .4))

                self.hat_button = DirectButton(text=('Fez Hat', 'Loading...', 'Change Hat', ''),
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
                # cog speed is set to 30 to compensate for the reduction in speed caused by descaling
                self.forward_speed = 30

                self.size = -1
                cog1_scale1 = self.cog1.scaleInterval(.25, Point3(.5, .5, .5))
                cog_tag1_scale1 = self.cog_tag1.scaleInterval(.25, Point3(.5, .5, .5))
                cog_tag1_pos1 = self.cog_tag1.posInterval(.25, Point3(.565, .45, .05))

                self.scale_button.removeNode()
                del self.scale_button

                seq1 = Parallel(cog1_scale1,
                                cog_tag1_scale1,
                                cog_tag1_pos1
                                )
                seq1.start()

                self.scale_button = DirectButton(text=('Small Cog', 'Loading...', 'Change Size', ''),
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

        # returns small scale to normal scale
        def normal_scale(self):
                self.size = 0
                # cog speed is set to 20
                self.forward_speed = 20
                cog1_scale2 = self.cog1.scaleInterval(.25, Point3(1, 1, 1))
                cog_tag1_scale2 = self.cog_tag1.scaleInterval(.25, Point3(1, 1, 1))
                cog_tag1_pos2 = self.cog_tag1.posInterval(.25, Point3(.565, .45, .475))
                self.scale_button.removeNode()
                del self.scale_button

                seq2 = Parallel(cog1_scale2,
                                cog_tag1_scale2,
                                cog_tag1_pos2,
                                )
                seq2.start()
                self.scale_button = DirectButton(text=('Normal Cog', 'Loading...', 'Change Size', ''),
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

        # scales cog to 1.5
        def large_scale(self):
                self.size = 1
                # cog speed is set to 10 to compensate for the increase in speed caused by upscaling
                self.forward_speed = 10
                cog1_scale3 = self.cog1.scaleInterval(.25, Point3(1.5, 1.5, 1.5))
                cog_tag1_scale3 = self.cog_tag1.scaleInterval(.25, Point3(1.5, 1.5, 1.5))
                cog_tag1_pos3 = self.cog_tag1.posInterval(.25, Point3(.565, .45, .9))
                self.scale_button.removeNode()
                del self.scale_button

                seq3 = Parallel(cog1_scale3,
                                cog_tag1_scale3,
                                cog_tag1_pos3,
                                )
                seq3.start()

                self.scale_button = DirectButton(text=('Large Cog', 'Loading...', 'Change Size', ''),
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

        # returns large scale to normal scale
        def normal_scale2(self):
                self.size = 0
                # cog speed is set to 20
                self.forward_speed = 20
                cog1_scale4 = self.cog1.scaleInterval(.25, Point3(1, 1, 1))
                cog_tag1_scale4 = self.cog_tag1.scaleInterval(.25, Point3(1, 1, 1))
                cog_tag1_pos4 = self.cog_tag1.posInterval(.25, Point3(.565, .45, .475))
                self.scale_button.removeNode()
                del self.scale_button

                seq4 = Parallel(cog1_scale4,
                                cog_tag1_scale4,
                                cog_tag1_pos4,
                                )
                seq4.start()

                self.scale_button = DirectButton(text=('Normal Cog', 'Loading...', 'Change Size', ''),
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
                self.color_button.destroy()
                del self.color_button

                self.color_button= DirectButton(text=('Purple', 'Loading...', 'Next Color', ''),
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
                self.color_button.destroy()
                del self.color_button

                self.color_button = DirectButton(text=('Yellow', 'Loading...', 'Change Color', ''),
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
                self.color_button.destroy()
                del self.color_button

                self.color_button = DirectButton(text=('Cyan', 'Loading...', 'Change Color', ''),
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
                self.color_button.destroy()
                del self.color_button

                self.color_button= DirectButton(text=('Red', 'Loading...', 'Change Color', ''),
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
                self.color_button.destroy()
                del self.color_button

                self.color_button = DirectButton(text=('Blue', 'Loading...', 'Change Color', ''),
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
                self.color_button.destroy()
                del self.color_button

                self.color_button = DirectButton(text=('Green', 'Loading...', 'Change Color', ''),
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
                self.color_button.destroy()
                del self.color_button

                self.color_button = DirectButton(text=('White', 'Loading...', 'Change Color', ''),
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
                self.cog_torso1 = self.loader.loadTexture('source files\phase_3.5\maps\m_blazer.jpg')
                self.cog1.find('**/torso').setTexture(self.cog_torso1, 1)

                self.cog_arms1 = self.loader.loadTexture('source files\phase_3.5\maps\m_sleeve.jpg')
                self.cog1.find('**/arms').setTexture(self.cog_arms1, 1)

                self.cog_legs1 = self.loader.loadTexture('source files\phase_3.5\maps\m_leg.jpg')
                self.cog1.find('**/legs').setTexture(self.cog_legs1, 1)

                self.texture_button.destroy()
                del self.texture_button

                self.texture_button = DirectButton(text=('Cashbot', 'Loading...', 'Change Type', ''),
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
                self.cog_torso1 = self.loader.loadTexture('source files\phase_3.5\maps\l_blazer.jpg')
                self.cog1.find('**/torso').setTexture(self.cog_torso1, 1)

                self.cog_arms1 = self.loader.loadTexture('source files\phase_3.5\maps\l_sleeve.jpg')
                self.cog1.find('**/arms').setTexture(self.cog_arms1, 1)

                self.cog_legs1 = self.loader.loadTexture('source files\phase_3.5\maps\l_leg.jpg')
                self.cog1.find('**/legs').setTexture(self.cog_legs1, 1)

                self.texture_button.destroy()
                del self.texture_button

                self.texture_button = DirectButton(text=('Lawbot', 'Loading...', 'Change Type', ''),
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
                self.cog_torso1 = self.loader.loadTexture('source files\phase_3.5\maps\s_blazer.jpg')
                self.cog1.find('**/torso').setTexture(self.cog_torso1, 1)

                self.cog_arms1 = self.loader.loadTexture('source files\phase_3.5\maps\s_sleeve.jpg')
                self.cog1.find('**/arms').setTexture(self.cog_arms1, 1)

                self.cog_legs1 = self.loader.loadTexture('source files\phase_3.5\maps\s_leg.jpg')
                self.cog1.find('**/legs').setTexture(self.cog_legs1, 1)

                self.texture_button.destroy()
                del self.texture_button

                self.texture_button = DirectButton(text=('Sellbot', 'Loading...', 'Change Type', ''),
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
                self.cog_torso1 = self.loader.loadTexture('source files\phase_3.5\maps\c_blazer.jpg')
                self.cog1.find('**/torso').setTexture(self.cog_torso1, 1)

                self.cog_arms1 = self.loader.loadTexture('source files\phase_3.5\maps\c_sleeve.jpg')
                self.cog1.find('**/arms').setTexture(self.cog_arms1, 1)

                self.cog_legs1 = self.loader.loadTexture('source files\phase_3.5\maps\c_leg.jpg')
                self.cog1.find('**/legs').setTexture(self.cog_legs1, 1)

                self.texture_button.destroy()
                del self.texture_button

                self.texture_button = DirectButton(text=('Bossbot', 'Loading...', 'Change Type', ''),
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

        # loads the help box
        def help_box(self):
                self.help_button.destroy()
                del self.help_button
                self.isMoving = False
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

        # loads the exit popup
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

                # destroys exit pop up
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

        def setKey(self, key, value):
            self.keyMap[key] = value
            print('Moved')

            # Accepts arrow keys to move either the player or the menu cursor,
            # Also deals with grid checking and collision detection
        def move(self, task):
            self.camera.setPos(0, -20, 20)
            # Get the time that elapsed since last frame.  We multiply this with
            # the desired speed in order to find out with which distance to move
            # in order to achieve that desired speed.
            dt = globalClock.getDt()

            # If the camera-left key is pressed, move camera left.
            # If the camera-right key is pressed, move camera right.

            # save ralph's initial position so that we can restore it,
            # in case he falls off the map or runs into something.

            startpos = self.cog1.getPos()

            # If a move-key is pressed, move ralph in the specified direction.

            if self.keyMap["left"]:
                self.cog1.setH(self.cog1.getH() + 100 * dt)
            if self.keyMap["right"]:
                self.cog1.setH(self.cog1.getH() - 100 * dt)
            if self.keyMap["forward"]:
                self.cog1.setY(self.cog1, self.forward_speed * dt)
            if self.keyMap["backward"]:
                self.cog1.setY(self.cog1, -10 * dt)
            if self.keyMap['change-cam']:
                self.camera.setY(20)

            if self.keyMap["forward"] or self.keyMap["left"] or self.keyMap["right"] or self.keyMap["backward"]:
                if self.isMoving is False:
                    self.cog1.loop("Walk")
                    self.isMoving = True
            else:
                if self.isMoving:
                    self.cog1.stop()
                    self.cog1.loop("Stand")
                    self.isMoving = False

            # Normally, we would have to call traverse() to check for collisions.
            # However, the class ShowBase that we inherit from has a task to do
            # this for us, if we assign a CollisionTraverser to self.cTrav.
            # self.cTrav.traverse(render)

            entries = list(self.cogGroundHandler.getEntries())
            entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())

            if len(entries) > 0 and entries[0].getIntoNode().getName() == "terrain":
                self.cog1.setZ(entries[0].getSurfacePoint(render).getZ())
            else:
                self.cog1.setPos(startpos)

            entries = list(self.camGroundHandler.getEntries())
            entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())

            if len(entries) > 0 and entries[0].getIntoNode().getName() == "terrain":
                self.camera.setZ(entries[0].getSurfacePoint(render).getZ() + 10)
            if self.camera.getZ() < self.cog1.getZ():
                self.camera.setZ(self.cog1.getZ() + 5.0)

            # The camera should look in cog's direction,
            # but it should also try to stay horizontal, so look at
            # a floater which hovers above cog's head.
            self.camera.lookAt(self.floater)

            return task.cont

        def extra_move(self, task):
            pl = base.cam.node().getLens()
            # This makes the forward speed double while shift key is held down, and changes camera FOV as well
            if self.keyMap['sprint'] is True:
                pl.setFov(120)
                self.forward_speed = 60
                self.music2.setPlayRate(1.5)
                self.cog1.setPlayRate(2.0, 'Walk')

            if self.keyMap['sprint'] is False:
                self.forward_speed = 30
                pl.setFov(80)
                self.music2.setPlayRate(1.0)
                self.cog1.setPlayRate(1.0, 'Walk')

            return task.cont

        def show_collisons(self):
            self.cTrav.showCollisions(render)
            self.dev_button.removeNode()

        # function that exits the program
        @staticmethod
        def exit_app():
                sys.exit()


app = Cog()
app.run()

