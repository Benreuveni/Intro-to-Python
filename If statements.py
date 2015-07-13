'''
 Logic is the bread and butter of machine states.
 Everything we do with computers rests on formal logic and Boolean notation.

 The if / elif / else is one of the most powerful tools in your arsenal.
 You can think of them as a set of conditional triggers.

 if <so and so is true>:
   <do X>
 elif <so and so is true>: # elif stands for "else if"
   <do Y>
 elif <so and so is true>:
   <do Y2>
 else <if none of the previous things are true>
   <do Z>

 Let's try and create our own If statement!
 We'll start simple:
'''

x = 10

if x == 10:
    print "They are equal"
elif x != 10:
    print "They are not equal"
else:
    print "I'm confused!"

'''
 Here we ask whether x is the same as 10, if so, it triggers a particular "conditional"
 IF it has NOT triggered a conditional, it moves on to evaluate the next conditional the "elif"
 Finally, if neither of the two conditions are met, it will always execute the "else" conditional which is why
 we didn't need to specify any conditions on that line.

 A few notes on IF statements:

 1) You can chain an arbitrary number of elifs.

 2) elifs are more efficient than a bunch of "ifs" because an elif does not Have to be evaluated. An "If" does.
    each evaluation the computer has to do eats up some processing time, which in turn slows things down.

 3) a conditional can trigger an arbitrary number of things to execute

 4) you can "nest" multiple ifs within each other.
'''

# if x == 10:
#     if x % 10 == 0:
#         if x - 10 == 0:
#             if x - 1 != 8:
#                 print "They are equal"
# elif x != 10:
#     print "They are not equal"
# else:
#     print "I'm confused!"

# The computer came to the first IF and it evaluated to "true", it then evaluated each successive IF until it was done.

# In this example, what would happen if the seoond or third nested if failed? Try and break it to get a different print.
# Note that the "elif and the else" in this case are not evaluated since the first If is true.

#Ok! Let's try and make a "grading" If statement for our experiment!

response = 1
label = 2
show = 1

'''
 I have set up 3 variables for you that are currently static, but will eventually be pulled from either
 the user (response), or the input file (label, show).

 Let's make some logic that will evaluate whether or not the response is the same as the label.
 Based on the outcome of that evaluation, set a new variable called "feedback" to either 0 or 1.

 Then based on the value of "show" (0/1), print out "correct" or incorrect.
'''

# code goes here #



# Woot! Well done! You now have an automated way of grading user responses in "real time".

startTime = 0
timeOut = 2
endTime = startTime + timeOut

currentTime = 1

'''
 Next, make a new IF statement that checks to see the current time is outside our "time window"
 If it is, print something to the effect of "Too slow!" and create a new variable called "timedOut" and set it to 1.
 If it isn't, print something to the effect of "all good". Set timedOut to 0.
'''

# code goes here#

'''
 Lastly, let's talk about Boolean operators (AND, OR)
 These arguments are useful if we want to make complex conditionals:
 "Only trigger IF x AND y are True"
 "Only trigger IF x OR y are True"

 NOTE: These are "short-circuit" operators meaning that the second statement is ONLY evaluated if the first one is True

 So in the case of the AND statement below, since 7 is !> 9, the IF statement does not even bother looking at whether 9 < 10.

 In the case of the OR statement, since 7 is !> 9, it will ask whether 9 < 10. But if the first clause were True,
 it would not bother with evaluating the second conditional.
 '''

# if (7 > 9 and 9 < 10):
#     print "true"
# else:
#     print 'false'
#
# if (7 > 9 or 9 < 10):
#     print "true"
# else:
#     print 'false'
#
# a = 7
# b = 9
# c = 10
# d = 3
#
# if (a > c and b % d == True):
#     print "true"
# else:
#     print 'false'
#
# if (a > c or b % d == True):
#     print "true"
# else:
#     print 'false'