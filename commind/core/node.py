
from commind.core.style import Style
from commind.core.nodecontent import NodeContent

class Node:
    def __init__(self,parent=None,text='text',style=''):
        self.style = Style(style)
        self.content = NodeContent(text)
        self.parent = parent
        self.child = []
        self.pos = (0,0)
        self.shape = (len(text)*6,10)
        self.region = [0,0,len(text)*6,10]

    def setImage(self,image):
        self.content.image = image

    def refresh(self):
        self.getRegion()

    def getRegion(self):
        if len(self.child)>0:
            for i in self.child:
                self.region[0]=min(self.region[0],i.pos[0]+i.region[0])
                self.region[1]=min(self.region[1],i.pos[1]+i.region[1])
                self.region[2]=max(self.region[2],i.pos[0]+i.region[2])
                self.region[3]=max(self.region[3],i.pos[1]+i.region[3])
        return self.region
