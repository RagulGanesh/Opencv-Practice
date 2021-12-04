import cv2 as cv

def rescale(frame,scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img=cv.imread('Photos/dogLarge.jpg')

cv.imshow('Dog',img)
cv.imshow('Dog_resized',rescale(img,scale=0.2))

cv.waitKey(0)