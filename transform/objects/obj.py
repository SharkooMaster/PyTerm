import time
from ..vec2 import vec2

class obj:

    global screen_w
    global screen_h

    global w
    global h
    global pos

    global char

    def __init__(self, _screen_w, _screen_h, _w = 1, _h = 1, _x = 0, _y = 0, _char = '#'):
        global screen_w
        global screen_h
        global w
        global h
        global pos
        global char

        screen_w = _screen_w
        screen_h = _screen_h

        pos = vec2(_x, _y)

        w = _w
        h = _h

        char = _char
    
    def render(self):
        global screen_w
        global screen_h
        global w
        global h
        global pos
        global char

        toRet = []

        _x = (pos.get_x())
        _y = (pos.get_y())

        for j in range(h):
            toRet.append(int(_y + (j * screen_w) + _x))
            for i in range(w):
                toRet.append(int((_x + (screen_w * j)) + i))

        return list( dict.fromkeys(toRet) )
    
    def render_str(self):
        global w
        global h
        global char
        return ((char * w) + "\n") * h
    
    # --- get/set --- #
    
    def get_w(self):
        global w
        return w
    
    def get_h(self):
        global h
        return h
    
    def get_pos(self):
        global pos
        return pos
    
    def get_char(self):
        global char
        return char