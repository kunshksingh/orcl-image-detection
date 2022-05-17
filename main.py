#import cv2
#import numpy as np
import sys 
sys.path.append('/usr/local/lib/python3.9/site-packages')

class main:
    def timeSpent(self):
        elements = {}
        prevTime = 0

        #For each frame TODO
        while True:
            currTime = 0 #TODO Determine current timestamp
            object = "Test" #TODO Image detection
            elements[object] += currTime-prevTime
            prevTime = currTime
        return elements

    def __init__(self):
        elements = self.timeSpent()
        #TODO Run all commands
        for pair in elements.items():
            print(pair.keys + " was looked at for " + pair.values + " seconds") 