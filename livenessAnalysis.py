import tokenizing
import intermediateLine

#TODO: catch error for live variable not occuring in code

# takes a list of intermediateLines and adds liveness information to each
#
# lines: the list of intermediateLines
# lives: the variables live at the end of the code block
#
# returns the set of all variables that appear in the block
def setLiveness(lines, lives):
    # create empty sets; one for what variables are currently live, and one for all variables used
    currentLive = set()
    varSet = set()
    # add the final live variables to both sets
    for v in lives:
        currentLive.add(v)
        varSet.add(v)
    
    # traverse from the bottom up
    for l in reversed(lines):
        # add each src to the currentLive set; their appearance indicate they are consumed following the instruction
        if l.getSRC1().getTag() == tokenizing.VARIABLE or l.getSRC1().getTag() == tokenizing.TEMP:
            currentLive.add(l.getSRC1())
            varSet.add(l.getSRC1())
        if l.getSRC2().getTag() == tokenizing.VARIABLE or l.getSRC2().getTag() == tokenizing.TEMP:
            currentLive.add(l.getSRC2())
            varSet.add(l.getSRC2())
        # set the intermediateLine's live variables to the current set of live variables
        for i in currentLive:
            l.liveness.add(i)
        # remove the destination from the list of current variables, as it has been defined 
        currentLive.discard(l.getDST())
    return varSet

# Analyze input for correct syntax and break down live variables into a list
# If syntax is incorrect return 0
def liveness_check(liveness):
    livenessCheck = liveness[:5]
    liveness = liveness[5:]
    if (livenessCheck != "live:"):
        print ("Error: Last line is not in form live: ")
        return 0

    liveness = liveness.replace(" ", "")
    operation = liveness.split(',')

    liveVar = []
    if (operation == ['']):
        return liveVar
    for var in operation:
        t, empty = intermediateLine.checkVar(var)
        liveVar.append(t)
    
    return liveVar