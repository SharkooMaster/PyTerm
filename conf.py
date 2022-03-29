
from debug.debugger import debugger

class conf:

    def __init__(self):
        self.interface_debugger = debugger("logs")

    ### get/set ###

    def get_debugger(self):
        return self.interface_debugger