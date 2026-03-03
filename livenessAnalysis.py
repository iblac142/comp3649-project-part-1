import token
import intermediateLine

#TODO: catch error for live variable not occuring in code

def setLiveness(lines, lives):
    currentLive = set()
    varSet = set()
    for v in lives:
        currentLive.add(v)
        varSet.add(v)
        
    for l in reversed(lines):
        if l.getSRC1().getTag() == token.VARIABLE or l.getSRC1().getTag() == token.TEMP:
            currentLive.add(l.getSRC1())
            varSet.add(l.getSRC1())
        if l.getSRC2().getTag() == token.VARIABLE or l.getSRC2().getTag() == token.TEMP:
            currentLive.add(l.getSRC2())
            varSet.add(l.getSRC2())
        for i in currentLive:
            l.liveness.add(i)
        currentLive.discard(l.getDST())
    return varSet