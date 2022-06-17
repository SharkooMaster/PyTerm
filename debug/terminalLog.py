import os

path = "~/dev/PyTerm/logs/log_18_06_2022.txt"

lines = []

def log():
    global path
    file = open("./logs/log_18_06_2022.txt","r")
    for line in file:
        if(line not in lines):
            print(line)
            lines.append(line)

while(True):
    log()


