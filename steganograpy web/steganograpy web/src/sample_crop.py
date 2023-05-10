import numpy as np
import cv2
def segment(fn):
    image=cv2.imread(fn)
    orig_image=image.copy()

    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret, thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    _, contours, hierarchy=cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    f=0
    r=()
    print(orig_image.shape)
    for c in contours:
        # print(len(c))
        x, y, w, h = cv2.boundingRect(c)
        if x==0 and y==0 and w==orig_image.shape[1] and h==orig_image.shape[0]:
            continue
        if f <len(c):
            f=len(c)
            r=x,y,w,h=cv2.boundingRect(c)
        # if len(c)>500:
        #     x,y,w,h=cv2.boundingRect(c)
        #     cv2.rectangle(orig_image,(x,y),(x+w,y+h),(0,0,255),2)
        #     cv2.imshow('Bounding rect',orig_image)
        #     cv2.waitKey(0)
        #     accuracy=0.03*cv2.arcLength(c,True)
        #     approx=cv2.approxPolyDP(c,accuracy,True)
        #     cv2.drawContours(image,[approx],0,(0,255,0),2)
        #     cv2.imshow('Approx polyDP', image)
        #     cv2.waitKey(0)
        #     cv2.destroyAllWindows()
    print(f)
    print(r)
    x,y,w,h=r
    return r
from stegano import lsb

r=segment("sample3.png")
img=cv2.imread("sample3.png")
x, y, w, h = r
crop_img = img[y:y + h, x:x + w]
cv2.imwrite("csample1.png",crop_img)



clear_message = lsb.reveal("csample1.png")
print(clear_message,"=====================")