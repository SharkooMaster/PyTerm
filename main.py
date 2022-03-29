
from transform.objects.obj import obj
from world.renderer import renderer
from conf import conf

class main:

    global debugger

    def __init__(self):
        global debugger
        wall = obj(_screen_w=40, _screen_h=20, _h = 10, _w = 10, _x=0)
        wall_2 = obj(_screen_w=40, _screen_h=20, _h = 10, _w = 8, _x=9, _char='0')

        debugger = conf().get_debugger()
        debugger.log("Conf init : main")
        
        world = renderer(20,40)
        world.add_obj(wall)
        world.add_obj(wall_2)
        world.render()

main()
