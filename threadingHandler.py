import threading

class lowObj_thread:
    def __init__(self, _iD, _name, _tickRate):
        threading.Thread.__init__(self)
        self.iD         = _iD
        self.name       = _name
        self.tickRate   = _tickRate
    
    def run(self, toRun):
        toRun()


class threadingHandler:

    def __init__(self, _calcRate, _renderRate):
        self.th_main     = lowObj_thread(1, "pyterm_main"   , _calcRate)
        self.th_render   = lowObj_thread(1, "pyterm_render" , _renderRate)

        self.th_main.start()
        self.th_render.start()