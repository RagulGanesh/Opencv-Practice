import cv2 as cv

# Read in an image
img = cv.imread('Photos/dog.jpeg')
cv.imshow('Dog', img)

#Converting to Gray Scale
#gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#To Blur an Image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#To display Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
#cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
#cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
#cv.imshow('Resized', resized)

# Cropping
cropped = img[50:80, 80:300]
#cv.imshow('Cropped', cropped)

cv.waitKey(0)