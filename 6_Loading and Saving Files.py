# Import relevant libraries
from psychopy import data
import numpy as np  # whole numpy lib is available, prepend 'np.'

'''
 OK!

 Now that we've covered variables, IFs FORs, WHILEs and FUNCTIONS, we're nearly there!

 The last bit we need to cover is how to load files and how to write to files. These are made very easy by Python.

 To load a file that has numbers and strings:
'''

mixedFile = np.genfromtxt('Stroop_Input.txt', dtype=None)
#print mixedFile[0]

'''
 As you can see, we have loaded a txt file and assigned it to a variable. We can now reference that variable as though
 it were the txt file.

 There is another way to load files if you have No Text in them.
'''

numbers = np.loadtxt('just numbers.txt')
#print numbers

'''
 In order to write to a file, we must first create a file, and then add data to it. Note that you can only write
 STRINGS to a file. But don't worry, writing str(1) - which forces 1 into a string - will result in 1 and not '1' in
 your data file.

 For example:
'''

data = open('dataFile.txt', 'w')


# now that we have a new *empty* file, we can start adding data to it.

# data.write(str(1)+'\n')
# data.write('a,b,c\n')

# A more advanced way of writing to a file:

# data.write('%i %f %s\n' %(1, 1.11, 'd'))

'''
 Let's break that down. What we see is a series of % values, and then a % and a reference. What this means is:

 "I want an [integer] followed by a space, followed by a [float] followed by a space, followed by a [string] followed by
 a [new line]. We then specify what particular [integer][float][string] we want. Note that these do not have to be static
 and can be variables.
'''

i = 1
f = 0.9975
s = "string"

# data.write('%i %f %s\n' %(i, f, s))

'''
 It is important to note that once you specify the type of thing you're going to write (ie: %i) you MUST pass it an
 appropriate instance of that thing. So we cannot do the following:
'''
i = "1"
f = 0.9975
s = "string"

# data.write('%i %f %s\n' %(i, f, s))

'''
OK! We've covered pretty much everything we need in order to build our experiment!

There are a few little things that I'll give you, but they are really specific (like how to create a gui dialog box), etc.
'''
