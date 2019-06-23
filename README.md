<h1>Cog Customization v1.1.3 Beta</h1>

![image](https://user-images.githubusercontent.com/48182689/58392291-4c9d1480-8007-11e9-8c5a-0edb3a838928.png)
<h6>v1.1 Beta</h6>

This is a simple Panda3D program that allows the user to customize a Cog from Toontown.

[**Tutorial of the functions of the 4 main buttons**](https://youtu.be/33jWVTQWn1Q)

[**Overview of v1.0.1**](https://youtu.be/H13CPHQySiQ)

<h2>Table of Contents</h2>

- [Prerequisites](https://github.com/chrisd149/Cog-Customization#prerequisites)
	- [System Info](https://github.com/chrisd149/Cog-Customization#system-info)
	- [Software Info](https://github.com/chrisd149/Cog-Customization#software-info)
- [Installation](https://github.com/chrisd149/Cog-Customization#installation)
	- [How to Install](https://github.com/chrisd149/Cog-Customization#how-to-install)
	- [Installation Issues](https://github.com/chrisd149/Cog-Customization#installation-issues)
- [Current Features](https://github.com/chrisd149/Cog-Customization#current-features)
- [Goals of Project](https://github.com/chrisd149/Cog-Customization#goals-of-project)
	- [Main Goals](https://github.com/chrisd149/Cog-Customization#main-goals)
	- [Side Goals](https://github.com/chrisd149/Cog-Customization#side-goals)
- [FAQ](https://github.com/chrisd149/Cog-Customization#faq)
- [Licensing](https://github.com/chrisd149/Cog-Customization#license)
- [Built With](https://github.com/chrisd149/Cog-Customization#built-with)
- [Authors](https://github.com/chrisd149/Cog-Customization#authors)
	- [Christian's Contact Info](https://github.com/chrisd149/Cog-Customization#contact-info)

<h2>Prerequisites</h2>

<h3>System Info</h3>	

*	**OS**: Windows 10/8/7/Vista/XP; Mac OS 10.14; Linux Ubuntu 18.04

*	**CPU**: 500Mhz< CPU, 1Ghz< Recommended

*	**GPU**: CPU interal graphics, any Nividia or Radeon GPU recommended

*	**Memory**: 200mb<, 512mb< recommended

<h3>Software Info</h3>

*	**Engine**: ***Panda3D-1.10.2***

*	**Programming Language**: ***Python 3.7***

*	**Language**: English, Spanish possibly later.

<h2>Installation</h2>

<h3>How to Install</h3>
	
1.	Download files from the latest release from the releases section.

2.	Install and configure Panda3D-1.10-02 at www.panda3d.org/download/sdk-1-10-2 if not already installed.

3.	Go to www.toontownrewritten.com/play, and install Toontown Rewritten.

4.	If not installed already, get [Python 3.7](www.python.org/downloads) installed, and properly configure it.

5.	Go to the Toontown Rewritten Folder, and copy/paste the .mf phase files into your Panda3D folder 
		- (For this project, only phase_3 through phase_5.5, and phase_9 through phase_11 files are needed). 
		
6.	Open main.pyw(Windows OS) or main.py(Any OS) to run the application 
	
<h3>Installaton Issues and Fixes</h3>

- You may have issues with setting the PATH varriable for Python on your Windows computer.  To fix this, watch this [video](https://www.youtube.com/watch?v=4V14G5_CNGg)
- The program may not start due to a few reasons:
	- Panda3D isn't set as the Python interpreter.  To fix this, make the default interpreter for main.py Panda3D-1.10.2-x64/python/python.exe.  This [video](https://user-images.githubusercontent.com/48182689/58389652-5e2bef80-7ffa-11e9-8f5b-7b4cfa74cf24.png) helps explain it better
		![image](https://user-images.githubusercontent.com/48182689/58389652-5e2bef80-7ffa-11e9-8f5b-7b4cfa74cf24.png)
	- You may not have the phase files in the Panda3D folder
	- The font files may not be in the same folder as the program main.py/main.pyw
- Download the latest release from the Releases section, since older releases may have more bugs/less features.
	
<h2>Current Features</h2>

- 4 DirectButtons with functions that control the appearance of the Big Cheese cog
- A help button that opens a help box
- 3 Actors that have a loop of sequences of animations
- Music that can be stopped by clicking the key M and restarted by holding down M
- An exit button that leads to an exit popup window
	- Exit popup with 2 DirectButtons that close the program or exit popup
- A DirectEntry object that can be closed by clicking the Enter key
- A DirectButton that opens the Cog Customization Wiki
- Title of program window with program name and version
- Default resoulution of 720p to fit most monitors
- Frame rate meter that displays current frame rate
- Game log that includes the run time and specs of the program

<h2>Goals of Project</h2>

<h3>Main Goals</h3>

*	[X] **Sequences of animations of multiple actors**

*	[X] **GUI buttons with working animations/sounds/functions**

*  	[X] **Functions that change colors, scale, load/delete models, and textures**

*	[ ] **Separate versions of main.py/pyw in Spanish, French and German**

<h3>Side Goals</h3>

*	[X] **Update the game regularly with bug fixes and updates**

*	[X] **Resolve Bugs/Issues when present**

*	[X] **Allow the user to access help *while* ingame or online via the wiki**

*	[ ] **Make a for loop that returns different valules in game_log.txt (i.e. total time ingame, avg frame rate, customizations chosen, etc.**

*	[ ] **Change all code to Python 3.8 and Panda3D 1.10.3**

<h2>FAQ</h2>

Q: *Why isn't there an .exe file to make installation easier?*

A: I planned on making this project with the intent on making runnable on a majority of systems.  .exe is not supported on Mac and Linux systems, so they wouldn't have access to the program.  Making seperate versions for each operating system would take addtional time and effort on top of the normal updates.

Q: *Why use Panda3D, an almost 2 decade old game engine, alongside Python, to build a game?*

A: Panda3D is very unique in that it uses Python as it's main programming language.  Python is top level compared to normal gaming languages, like C++/C#, making it slow to execute.  However, it is easier and faster to write Python compared to a C-based language, making updates faster and easier to make.  Panda3D is the engine that runs Toontown, meaning I can use Toontown assets as models/actors/sfx in my program without having to make them myself.

Q: *Due to the game using Disney assets from Toontown Online, how is this program legal?*

A: After Toontown Online closed in 2013, many Toontown servers poped up, using Disney assets and modifing them to make their own free versions of the game.  Disney has chosen not to pursure legal action against these servers, which has been spectulated to be due to the large fanbase still present to this day, and the decison to make all servers non-profit.  I made my game with this in mind, so it is completly free to access and download, and credit is given to Disney when it is due.

Q: *What is the end goal for this project?*

A: This project is my first GitHub project I made public, as I wanted to test how to develop a game to give to the public.  I also learned many new things with Python and Panda3D that I wouldn't have learned elsewhere.  My goal is to constantly update the game when I get new ideas, and to learn more about game devlopment and programming.

Q: *What experience is required to make a game like this one?*

A: This project took me almost 3 months to make at this point.  I can say I was very slow for the first month, mainly due to health issues, but I quickly got back in to coding and learned more about Panda3D.  All in all, I would say a few months experience with Python and some experience with Panda3D can give you the mindset and tools to make a game like this one.  Much of the code is still very basic, since many functions could be shortened by using loops/dictionaries.

Q: *How would one go about learning Panda3D with Python?*

A: The easiest way is too learn Python on *atleast* a beginner level.  Then, follow some tutorials on Youtube, that go over setup and basic coding practices specific to Panda3D.  I recommend you go to the offical [Panda3D Manual](https://www.panda3d.org/manual/) to get more detailed lessons on the game engine.


<h2>License</h2>

This project is licensed under the a modified MIT License, which allows private use, commercial use, modification, and distribution of this program, but not sales, and gives me (Christian Diaz) copyright holder status.

**This Panda3D game and/or the author(s) are not affiliated with *The Walt Disney Company* and/or the *Disney Interactive Media Group*(collectively referred to as *"Disney"*), and/or Toontown Rewritten.  All textures/models/sounds used in this program are not mine, and are allowed to be publicly used and distributed, with the exceptition for profit, which isn't allowed at all.  By downloading this game, you agree to release any employees of Disney and/or Toontown Rewritten from any liablity caused to you from the use of Cog Customization.**


<h2>Built With</h2>

*	[***Panda3D***](https://www.panda3d.org/) - Game engine used and tutorials.

*	[***Toontown Rewritten***](https://www.toontownrewritten.com/) - Phase files imported from Toontown phase files.

*	[***PyCharm***](https://www.jetbrains.com/pycharm/) - IDE used to build program.



<h2>Authors</h2>

Main Author: Christian M Diaz

<h3>Contact Info</h3>

*	GitHub UserName: **@chrisd149**

*	Discord Username: **Miguel149#7640**

*	Twitter: **@miguel_TTR**

* Email: **christianmigueldiaz@gmail.com**
	* Active Hours M-F: 3pm - 12am EST
	* Active Hours Weekend: 12pm - 1am EST (Some of the time im availiable to 4am on the weekends)

<h4>All questions and inquiries must be related to the project in some way, unrelated messages will be ignored</h4>

