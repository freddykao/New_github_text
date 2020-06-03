import cv2 
import numpy as np 
image = cv2.imread( "lena.png" , cv2.IMREAD_COLOR)
cvt  = cv2.cvtColor( image ,cv2.COLOR_BGR2HLS)
img_lab = cv2.cvtColor(cvt, cv2.COLOR_BGR2LAB)

while True:
    cv2.imshow("cvt " , cvt)
    cv2.imshow("Image",image)
    cv2.imshow("img_lab",img_lab)

    (B,G,R)=cv2.split(image)
    cv2.imshow('R',R)
    cv2.imshow('G',G)
    cv2.imshow('B',B)
    if cv2.waitKey(0) == 27 :
        cv2.destroyAllWindows()
        break
