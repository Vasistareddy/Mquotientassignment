import cv2
img = cv2.imread('1.jpg')
image = cv2.resize(img, (480,640)) 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('rgray_1.jpg',gray_image)
#cv2.imshow('color_image',image)
#cv2.imshow('gray_image',gray_image)
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows
 
#End of Code
