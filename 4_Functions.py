__author__ = "Ben Reuveni - ben.reuveni@gmail.com"

from psychopy import visual, core, data, event, logging, gui, sound

'''
Now that we have a solid understanding of logical operations (IFs and Booleans) as well as how to perform operations
multiple times (FOR and WHILE loops), let's talk about functions.

Functions can be thought of as modules that perform a specific task(s). A useful analogy would be:

Jellyfish digest everything they eat in a single place (incomplete digestion). That means that all the operations it
needs to do in order to digest food are done in 1 place.

Humans on the other hand, have specialized "modules" that do different things. For example, when you need to digest,
you call on the "digestive tract" module which then calls individual modules like "mouth", "stomach",
"small / large intestines" etc.

OK, enough biology. Let's get back to Functions. Functions are self-contained units of code that perform operations.
In this context, self-contained means that the function is almost like a separate file of code. It really only knows
about things inside the function and unless told, will not impact anything outside of itself.

Functions accept arguments which are like the "Input", and they can return "outputs" (but only if told to do so).

Here's an example:
'''

def selfContainedFunction():
    a = 1+3
    print a

#selfContainedFunction()
#print a

'''
Notice how you get an error for this line. This is because "a" was defined Inside a function and as such, it is not
accessible outside that function. This is what it means to be "self contained". This also means that you can reuse
variables inside a function that have already been defined outside of it since they don't ever see each other (though
I'd recommend you not).

make sure to comment out that erroneous "print a".

On the other hand:
'''

def selfContainedFunction():
    a = 1+3
    print a
    return a
#print selfContainedFunction()

'''
As you can see, this works. So what changed? Well, for one thing, we added a "return" statement. The "return" statement
tells the function to pass on information from within the function to outside of it.

We then told it to "print" the function which resulted in printing "a" since it was the only thing returned. Now you might
be wondering what would happen if you added a "print" command to line 29. Go ahead and try.

The reason that happens is because we did not tell the function to return anything.

Now let's say that we want the function to return a value "a", but we want to use it somewhere else. We could use
selfContainedFunction() in the place of "a" throughout our code, but that seems unwieldy. Instead, we can do the following:
'''

def selfContainedFunction():
    a = 1+3
    print a
    return a
#a = selfContainedFunction()
#print a

'''
As you can see, all we did was assign the output of that function to a variable. Since the variable is in "global" space
meaning not in a function, it is now accessible to everything. I should also note here that Functions have full access
to information defined outside of themselves. So the following works:
'''

b = 1
def selfContainedFunction():
    print b
#selfContainedFunction()

'''
Now, functions are extremely useful because they allow you to segment your code in such a way that each operation
you wish to perform happens in a module that you can reuse instead of duplicating code every time you want to do that
operation.

The usefulness of Functions is further expanded because of the fact that they can accept inputs (called arguments).
For example:
'''

a = 1
b = 2
c = 3

def doAddition(first, second):
    d = first + second
    return d

d = doAddition(a, b)
#print d

e = doAddition(c,d)
#print e

'''
As you can see, when we created the function, we defined 2 arguments that it accepts (the names of which are arbitrary).
Once we've defined an argument, we can then reference it anywhere within the function and it will inherit the value
of what we fed into the function.

Try and play around with adding print statements into the function above such as "print first". Notice how the output
changes because of what arguments were passed to the function. It is also useful to note that sometimes you may pass
an argument to a function but not use it. You may wish to do this so that you can call a Second function from within
the first and pass that value along.

For example:
'''

def firstFunction(a,b,c):
    d = a+b
    return secondFunction(c,d)


def secondFunction(c,d):
    e = c+d
    return e

#e = firstFunction(1,2,3)
#print e

'''
Let's break that down:

We define 2 functions, each of which take arguments, however the first function doesn't use "c" except as a pass-through.
The first function then calls a second function with 2 arguments and is told to "return" the output of that second
function.

Within the second function, we take arguments, do something to them, and return a value.

So the flow goes:

Call Function 1 with appropriate arguments -> function 1 does something and then calls Function 2 -> function 2 takes
arguments, does something and returns a value to function 1 (since it is the one who called the function). Function 1 knows
that it needs to return (to whatever called it) the output of the second function. We store the output of function 1 in a
variable "e" and then print e.

If all that seemed confusing, keep in mind that Functions return values to the thing that called them. I usually find it
easiest to start from the end and work back to the original caller.

Now that we have a basic understanding of functions, let's put it to use:

Create a function that takes 3 arguments:

1) a keypress that you've captured (use the event.getKeys() command)
2) the correct response
3) whether or not to print the result

The function should check to see whether the keypress matches the correct response (that is housed in a list that you
indexed in order to pass as an argument) and then both prints, and outputs a new variable that is either 0 for
incorrect or 1 for correct.

Hint: This will involve at least a few IF statements and a function.

Don't forget to call the function at the end.


Feel free to use what you've learned in "If statements" BUT I really really recommend you do NOT cut and paste it. Instead
a much better way to cement your understanding is to recode it all from nothing.
'''

# code goes here #


'''
Great! Now that we have a function that accepts input, matches it and spits out a "grade" , we can simply call that
function anywhere we like instead of dumping all that code everywhere we may need a "grade". Much elegant! So Code!

Let's try something new:

Until now, we've been playing around with non-visual operations which is a little boring. Let's see how we draw an image
to the window.

PsychoPy has various predefined objects that make all this very easy. For example:
'''

#win = visual.Window(size=(700, 700), fullscr=False, screen=0, allowGUI=False, monitor=u'testMonitor',
#                     allowStencil=False, color=[0,0,0], colorSpace=u'rgb', units='cm')

textStim = visual.TextStim(
    win=win, ori=0, name='', text='+', font='Arial',
    units='cm', pos=[0, 0], height=1, wrapWidth=None,
    color="white", colorSpace='rgb', opacity=1, depth=0.0)

imageStim = visual.ImageStim(
    win=win, name='', image='Correct.png', mask=None, ori=0,
    pos=[0, 0], size=[10.0, 10.0], color=[1,1,1], colorSpace=u'rgb',
    opacity=1, texRes=128, interpolate=False, depth=-2.0)

correctSound = sound.SoundPyo(value=500, secs=0.5)
woohoo = sound.SoundPygame(value = 'Woohoo.wav')

'''
The "textStim", "imageStim" and "correctSound" are arbitrary names I gave to a particular object, in this case,
a TextStim, ImageStim and SoundStim.

Once they are defined, we can call them wherever and however many times we like. We can also modify them "on the fly"

There are several ways to draw stuff to the window depending on whether you want it to be continuously drawn, or
drawn for a single frame, etc. Also, it is important to note that PsychoPy utilizes a buffer space. You can think
of a buffer space as an area of memory that is "visually hidden" from the user to which we can draw stuff before we show
it so that we don't run into situations where we want to draw something but it isn't ready yet for whatever reason.

Let's take a look:
(make sure you've uncommented line 183 and 184)
'''

 # imageStim.setAutoDraw(True)
 # core.wait(2) # this command just tells PsychoPy "Don't do ANYTHING for the next X seconds, then carry on as normal"
 # imageStim.setAutoDraw(False)

'''
Did anything show up aside from the window?

The reason it did not is because, while we told PsychoPy to AutoDraw the image (which means keep on drawing it every frame
until I say otherwise), we did not tell PsychoPy to expose the "buffer" to us. Therefore, the image was being drawn
"behind the scenes".

We can expose it with the win.flip() command. Insert it directly after the imageStim.setAutoDraw(True) command.

We may also want to print text to the screen. This is done exactly the same way as drawing an image.
Change imageStim to textStim. You'll notice it printed a " + " to the screen. Let's say we want to change what it prints
but we don't want to "hard code" it before we hit "RUN".

We can easily accomplish this with the following command: textStim.text = "Hello World!"

Add that command right before you tell PsychoPy to draw the text stim.

Next, we may also want to play a sound. This is done with the .play() command. Try and add a command to the above
code that will also play a sound for us. The sound duration is currently set at 0.5s.

Note that while this sound is currently set to a particular Hz, we can also point it to a sound file like so:

woohoo = sound.SoundPyo(value = 'Woohoo.wav')

Note: I haven't been able to get mp3s to play, I believe it has to do with copyright material so .wav are likely the
way to go. If you figure it out, let me know :)
'''

#woohoo.play()

'''

OK, now that we know how to present images, let's create a for-loop that calls a function which displays
an image for X seconds.

Here are the parameters:

Which image to draw will come from an array of images. Instead of creating an ImageStim for every image you want to
show, find a way to change the existing ImageStim to show a different image each time. Hint: Remember how we changed the text?

So the For-loop will dictate how many images you will show, and it will also dictate which image to show. The for-loop
should call a function that actually shows the image.

The function should take arguments that control whether we're drawing an ImageStim or TextStim, and how long to display
it for.
'''

# code goes here #
