import time

class AppInfo:  # formats information about Main.py
        def __init__(self, devs, ver):
                self.authors = devs
                self.version = ver
                self.app_data = 'Authors: {} | ' \
                                'Version: {} | ' \
                                .format(devs, ver)


data = AppInfo('Christian Diaz', 'v2.0 Beta')

print('GitHub Link: https://github.com/chrisd149/Cog-Customization')
print(data.app_data)
print('Thanks for playing!')

# creates a game log file if it already isn't made
log = open("game_log.txt", "w+")

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
