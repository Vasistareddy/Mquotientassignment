import cv2
import numpy as np

print " Press r to replicate the border with a random color "
print " Press c to replicate the border "
print " Press Esc to exit "

img = cv2.imread('rgray_10.jpg')


rows,cols = img.shape[:2]

dst = img.copy()

top = int (0.05*rows)
bottom = int (0.05*rows)

left = int (0.05*cols)
right = int (0.05*cols)
cv2.imshow('border',dst)
value = np.random.randint(0,255,(3,)).tolist()
dst1 = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_CONSTANT,value = value)
cv2.imshow('padd',dst1)
gray_image = cv2.cvtColor(dst1, cv2.COLOR_BGR2GRAY)
cv2.imwrite('test2_10.jpg',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


