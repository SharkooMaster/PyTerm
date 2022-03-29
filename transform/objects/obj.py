import time
from ..vec2 import vec2

class obj:

    def __init__(self, _screen_w, _screen_h, _w = 1, _h = 1, _x = 0, _y = 0, _char = '#'):

        self.screen_w = _screen_w
        self.screen_h = _screen_h

        self.pos = vec2(_x, _y)

        self.w = _w
        self.h = _h

        self.char = _char
    
    def render(self):
        toRet = []

        x = (self.pos.get_x())
        y = (self.pos.get_y())

        for j in range(self.h):
            toRet.append(int(y + (j * self.screen_w) + x))
            for i in range(self.w):
                toRet.append(int((x + (self.screen_w * j)) + i))

        return list(dict.fromkeys(toRet))
    
    def render_str(self):
        return ((self.char * self.w) + "\n") * self.h
    
    # --- get/set --- #
    
    def get_w(self):
        return self.w
    
    def get_h(self):
        return self.h
    
    def get_pos(self):
        return self.pos
    
    def get_char(self):
        return self.char