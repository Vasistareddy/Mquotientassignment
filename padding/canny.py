import cv2
import numpy as np

img = cv2.imread('rgray_17.jpg',0)
high_thresh, thresh_im = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
lowThresh = 0.5*high_thresh
print high_thresh,lowThresh
print thresh_im
edges = cv2.Canny(img,high_thresh,lowThresh)
cv2.imwrite('canny17.jpg',edges)
cv2.imshow('org',img)
cv2.imshow('edg',edges)
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows
 
