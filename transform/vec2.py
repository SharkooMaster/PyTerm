
class vec2:

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    def pos(self):
        return [self.x,self.y]
    
    def pos_str(self):
        return str(f"({self.x},{self.y})")
    
    def translate(self, _x=None, _y=None):
        if(_x != None): self.x += _x
        if(_y != None): self.y += _y
    
    # --- get/set --- #
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y