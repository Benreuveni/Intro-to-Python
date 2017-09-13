from psychopy import visual, event

win = visual.Window(size=(700, 700), fullscr=False, screen=0, allowGUI=False, monitor=u'testMonitor',
                    allowStencil=False, color=[0,0,0], colorSpace=u'rgb', units='cm')

def textInput():
    #until return pressed, listen for letter keys & add to text string
    text = ''
    while event.getKeys(keyList=['escape'])==[]:
        letterlist = event.getKeys()
        print letterlist
        letterDict = {'space': ' '}
#        letterlist=event.getKeys(keyList=['0','1','2','3','4','5','6','7','8','9','backspace'])

        for l in letterlist:
            if l == 'space':
                text += ' '
            elif l == 'return':
                text += '\n'
            #if key isn't backspace, add key pressed to the string
            elif l != 'backspace':
                text += l
            #otherwise, take the last letter off the string
            elif len(text)>0:
                text = text[:-1]
        #continually redraw text onscreen until return pressed

        textObject = visual.TextStim(win=win, ori=0, name='pause', text=text, font=u'Arial', pos=[0, 0],
                                     height=1.0, wrapWidth=None, color=u'white', colorSpace=u'rgb', opacity=1, depth=-1.0)

        # textReport.draw()
        textObject.draw()
        win.flip()
    text = str(text)
    event.clearEvents()
    print text
    return text

textInput()