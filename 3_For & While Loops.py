from psychopy import visual, core, data, event, logging, gui, sound

'''
 Before we begin, let's learn how to create a "window" using PsychoPy. A window can be thought of as your "Canvas". The
 area in which we will be drawing stuff like text and images to. It also creates an environment for capturing keys, etc.
 Without a window, PsychoPy has no way of knowing where to "listen".

 PsychoPy makes this easy with the visual.Window command. Most of the attributes are self-explanatory.
 '''

win = visual.Window(size=(700, 700), fullscr=False, screen=0, allowGUI=False, monitor=u'testMonitor',
                     allowStencil=False, color=[0,0,0], colorSpace=u'rgb', units='cm')

'''
 Once we've defined a window, we will need to tell each thing we want to draw to the screen to use That window.

 Now that we understand IF statements, we can move on to loops.

 Imagine you have an operation, but you want it to run more than once. This is where FOR and WHILE loops come in!

 Let's start with FOR loops. A FOR loop is a framework that executes arbitrary code an arbitrary *but FINITE* number of times.

 For example:
'''

for x in range(10):
    print x

# Notice the new variable "x" (it could have been anything I wanted - y, z, a, bob)

for bob in range(10):
    print bob

'''
 The value of x (or bob) will change with each iteration of the FOR loop. So on the first time around, x is equal to
 the first value in the range (in this case 0). The second time around, x == 1 and so on through "range(10)"

 The "range(start,stop)" command is a quick way of saying "I want all the numbers in this range".
 Note that when we want to start from 0, we can omit the "start" argument since it's obvious.
 Set up a FOR-loop and try and print out all number from 1 to 8 including 8.
'''

# code goes here #

'''
 You might have had the notion that this can be used to iterate over trials and stimuli through indexing! You'd be right!

 Now let's try and build our own FOR loop.
 Create a list of 10 colors (i.e ['red', 'blue', ...]) make sure you set up a variable to hold it, and that they are strings!

 Next, create a FOR loop that goes through the list and prints out each color name in sequence. You'll need to use
 indexing to get this to work.
'''

# code goes here #



'''
 Great! FOR loops are very very powerful and can help us automate wildly time consuming operations.

 Now, what if we want something to loop indefinitely until something interesting happens?
 For example, what if we want the program to do some operation (count/wait/listen) until a pre-determined condition is met?

                                    ### *** !!! VERY IMPORTANT !!! *** ###

 If you do not specify an "Exit" clause, a while-loop can seriously mess things up because it dominates your CPU.
                            MAKE SURE YOUR WHILE LOOP HAS A WAY OUT BEFORE YOU RUN IT!!!
'''

counter = 0

# while (counter < 11): # this is our exit clause.
#     counter += 1 # this ensures that our exit clause will be met.
#     print counter # this just lets us follow where we currently are.

'''
 Remember that really annoying game "7 Boom"? You start counting, and any time you reach a number divisible by 7
 you say "boom" instead of the number.
 Let's code that game! Here are the guidelines:

 Create a variable to hold 7 - that way we can easily modify it to be 8 Boom or 21 Boom.
 Create a counter variable as above. Feel free to reuse the above, but make sure you set it to 0!
 Create a while loop that has an IF statement in it.
 Each time around, the while loop should ask "is counter divisible by 7? if so, print BOOM! If not, print the number.

 Play this game until you hit 100.

 Remember, to make sure your while loop has a way to exit the loop!
'''

# code goes here!



'''
 Great! Let's make one more.
 Before we start, a very common way to setup While loops is to use True/False as the break points.

 You might say:

while (true):
    <do something>

 You can then include an IF statement to check whether it's time to break the while-loop and if that IF is triggered
 you use the command: break.
'''

p = 10
k = 0
# while(True):
#     print('in the while')
#     p -= 1
#     if p == k:
#         print ('exiting the while')
#         break


# Another way to break a while loop is to set a variable to True and then later set it to False.

m = True
p = 10 # remember to reset variables you want to reuse. Otherwise they retain their previous value!
k = 0
# while(m): # this is shorthand for "while(m == True)"
#     print('in the while')
#     p -= 1
#     if p == k:
#         print ('exiting the while')
#         m = False # this means that the very next thing the computer does is go back to the "while(m)" line and
#                   # evaluate whether or not it's True. Suddenly, it's False, and so the "While-Loop" is not triggered!


'''
 OK, enough fun and games! We're here to do science!

 Let's work on a new While Loop that has 2 ways to exit.
 First set up the variables you'll need, then start working on the While-Loop.

 Previously, we simulated time elapsing by creating a counter and setting it to some value, now it's time to learn
 how to reference actual usable time! (pardon the pun).

 First, we set up a counter to track the time. PsychoPy gives us a great way to track time with the core.Clock() function.
 Here is how we use it:

 Set up a variable to hold the clock object
'''
trialClock = core.Clock()

# Once we have a clock, we can use the .getTime() to pool the system for the current time.

currentTime = trialClock.getTime()
#print currentTime
#print trialClock.getTime()

'''
 Next, we need a way to capture user input!
 Psychopy has an easy way of capturing keyboard events! It is called event.getKeys()

 Here is how we use it:
 We set a variable to hold any keys that are pressed
 In the () we get to specify which keys are allow to be pressed. If we leave it blank, all keys are allowed.
 We can also pass a list to event.getKeys(listOfKeys).
'''

allowedKeys = ('space', 'd', 'k') # make sure they are strings!
keys = event.getKeys(allowedKeys)
'''
 This initializes the "listener" and after this line, the program is "listening" for
 keys. Note that each time you invoke event.getKeys() it resets the buffer.
'''
#print keys[0] # print the first key to be pressed. Does this work? Can you figure out why or why not?
#print keys # print all keys that were pressed.

# Here's a better example:
pressed = []
# while (True):
#     x = 0
#     keys = event.getKeys(allowedKeys)
#     if len(keys) > 0:
#         pressed.append(keys[0])
#         x += 1
#         print keys
#     if len(pressed) > 2:
#         'All done!'
#         break

'''
 Consider what happens to "pressed" when the first key is pressed. HINT: consider using the len() function.

 OK now that we have the framework for both tracking time, and tracking user-input, we're almost home!

 The first exit clause is if keyPressed == 1 (you'll need to set it up).
 The second is if timeOut == 1. This should be triggered if the timer hits endTime before a key is pressed.

 So we'll need to keep track of whether a key was pressed, AND whether the current time is lower than our endTime time.

 Here's some help :)
'''

startTime = trialClock.getTime()
timeOut = 10 # this is in seconds.
endTime = startTime + timeOut

'''
 Think about where you want to place the 3 variables I just created. Should they be IN the while-loop or outside it?
 What's the difference?

 So, your While-Loop will consist of at Least 2 IF statements (or perhaps 1 IF statement and an elif).

 MAKE SURE YOU GIVE YOUR WHILE LOOP A WAY OUT BEFORE YOU RUN IT!
'''

# Code goes here #