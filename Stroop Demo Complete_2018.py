from __future__ import division #so that 1/3=0.333 instead of 1/3=0
__author__ = "Ben Reuveni - ben.reuveni@gmail.com"

'''
 This is intended to be a template for most Behavioral experiments.
 The basic design is to read from an input file, administer the experiment
 and provide a datafile at the end.
 The hope is that this experiment can be modified to serve almost any design.
'''

# Import relevant libraries

import os, sys, random, datetime, time, psychopy #handy system and path functions
from psychopy import visual, core, data, event, logging, gui, sound
import numpy as np  # whole numpy lib is available, prepend 'np.'



# This next bit will pop up a dialogue window where we can control a few things as well as specify participant #
expName = 'None'
expInfo = {'Participant': 1, 'Condition': 0} # can be expanded based on input needs
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit() #user pressed cancel
expInfo['date'] = datetime.datetime.now().strftime("%d-%m-%y\nTime: %H:%M:%S")#add a simple timestamp

'''
 Magic Numbers - Note: None of these NEED to be specified from within the code.
 It is entirely possible (and sometimes recommended) to get all this information
 from your input file using clever indexing/variable declarations.

 Just make sure to load your file first!

 For now, we're going to simply declare them here.
'''

trialClock = core.Clock()
# All times are in seconds.
fixateTimeout = 0.25
stimTimeout = 1
responseTimeout = 1
tooSlowTime = .25
feedbackTimeout = 1
ITI = 0.25

soundFeedback = 1 # controls whether or not sound will be played along with the feedback
soundFreq = 500
totalTrials = 12
stimBeforeBreak = 7

# this is where we specify which keys are allowed. Make this whatever you like!
allowedKeys = ("d", "k")
keyMap = {"d":2, "k":1, 'NA':'NA'} # this is a dictionary. Just like a normal dictionary, the first item is what you input, the second item is its definition
allKeys = []
stimCount = 0

'''
 This controls whether the program translates numbers to words or words to numbers.
 This is an example of how we can use the initial dialog box to control anything we want throughout the exp.
 This IF will appear in various places throughout - Try and spot them and see what they do.
'''
if expInfo['Condition'] == 0:
    colorMap = {1:'red', 2:'blue', 3:'green', 4:'orange', 5:'yellow', 6:'pink'}
    stimMap = {1:'Red', 2:'Blue', 3:'Green', 4:'Orange', 5:'Yellow', 6:'Pink'}
elif expInfo['Condition'] == 1:
    colorMap = {'RED':1, 'BLUE':2, 'GREEN':3, 'ORANGE':4, 'YELLOW':5, 'PINK':6}
    stimMap = {'RED':1, 'BLUE':2, 'GREEN':3, 'ORANGE':4, 'YELLOW':5, 'PINK':6}

#Initialize pre-experiment stuff including loading the input file, creating the output file.

#Sets up a datafile
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + '%s' %(expInfo['Participant']) # this sets up the pathname for the output file using the participant number
logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

#loads the input file from the current working directory - this can be changed if specified.

if expInfo['Condition'] == 0:
    inputMain = np.genfromtxt('Stroop_Input.txt', dtype=None) #file name in ' ' can be changed.
if expInfo['Condition'] == 1:
    inputMain = np.genfromtxt('Stroop_Input_words2.txt', dtype=None) #file name in ' ' can be changed.

#opens a datafile with the following name

if expInfo['Condition'] == 0:
    dataFile = open(filename+'_Stroop_Task_Output.txt', 'w') #it's best not to use spaces in the filename.
if expInfo['Condition'] == 1:
    dataFile = open(filename+'_Stroop_Task_Output_Words.txt', 'w') #it's best not to use spaces in the filename.


#sets up the output file "header" with some useful information about trial design, start time, etc.
dataFile.write(
    'Participant #' +str(expInfo['Participant'])
    +'\nFixation Timeout: ' + str(fixateTimeout)
    + 's\nStimulus Timeout: ' +str(stimTimeout)
    + 's\nResponse Timeout: ' +str(responseTimeout)
    + 's\nFeedback Timeout: ' +str(feedbackTimeout)
    + 's\nITI: ' + str(ITI)
    + '\n'
    + '\nStimuli Before Break: ' + str(stimBeforeBreak)
    + '\nTotal Trials: ' + str(totalTrials)+'\n\n')


# Objects

win = visual.Window(size=(700, 700), fullscr=False, screen=0, allowGUI=False, monitor=u'testMonitor',
                    allowStencil=False, color=[0,0,0], colorSpace=u'rgb', units='cm')

textStim = visual.TextStim(
    win=win, ori=0, name='', text='+', font='Arial',
    units='cm', pos=[0, 0], height=1, wrapWidth=None,
    color="white", colorSpace='rgb', opacity=1, depth=0.0)

imageStim = visual.ImageStim(
    win=win, name='', image='Correct.png', mask=None, ori=0,
    pos=[0, 0], size=[10.0, 10.0], color=[1,1,1], colorSpace=u'rgb',
    opacity=1, texRes=128, interpolate=False, depth=-2.0)

correctSound = sound.Sound(value=500, secs=feedbackTimeout)
incorrectSound = sound.Sound(value=200, secs=feedbackTimeout)

# Functions

def doUserInteraction(stim, expectedKeys, timeout, soundFile):
    global paused
    if timeout == None or timeout == 0:
        timeout = sys.maxint
    startTime = trialClock.getTime()
    endTime = startTime + timeout

    response = {
        "keys": [],
        "firstKey": None,
        "lastKey": None,
        "startTime": startTime,
        "endTime": endTime,
        "duration": 0,
        "timedOut": False,
        }

    if soundFile != None:
        soundFile.play()

    while(True):
        stim.setAutoDraw(True) #continuously draws the stimulus to the buffer
        win.flip() # exposes the stimulus to the screen
        keys = [] # initializes an empty array to hold the keys that were pressed.

        # this IF checks 2 things in order to determine which keys are allowed to be pressed:

        if expectedKeys != None: # Have I specified a list of allowed keys?
            if len(expectedKeys) != 0: # Have I specified any particular keys (rather than just [] which means All keys)?
                keys = event.getKeys(expectedKeys) # Listen for key presses from a particular subset
            else:
                keys = event.getKeys() # Listen for Any key presses.
        if len(keys) > 0: # If a key was pressed store some values in the object "response" defined above.
            response["keys"] = keys # put all the responses in here.
            response["firstKey"] = keys[0] # put the first keypress here
            response["lastKey"] = keys[len(keys)-1] # put the last keypress here.
            break #break out of this function

        elif trialClock.getTime() > endTime: # If the response time window has run out
            response["timedOut"] = True # indicate that we timed out
            response["firstKey"] = 'NA' # put 'NA' as the first key pressed
            break

        if event.getKeys(['f5']): # This is a "pause" button for the experiment
            textStim.text = 'Press any key to continue'
            textStim.pos = (0,-10)
            paused = 1
            stimUntilAnyKey(textStim)
            textStim.pos = (0,0)

        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit() #quits the entire experiment - will dump you to the desktop or whatever.

    stim.setAutoDraw(False) # stop drawing the stimulus to the buffer
    win.flip() # expose the now blank buffer to the screen
    response["duration"] = trialClock.getTime() - startTime # keeps track of how long since the stim was drawn to the screen
    event.clearEvents(eventType=None) # clear the key buffer.
    return response # ends the function and returns the object "response". Without this return - we would not be able to access any of this data.

def stimUntilAnyKey(stim):
    return doUserInteraction(stim, allKeys, None, None)

def doStimulus(expectedKeys, timeout, text, color):
    global textStim

    if expInfo['Condition'] == 0:
        textStim.color = colorMap[color] # If numbers, you need this line
        textStim.text = stimMap[text] # If numbers, you need this line
    elif expInfo['Condition'] == 1:
        textStim.text = text # If your inputFile literally has the text in it, this line will work
        textStim.color = color # If your inputFile literally has the color names in it, this line will work
#
    return doUserInteraction(textStim, expectedKeys, timeout, None)

def doFixate(duration):
# calls doUserInteraction with fixate stim, no keys
    textStim.color = 'White'
    textStim.text = '+'
    return doUserInteraction(textStim, None, duration, None)

def showCorrect(duration, soundFeedback):
# calls doUserInteraction  with "correct" stim
    imageStim.image = 'Correct.png'
    if soundFeedback == 1:
        return doUserInteraction(imageStim, None, duration, correctSound)
    else:
        return doUserInteraction(imageStim, None, duration, None)

def showIncorrect(duration, soundFeedback):
# calls doUserInteraction with "incorrect" stim, no AllowedKeys, duration
    imageStim.image = 'Incorrect.png'
    if soundFeedback == 1:
        return doUserInteraction(imageStim, None, duration, incorrectSound)
    else:
        return doUserInteraction(imageStim, None, duration, None)

def doTooSlow(allowedKeys):
# calls doUserInteraction with the "too slow" stim, allowedKeys and no timeout
    textStim.color = 'White'
    textStim.text = 'Too Slow!\n\nPlease make your selection faster next time'
    return doUserInteraction(textStim, None, tooSlowTime, None)

def doBlank(duration):
# calls doUserInteraction with blank stim
    textStim.text = ''
    return doUserInteraction(textStim, None, duration, None)

def doPause():
# calls doUserInteraction with blank stim
    textStim.color = 'White'
    textStim.text = 'Please feel free to take a break.\n\nPress any key to continue when ready.'
    return doUserInteraction(textStim, allKeys, None, None)

def doFeedback(response, label, show):
        #print 'true feedback'
        if response == label:
            feedback = 1
            #print "Correct"
            if show == 1:
                showCorrect(feedbackTimeout, soundFeedback)
        elif response == 'NA':
            feedback = 'NA'
        elif response != label:
            feedback = 0
            #print "Incorrect"
            if show == 1:
                showIncorrect(feedbackTimeout, soundFeedback)
        return feedback

def mainExperiment():

    global trialClock, stimCount #reference some variables we will need.
    print 'in main experiment' #just a bit of debug to make sure we know where we are.

    phase = 1 #just in case we want to run multiple runs, or perhaps record training.
    trialClock.reset() #tidy up the clock just to be sure.

    #begins the actual experiment
    for stim in range(len(inputMain)): #this sets up how long the experiment will be. In this case, it will go through the whole inputFile.
        doFixate(fixateTimeout) # Calls the function that presents the fixation-cross
        response = doStimulus(allowedKeys, stimTimeout, inputMain[stim][0], inputMain[stim][1]) # Calls the function that sets the stimulus, then displays it and waits for a response, then saves the output of doUserInteraction as "response"
        if (response["timedOut"]): # we reference the newly gotten "response" object and ask if the "timeOut" value is "True"
            response = doTooSlow(allowedKeys) # if so, we call the function to show the "too slow" message.
        feedback = doFeedback(keyMap[response["firstKey"]], inputMain[stim][2], 1) # we reference the response object from doUserInteraction and the inputFile. Then we call the function that does feedback and we save the output to "feedback"
        stimCount += 1 # we iterate stimCount

        # we write everything we want to the file on a trial by trial basis. That way if anything happens, we only lose at most the current trial.
        dataFile.write('%i %s %s %i %s %s %f\n' %(stimCount, inputMain[stim][0], inputMain[stim][1], inputMain[stim][2], keyMap[response["firstKey"]], feedback, response["duration"]))

        doBlank(ITI) # call a function that shows the ITI (blank screen).

        # This IF asks 2 questions and if they pass, calls a function that shows a "rest" screen
#        if stimCount < trialsBeforeP2 and stimCount % stimBeforeBreak == 0: # Should I still be in this phase? AND is it time for a break?

        if stimCount % stimBeforeBreak == 0: # Is it time for a break?
            doPause() # calls a function that shows a "rest" screen
            print 'break' # print's 'break' to the console (debug)

         # This is an example of how we could hand off to a second "phase" after a specified number of trials
 #       if stimCount == trialsBeforeP2:
 #           doMasterTest()
 #           break

    # Wrap everything up before quitting.
    dataFile.write(datetime.datetime.now().strftime("Experiment Ended: %H:%M:%S")) #adds the final line to the dataFile with the experiment duration.
    textStim.text = 'Thank you for participating in this study.\n\nPlease inform the researcher that you have finished.' # sets some text
    stimUntilAnyKey(textStim) # Shows the "you're done!
    core.quit() # the Deathblow to your experiment.

textStim.text = 'Welcome to your very first experiment! Hooray!\n\n' \
                'This is a Stroop Experiment. As such, you will be presented with a word of a color in varying font colors. ' \
                'Some will match and some will not.\n\n' \
                'If the Word and the font Color match, press "k". If they do Not match, press "d"\n\n' \
                'Please try and respond as quickly as possible.\n\n' \
                'Press any key to begin!'
stimUntilAnyKey(textStim)
dataFile.write('\nDate: ' + str(expInfo['date']) + '\n\ntrial text color congruent response feedback RT\n')
mainExperiment()
