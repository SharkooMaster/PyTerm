import threading

class lowObj_thread(threading.Thread):
    def __init__(self, _iD, _name, _tickRate):
        threading.Thread.__init__(self)
        self.iD         = _iD
        self.name       = _name
        self.tickRate   = _tickRate

        self.stack      = []

    def run(self):
        for task in self.stack:
            task()

    def insertToStack(self, toAppend):
        self.stack.append(toAppend)


class threadingHandler:

    def __init__(self, _calcRate, _renderRate):
        self.th_main     = lowObj_thread(1, "pyterm_main"   , _calcRate)
        self.th_render   = lowObj_thread(1, "pyterm_render" , _renderRate)

        self.th_main.start()
        self.th_render.start()

    def insert_thMain(self, toInsert):
        self.th_main.insertToStack(toInsert)

    def insert_thRender(self, toInsert):
        self.th_render.insertToStack(toInsert)

    def runTh_all(self):
        self.th_main.run()
        self.th_render.run()
