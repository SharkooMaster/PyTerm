
class vec2:

    global x
    global y

    def __init__(self, _x, _y):
        global x
        global y
        x = _x
        y = _y
    
    def pos(self):
        global x
        global y
        return [x,y]
    
    def pos_str(self):
        global x
        global y
        return str(f"({x},{y})")
    
    def translate(self, _x=None, _y=None):
        global x
        global y
        if(_x != None): x += _x
        if(_y != None): y += _y
    
    # --- get/set --- #
    
    def get_x(self):
        global x
        return x
    
    def get_y(self):
        global y
        return y