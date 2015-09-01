import cv2
import numpy as np
src = cv2.imread('test2_17.jpg')
img = cv2.imread("test4_17.jpg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, im_bw) = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(im_bw,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
area1 = []
for contour in contours:
	area = cv2.contourArea(contour)#area of each boundingbox
	area1.append(area)
k = (sorted(area1)[-2])#second maximum value
#k = max(area1)
for contour in contours:
	[x,y,w,h] = cv2.boundingRect(contour)
	area = cv2.contourArea(contour)
	cv2.rectangle(im_bw,(x,y),(x+w,y+h),(255,0,255),2)
	if k == area:
		cv2.rectangle(im_bw,(x,y),(x+w,y+h),(255,0,255),2)
		crop_img = img[y: y+h, x: x+w]
		crop_img = src[y: y+h, x: x+w]
	#print area
	#avg = sum(area1)/len(area1)


#cv2.imshow('G_I',gray_image)
cv2.imshow('gray',gray_image)
cv2.imshow('B_I',im_bw)
cv2.imshow('C_I',crop_img)
#cv2.imshow('C_O',image)
#cv2.imshow('cropped',crop_img)
#cv2.imwrite('form.png',image)
cv2.imwrite('output_pad_17.jpg',crop_img)
#cv2.imwrite('gray.png',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
