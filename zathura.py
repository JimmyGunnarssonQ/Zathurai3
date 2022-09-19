#!/usr/bin/enc python3
import sys 
import os 

input = sys.argv
item = input[1]
output = ""


for i in item:
    if i in ["(", ")", " ", "[", "]", "{", "}"]:
        i=r"\ ".replace(" ", "") + i
    output+=i

os.system("setsid -f zathura " + output + "&& kill -9 %d"%(os.getppid()))
