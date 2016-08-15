from __future__ import division #so that 1/3=0.333 instead of 1/3=0
__author__ = "Ben Reuveni - ben.reuveni@gmail.com"

# Import relevant libraries

import os, sys, random, datetime, time, psychopy #handy system and path functions
from psychopy import visual, core, data, event, logging, gui, sound
import numpy as np  # whole numpy lib is available, prepend 'np.'


# This next bit will pop up a dialogue window where we can control a few things as well as specify participant #
expName = 'Stroop'
expInfo = {'Participant': 1, 'Condition': 0} # this is a dictionary!
dlg = gui.DlgFromDict(dictionary=expInfo,title=expName)

if dlg.OK == False:
    core.quit() #quit if user pressed cancel

expInfo['date'] = datetime.datetime.now().strftime("%d-%m-%y\nTime: %H:%M:%S")#add a simple timestamp


# Magic Numbers
'''
OK! Let's think about what variables we may need.
Certainly ones to hold timing info.
Perhaps something that defines how many trials we want (though this can be dictated by the input file as well)
Which keys are allowed
A dictionary that translates key strings to numbers because we want our data file to contain numbers for easy analysis.
So if someone presses 'd', we want that to end up as a 1 (or whatever).

I often find that this section tends to grow based on need.
'''


# Objects
'''
For Objects, we really only need 3:
A Text object
An Image object
A Sound Object (if you want to include Audio feedback).

Remember, reusing objects is not only good practice, it's less intensive on the machine / memory.
'''





# Functions
'''
This is where the majority of your code is going to live. Think about what aspects you need in order to run an experiment
What are all the moving parts? Here's a starter list:

A function that displays something and waits for either input or time to elapse
A function that grades the user response
A function that iterates over trials and calls the other functions when appropriate.

Think about it in terms of trial design. The more modular you make your experiment, the more flexible it will be in the future.
When I make my experiments, each aspect of trial design becomes its own function:

Fixation presentation
Stimulus presentation + response
Feedback
ITI / Break

Hint: You can use functions that do only 1 or 2 operations and then call another function:
<function is called>
changes the text of the textObject
<calls another function>
'''



# Experiment control
'''
This is going to be the shortest bit of the code. It's really just for calling your main function, and anything else
you might want to do Before you call that function and start the actual trials as well as anything you want done After
your main trial function is done, unless you have that function quit once it's done. Up to you!
'''
