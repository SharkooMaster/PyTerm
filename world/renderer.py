
import time
import threading
import os

class renderer:

    def __init__(self, _screen_h, _screen_w, _debugger):
        self.debugger = _debugger

        self.debugger.log("renderer init debugger")

        self.screen_w = _screen_w
        self.screen_h = _screen_h

        self.grid = (((" " * self.screen_w) + "\n") * self.screen_h)

        self.objs = []

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def get_obj(self):
        return self.objs

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
