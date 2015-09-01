import cv2
import numpy as np

img = cv2.imread("/home/vasista/Desktop/assignment1/simple/1.jpg")
image = cv2.resize(img, (480,640)) 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(thresh, im_bw) = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(im_bw,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('C_I',image)
#print len(contours)
area1 = []
for contour in contours:
	[x,y,w,h] = cv2.boundingRect(contour)
	if h<40 or w<40:
        	continue
	if h>40 or w>40:
		area = cv2.contourArea(contour)
		area1.append(area)
		#avg = sum(area1)/len(area1)
		k = max(area1)
		if k==area: #assuming form area will be the large
			cv2.rectangle(im_bw,(x,y),(x+w,y+h),(255,0,255),2)
			crop_img = image[y: y+h, x: x+w]

cv2.imshow('G_I',gray_image)
cv2.imshow('B_I',im_bw)
cv2.imshow('C_O',image)
cv2.imshow("cropped",crop_img)
#cv2.imwrite('form.png',image)
cv2.imwrite('/home/vasista/Desktop/Assignment/test/outputtest.jpg',crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
