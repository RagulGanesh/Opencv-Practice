import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)

#img=cv.imread('Photos/cat.jpeg')
#cv.imshow('Cat',img)

#1.Paint the Image with a certail color
#blank[:]=0,0,255
#cv.imshow('Green',blank)
#To color a certain area--> blank[200:300, 400:500]=0,0,255

#2.To draw a Rectangle
#cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
#cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED)
#cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=-1)
#cv.imshow('Rectangle',blank)

#3.To draw a circle
#cv.circle(blank,(250,250),100,(0,0,255),thickness=3)
#cv.imshow('Circle',blank)

#4.To draw a line

#cv.line(blank,(0,0),(400,400),(0,0,250),thickness=3)
#cv.imshow('Line',blank)

#5.To write a text

cv.putText(blank,"Hello World!",(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255),thickness=2)
cv.imshow('Text',blank)


cv.waitKey(0)