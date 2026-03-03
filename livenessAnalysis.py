import token
import intermediateLine

def setLiveness(lines):
    currentLive = set()
    for l in reversed(lines):
        currentLive.add(l.getSRC1())
        if l.getSRC2().getTag() == 2 or l.getSRC2().getTag() == 3:
            currentLive.add(l.getSRC2())
        for i in currentLive:
            l.liveness.add(i)
        currentLive.discard(l.getDST())