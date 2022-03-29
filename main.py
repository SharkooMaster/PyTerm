
from transform.objects.obj import obj
from world.renderer import renderer
from conf import conf

class main:

    def __init__(self):
        self.debugger = conf().get_debugger()
        self.debugger.log("Conf init : main")

        world = renderer(20,40, self.debugger)

        wall = obj(_screen_w=40, _screen_h=20, _h = 5, _w = 8, _x=0)
        world.add_obj(wall)
        wall_2 = obj(_screen_w=40, _screen_h=20, _h = 10, _w = 8, _x=10, _char='0')
        world.add_obj(wall_2)
    
        world.render()

main()
