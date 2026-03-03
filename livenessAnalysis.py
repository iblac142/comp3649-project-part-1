import token
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
        if l.getSRC1().getTag() == token.VARIABLE or l.getSRC1().getTag() == token.TEMP:
            currentLive.add(l.getSRC1())
            varSet.add(l.getSRC1())
        if l.getSRC2().getTag() == token.VARIABLE or l.getSRC2().getTag() == token.TEMP:
            currentLive.add(l.getSRC2())
            varSet.add(l.getSRC2())
        # set the intermediateLine's live variables to the current set of live variables
        for i in currentLive:
            l.liveness.add(i)
        # remove the destination from the list of current variables, as it has been defined 
        currentLive.discard(l.getDST())
    return varSet