import cv2
import numpy as np
import matplotlib.pyplot as plt

import sys 
import os

from PIL import Image, ImageDraw
import scipy.misc

sys.path.append('/usr/local/lib/python3.9/site-packages') #For issues with package dependencies locally

#TODO Loop through all images in directory 
#timer = cv2.getTickCount
filename = "resources/test/test/Ped/VR_Video/Gaze_mapping/2.video_frames_w_gaze/2022-04-01 13-29-23/1500b.jpg"
img = cv2.imread(filename, cv2.IMREAD_COLOR)
imageRect = img
altered = None

def main():
    point = detectGazeLoc()
    enhancement(point)

def detectGazeLoc():
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0 #TODO Determine the location of the gaze points

    #Harcode, delete when implementing
    x1 = 1030
    x2 = 1000
    y1 = 650
    y2 = 710

    x = int((x1+x2)/2) 
    y = int((y1+y2)/2) 

    return (x,y) #Return average location
def enhancement(point):
    x = point[0]
    y = point[1]
    
    #Crop Reigon
    copiedImg = img.copy()
    copiedImg = copiedImg[y-250:y+250,x-250:x+250]

    #Enhance
   
    cv2.imwrite(filename, copiedImg)

def annotate():
    xInterest = []
    yInterest = []

    
    minX = min(xInterest)
    minY = min(yInterest)
    maxX = max(xInterest)
    maxY = max(yInterest)
    altered = cv2.rectangle(img, (minX,minY), (maxX,maxY), (255,255,0), thickness=2, lineType=cv2.LINE_AA)

def resolveImage():
    location = detectGazeLoc()
    x = location[0]
    y = location[1]
    imageName = ""
    
    return imageName

main() 

#img = cv2.imwrite(filename, altered)