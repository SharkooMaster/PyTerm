
import time
import os

class renderer:

    global screen_w
    global screen_h

    global grid

    global objs

    def __init__(self, _screen_h, _screen_w):
        global screen_w
        global screen_h
        global grid
        global objs

        screen_w = _screen_w
        screen_h = _screen_h

        grid = ((("i" * screen_w) + "\n") * screen_h)

        objs = []

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')
    
    def get_obj(self):
        global objs
        return objs
    
    def add_obj(self, obj):
        global objs
        objs.append(obj)
    
    def inject_objs(self):
        global screen_w
        global screen_h
        global grid
        global objs

        grid_clean = grid.replace("\n", "")
        tempGrid = list(grid_clean)

        for obj in objs:
            for pos in obj.render():
                tempGrid[pos] = obj.get_char()
        
        for j in range(screen_h):
            tempGrid.insert((j * screen_w) +(j), "\n")
        
        grid = ''.join(tempGrid)
    
    def render(self):
        global screen_w
        global screen_h
        global grid

        while True:
            self.cls()
            self.inject_objs()

            print(grid)
            time.sleep(0.5)