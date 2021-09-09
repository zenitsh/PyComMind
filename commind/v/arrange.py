
import commind.core.node

#region is a length mutable list 

def arrangeNodeByRectangle(node):
    for i in node.child:
        arrangeNodeByRectangle(i)
    _height = 0
    for i in node.child:
        _height = _height + i.region[3] - i.region[1]
        i.pos = (-i.region[0],_height-i.region[3])
    _height = _height / 2
    for i in node.child:
        i.pos = (i.pos[0],i.pos[1]-_height)
