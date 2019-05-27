<h1>Cog Customization v1.1.0 Beta</h1>

![image](https://user-images.githubusercontent.com/48182689/58392291-4c9d1480-8007-11e9-8c5a-0edb3a838928.png)
<h6>v1.1 Beta</h6>

This is a simple Panda3D program that allows the user to customize a Cog from Toontown.

[**Tutorial of the functions of the 4 main buttons**](https://youtu.be/33jWVTQWn1Q)

[**Overview of v1.0.1**](https://youtu.be/H13CPHQySiQ)

<h2>Table of Contents</h2>

- [Prerequisites](https://github.com/chrisd149/Cog-Customization#prerequisites)
	- [System Info](https://github.com/chrisd149/Cog-Customization#system-info)
	- [Software Info](https://github.com/chrisd149/Cog-Customization#software-info)
- [Installiation](https://github.com/chrisd149/Cog-Customization#installing)
	- [How to Install](https://github.com/chrisd149/Cog-Customization#how-to-install)
	- [Installiation Issues](https://github.com/chrisd149/Cog-Customization#installiation-issues)
- [Goals of Project](https://github.com/chrisd149/Cog-Customization#goals-of-project)
	- [Main Goals](https://github.com/chrisd149/Cog-Customization#main-goals)
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

<h2>Installiation</h2>

<h3>How to Install</h3>
	
1.	Download files from the latest release from the releases section.

2.	Install and configure [Panda3D-1.10-02](www.panda3d.org/download) if not already installed.

3.	Go to www.toontownrewritten.com/play, and install Toontown Rewritten.

4.	If not installed already, get [Python 3.7](www.python.org/downloads) installed, and properly configure it.

5.	Go to the Toontown Rewritten Folder, and copy/paste the .mf phase files into your Panda3D folder 
		- (For this project, only phase_3 through phase_5.5, and phase_9 through phase_11 files are needed). 
		
6.	Open main.pyw(Windows OS) or main.py(Any OS) to run the application 
	
<h3>Installiation Issues and Fixes</h3>

- You may have issues with setting the PATH varriable for Python on your Windows computer.  To fix this, watch this [video](https://www.youtube.com/watch?v=4V14G5_CNGg)
- The program may not start due to a few reasons:
	- Panda3D isn't set as the Python interpreter.  To fix this, make the default interpreter for main.py Panda3D-1.10.2-x64/python/python.exe.  This [video](https://user-images.githubusercontent.com/48182689/58389652-5e2bef80-7ffa-11e9-8f5b-7b4cfa74cf24.png) helps explain it better
		![image](https://user-images.githubusercontent.com/48182689/58389652-5e2bef80-7ffa-11e9-8f5b-7b4cfa74cf24.png)
	- You may not have the phase files in the Panda3D folder
	- The font files may not be in the same folder as the program main.py/main.pyw
	
<h2>Goals of Project</h2>

<h3>Main Goals</h3>

*	[X] **Sequences of animations of multiple actors**

*	[X] **GUI buttons with working animations/sounds/functions**

*  	[X] **Functions that change colors, scale, load/delete models, and textures**

*	[X] **Allow the user to access help *while* ingame or online via the wiki**

*	[X] **Update the game regularly with bug fixes and updates**

<h2>FAQ</h2>

Q: *Why isn't there an .exe file to make installation easier?*

A: I planned on making this project with the intent on making runnable on a majority of systems.  .exe is not supported on Mac and Linux systems, so they wouldn't have access to the program.  Making seperate versions for each operating system would take addtional time and effort on top of the normal updates.

Q: *Why use Panda3D, an almost 2 decade old game engine, alongside Python, to build a game?*

A: Panda3D is very unique in that it uses Python as it's main programming language.  Python is top level compared to normal gaming languages, like C++/C#, making it slow to execute.  However, it is easier and faster to write Python compared to a C-based language, making updates faster and easier to make.  Panda3D is the engine that runs Toontown, meaning I can use Toontown assets as models/actors/sfx in my program without having to make them myself.

Q: *Due to the game using Disney assets from Toontown Online, how is this program legal?*

A: After Toontown Online closed in 2013, many Toontown servers poped up, using Disney assets and modifing them to make their own free versions of the game.  Disney has chosen not to pursure legal action against these servers, which has been spectulated to be due to the large fanbase still present to this day, and the decison to make all servers non-profit.  I made my game with this in mind, so it is completly free to access and download, and credit is given to Disney when it is due.

Q: *What is the end goal for this project?*

A: This project is my first GitHub project I made public, as I wanted to test how to develop a game to give to the public.  I also learned many new things with Python and Panda3D that I wouldn't have learned elsewhere.  My goal is to constantly update the game when I get new ideas, and to learn more about game devlopment and programming.


<h2>License</h2>

**This Panda3D game and/or the author(s) are not affiliated with *The Walt Disney Company* and/or the *Disney Interactive Media Group*(collectively referred to as *"Disney"*).  All textures/models used in this program are not mine, and are allowed to be publicly used and distributed, with the exceptition for profit, which isn't allowed at all.**

This game can be modified to any extent. and can be reuploaded ***if*** it is modified.

Credit is not required, just have fun running/modifing the program :)


<h2>Built With</h2>

*	[***Panda3D***](https://www.panda3d.org/) - Game engine used and tutorials.

*	[***Toontown Rewritten***](https://www.toontownrewritten.com/) - Phase files imported from Toontown phase files.

*	[***PyCharm***](https://www.jetbrains.com/pycharm/) - IDE used to build program.



<h2>Authors</h2>

Main Author: Christian M Diaz

<h3>Contact Info</h3>

*	GitHub UserName: **@chrisd149**

* Email: **christianmigueldiaz@gmail.com**
	* Active Hours M-F: 3pm - 9pm EST
	* Active Hours Weekend: 11am - 1am EST (Some of the time im availiable to 4am on the weekends)

<h4>All questions and inquiries must be related to the project in some way, unrelated messages will be ignored</h4>

