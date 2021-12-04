import cv2 as cv
'''
#reading an image
#img stores matrix of pixels
img=cv.imread('cat.jpeg')
#to show an image
cv.imshow('Dog',img)'''
#capture=cv.VideoCapture(0, cv.CAP_DSHOW)
capture=cv.VideoCapture('Hosting your site.mp4')

while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

