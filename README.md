# PyTerm
A python terminal based game engine.

Required to run:
  - Create a [logs] folder in the main directory where the conf.py file exists.

Note:
  The main file is only for my sake, its technically just a template for others to kind of understand how the code runs in basic form until im done with the library and have a documentation page set up

#TEMPLATE:

            PreProcess
"self.debugger = conf().get_debugger()
self.debugger.log("Conf init : main")"

          RunTime_handlers
"self.minRate    = 0.5
self.calcRate   = 0.7
self.renderRate = 0.5
self.th = threadingHandler(self.calcRate, self.renderRate)"
// These are needed to run the engine. You may of course adjust the parameters, thats why i have them open and not automated. More control
