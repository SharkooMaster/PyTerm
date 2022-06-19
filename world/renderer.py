
import time
import threading
import os

from transform.vec2 import vec2
from input_.input_handler import input_handler as inp

class renderer:

    def __init__(self, _screen_h, _screen_w, _debugger, _char):
        self.debugger = _debugger

        self.debugger.log("renderer init debugger")

        self.screen_w = _screen_w
        self.screen_h = _screen_h

<<<<<<< HEAD
        self.grid = (((_char * self.screen_w) + "\n") * self.screen_h)
=======
        self.grid = (((" " * self.screen_w) + "\n") * self.screen_h)
>>>>>>> 209570cf0f003661a168b588278b009715fba662

        self.objs = []

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def get_obj(self):
        return self.objs

<<<<<<< HEAD
    # 'p' position,
    # 's' scale,
    # 'c' char,
    def edit_obj(self, _obj, _arg):
        if("p" in _arg):
            index = self.get_objIndex(_obj)
            if("x" in arg): self.objs[index].pos = vec2(self.objs[index].pos.x + int(_arg[2:]), self.objs[index].pos.y)
            if("y" in arg): self.objs[index].pos = vec2(self.objs[index].pos.x, self.objs[index].pos.y + int(_arg[2:]))

    def get_objIndex(self, _obj):
        return self.objs.index(_obj)
    
=======
>>>>>>> 209570cf0f003661a168b588278b009715fba662
    def add_obj(self, obj):
        self.objs.append(obj)

    def inject_objs(self):
        grid_clean = self.grid.replace("\n", "")
        tempGrid = list(grid_clean)

        for obj in self.objs:
            for pos in obj.render():
                tempGrid[pos] = obj.get_char()

        for j in range(self.screen_h):
            tempGrid.insert((j * self.screen_w) +(j), "\n")

        self.grid = ''.join(tempGrid)

    def render(self):
        while True:
            self.cls()
            self.inject_objs()

            print(self.grid)
            time.sleep(0.5)
