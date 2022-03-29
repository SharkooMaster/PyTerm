
import time
from datetime import date

class debugger:

    global path
    global current_date
    global logFile

    def __init__(self, _path):
        global path
        global logFile
        global current_date
        current_date = date.today().strftime("%d_%m_%Y")

        path = f"{_path}/log_{current_date}.txt"

        logFile = open(path, "w")
        logFile.write("### init ###\n")
        logFile.flush()
        logFile.close()

    def writeToLogFile(self):
        global path
        global logFile
        logFile = open(path, "a")

    def closeLogFile(self):
        global logFile
        logFile.flush()
        logFile.close()

    def log(self, toLog):
        global logFile

        self.writeToLogFile()
        logFile.write(f" --- > {toLog}\n")
        self.closeLogFile()
