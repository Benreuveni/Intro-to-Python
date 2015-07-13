import math # this pulls the "math" module into memory and allows us to use all of its functions (like the value of Pi).

'''
 Variables are sections of memory that can hold data. This is the basis of nearly everything else we're likely to do.

 In Python, variable names are restricted to strings. A string is any combination of characters
 (not numbers - unless forced). So, we can name our variables anything from "x" to "stimTrialTimeout".

 When creating variables, it is customary to write in "camelBack" notation. Your first word is all lowercase, and
 each subsequent word has its fist letter capitalized.

 Also, try and be very explicit as to what the variable is / is used for. You may find it obvious while coding, but
 10 months from now you're going to wish you did.

 Here are some examples:

 Delete the '#' in front of the "print" commands and run the program to see the output. You may need to re-comment
 some of the lines as not all of them will work.
'''

a = 2
#print a

x = "24th letter of the English alphabet" # notice that we've included numbers in our string, but since they are between
#print x                                  # " " they are *forced* into a string.

stimTimeout = 2.25 # it can be a number as well.

# Note that since we have made "stimTimeout" literally equal to a number, we can then do math with that variable

#print ((stimTimeout + 5) / stimTimeout) * math.pi

L1 = [1,2,3] # variables can also hold lists and arrays!
#print L1

L2 = ['s',1,'b',2] # in this case, we have a list of both strings and numbers.
#print L2

L3 = [1,2,a,x] # in this case, we have a list that holds numbers and other variables!

# Try and guess what it will print before you try.
#print L3

L4 = [L1,L2,L3] # in this case, we have a list of lists! This is also called a multi-dimensional array (or matrix).
#print L4

L5 = [[1,2,3], [4,5,6], ['j','p','g'], [7,8,9]] # this is a 2D array that has 4 rows and 3 columns. Imagine each [ ]
                                                # stacked on top of the next

# [ 1,  2,  3 ]
# [ 4,  5,  6 ]
# ['j','p','g']
# [ 7,  8,  9 ]


'''
 Let's switch gears and talk about Operators before getting back to lists.

 Operators are things like +, -, *, /
 They allow us to manipulate numbers (mostly). I'll list as many as I can think of, and what they do

 -, /, *  these do exactly what you think they do: they only apply to Numbers.

 +  plus is a special operator in that it can apply to numbers or strings. For example:
'''
#print 2+2 # will yield 4 (or 5 depending on Big Brother).

answer = "4" # setup a variable that holds a STRING "4" *not a number*

#print "the answer to the above is " + answer

#print "the answer to the above is " + 2

'''
 This will fail. The reason it fails is because you're trying to mix between strings and numbers.
 We can tell Python to force 2 into a string with the str() command. Add a # to comment the failed print command.
'''

#print "the answer to the above is " + str(2)

# similarly, we can force strings into numbers with the int() command.

e = "2"

#print 2 + e # this will fail because e is a string.

#print 2 + int(e) # taadaaam! (remember to comment out the above failed print command.

'''
 Next we have =, ==, !, !=, +=, -=

 = is what it looks like. It sets one thing equal to another.
 == attempts to evaluate whether the equation is in fact equal "are these two things the same?"
 ! this is "Not". so !true == false.
 != is "not equal" so true != false.
 += means take whatever value is on the left, and add whatever value is on the right:
 2 += 3 == 5
 int(e) += 3 == 5. Note that this is shorthand for int(e) = int(e) + 3
 -= is the same, but subtraction.


 Next up is % (modulo). This is a seemingly cryptic, but Very useful operation.
 It divides two numbers and returns the remainder
'''

#print 2 % 2 == 0 # this will evaluate to "true" because 2 can be divided by 2, and the remainder is 0

#print 5 % 2 == 1 # this will evaluate to "true" as well. 5 can be divided by 2 exactly 2 times, and leaves a remainder of 1.

numerator = 9
denominator = 3

#print numerator % denominator

#print numerator % denominator != 0 # evaluates to False because 3 divides into 9 exactly 3 times with a remainder of 0

# let's talk about some useful commands you are likely to use.

# len(object) returns the length of the object passed.

q = "hello"
L1 = [1,2,3] # don't worry about what [] are just yet. They're lists!
len('hello') # returns 5 because "Hello" is 5 letters long.
len(q) # returns 5 because q is literally equal to "Hello", and that is 5 letters long.
len(L1) # returns 3 because L1 has 3 items in it.

# array.append

a = []
#print a
a.append(1)
#print a

'''
##### Before we move on to dictionaries, let's cover indexing! #####

 Indexing is exactly what it sounds like. When we have a list, we may want to reference a particular value in that list.
 For example, let's say that we want to print just the "b" in L2'. There are 3 very important things to keep in mind
 when indexing in Python.

 1) Python is base 0 (Zero) which means that the first item in any list is in position 0, not 1!
    So a list with 10 items looks like this in terms of index position [0,1,2,3,4,5,6,7,8,9]. Remember this :)

 2) Python is a non-inclusive counter. Meaning, it starts from the number you indicate, and goes up *BUT NOT INCLUDING*
    the end number. For example: telling Python to count from 1 to 10 will yield 1,2,3,4,5,6,7,8,9

 3) In a 2D array (X columns and Y rows), we index ROWS then COLUMNS (Y,X notation). Weird, but so.

 Remember L5? It is easier to "see" the 2D structure if we think of it like this:

 [ 1,  2,  3 ]
 [ 4,  5,  6 ]
 ['j','p','g']
 [ 7,  8,  9 ]

 Before running this print command, I urge you to make a prediction.
 After you run it, try and make it print the "p". What about the 9?
'''

#print L5[0][0]

# Just to be safe, let's examine a 3D array (now without glasses!)

L6 = [ [ [1,2,3], [4,5,6], [7,8,9] ], ['a','b','c'],['d','e','f'] ]

'''
# Sadly, I can't depict a 3D array here, but just think of it as cartesian coordinates. (Z,Y,X)

 Consider what is happening here. Don't worry if you feel a bit lost with all the []s going on.
 The outermost [] captures the whole array.
 the next set of [] captures both the numbers and the letters.
 the next set of [] captures only the numbers.
 finally, the innermost [] captures each set of numbers or letters.

 Take a moment a play around with this print line and indexing. It is unbelievably important that you be comfortable
 with indexing and navigating lists and arrays. Otherwise, you may end up pointing to a wrong answer in a grading script!

 The indexing syntax is the same as for a 2D array. The first [] points to the outermost division of groupings
 the next [] points to the next level in, and the final (because it's only a 3D array) points to the innermost grouping.

 How would you tell it to print:

 Only the numbers.
 Only the letters.
 Only "[4,5,6]"
 Only "e"
 add 2 + 6 using indexing!
'''

#print L6


'''
                                   ###### Dictionaries ######
'''

D1 = {1: a, 'coffee': "GIMME!"}

'''
 This is a dictionary. Its syntax is { item: definition, item: definition, etc. } just like a real dictionary!

 So if we reference this dictionary with the number 1, it will return the definition of 1 that we set up.
 Dictionaries are arbitrary, meaning they can hold anything that a variable can hold.

 In this case "a". Try and guess what this will print out! Think carefully!
'''
#print D1[a]

'''
 Dictionaries differ from lists in that you can use it to map several variables to a single one.
 for example:
'''

D2 = {1: 10, 2:10, 3:10}
#print D2[3]

'''
 Notice that this looks a lot like indexing, and it is! But it is not the same as indexing lists.
 Here, the index does not point to a particular position, but rather to a particular value.

 Remember that Python is base 0 (zero). D2 has 3 items in it so the positions would be 0,1,2
 If we were indexing position, D2[3] would return an error since there is no just position.

# Dictionaries can also be used to manage information.
'''

D3 = {
    "rt": a,
    "response": None,
    "label": L2[1],
    "stimID": L6[0][0][0]
}

# Don't be confused because it's vertical rather than horizontal. It's the same as
D3 = {'rt': a, 'response': None, 'label': L2[1], 'stimID': L6[0][0][0]}

# The difference is purely aesthetic and personal. Some people find vertical more human-readable, some don't.

# Try and print out various items.
#print D3

# Can you reassign "rt" to be 42? Hint: Consider what value you want, and where you want to store it.

# code goes here#

'''
 Now, you can see how we might use a dictionary to store information we want and reference it later. It's a nice
 bundled package that has the advantage that we only need to "keep track" of 1 variable instead of 4.

 There are a bunch more things to learn in Python, but for our purposes, this is all you "Need" in order to be on
 firm ground! Let's move on!
'''