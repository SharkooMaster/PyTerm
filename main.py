
from transform.objects.obj import obj
from world.renderer import renderer

class main:

    def __init__(self):
        wall = obj(_screen_w=40, _screen_h=20, _h = 5, _w = 8, _x = 10)
        
        world = renderer(20,40)
        world.add_obj(wall)
        world.render()

main()