import cv2 
import numpy as np 
image = cv2.imread( "lena.png" , cv2.IMREAD_COLOR)
gray = cv2.imread( "lena.png" ,cv2.IMREAD_GRAYSCALE)
while True:
    cv2.imshow("gray " , gray)
    cv2.imshow("Image",image)
    if cv2.waitKey(0) == 27 :
        cv2.destroyAllWindows()
        break
