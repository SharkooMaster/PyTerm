
from transform.objects.obj import obj
from world.renderer import renderer
from conf import conf
from threadingHandler import threadingHandler

import time

class main:

    def __init__(self):
        # PreProcess
        self.debugger = conf().get_debugger()
        self.debugger.log("Conf init : main")

        # RunTime_handlers
        self.minRate    = 0.5
        self.calcRate   = 0.7
        self.renderRate = 0.5
        self.th = threadingHandler(self.calcRate, self.renderRate)

        ### ------------------ ###
        self.world = renderer(20,40, self.debugger)

        # Obj 0
        wall = obj(_screen_w=40, _screen_h=20, _h = 5, _w = 8, _x=0)
        self.world.add_obj(wall)
        # Obj 1
        wall_2 = obj(_screen_w=40, _screen_h=20, _h = 10, _w = 8, _x=10, _char='0')
        self.world.add_obj(wall_2)

        # Push to th_render stack
        self.th.insert_thMain(self.th_main_content)
        self.th.insert_thRender(self.th_render_content)

        while True:
            self.th.runTh_all()
            time.sleep(self.minRate)

    def th_render_content(self):
        self.debugger.log("render thread cycle <<>>")
        self.world.render()

    def th_main_content(self):
        self.debugger.log("main thread cycle <<>>")

main()
