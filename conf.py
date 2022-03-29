
from debug.debugger import debugger

class conf:

    global interface_debugger

    def __init__(self):
        global interface_debugger
        interface_debugger = debugger("logs")

    ### get/set ###

    def get_debugger(self):
        global interface_debugger
        return interface_debugger
