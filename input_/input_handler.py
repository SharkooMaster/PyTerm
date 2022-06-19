
import threading

# Get input [objects].
# {"key": ".", "target": ".", "action": ""}
# action:
# [
#   // POSTION
#   SYNTAX: [0]:p (for position)
#   SYNTAX: [1]:x,y (for position axis)
#   SYNTAX: [2:]:p (value)
#   EXAMPLE:
#   px2
#   py23
# ]
# 
# On trigger >> action.

class input_handler:

    def __init__(self,_inputs = []):
        self.inputs = []
        self.input = ""

    def getInput(self,_x):
        self.input = unique(_x)

    def unique(self,_x):
        return list(set(_x.split()))
