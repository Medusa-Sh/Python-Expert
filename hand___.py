import cv2
import numpy as np

cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error could not open the camera")
    exit()

while True:
    ret, frame=cap.read()
    if not ret:
        print("Error failed to capture a image")  
        break
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #define the range for skin color in hsv
    lower_skin=np.array([0,20,70],dtype=np.uint8)
    upper_skin=np.array([20,255,255],dtype=np.uint8)
    
    #Create mask to detect skin color
    mask=cv2.inRange(hsv,lower_skin,upper_skin)

    #apply the mask to the frame
    result=cv2.bitwise_and(frame,frame,mask=mask)

    #find all counters
    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        max_contour=max(contours,key=cv2.contourArea)
        if cv2.contourArea(max_contour)>500:
            x,y,w,h=cv2.boundingRect(max_contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            center_x=int(x+w/2)
            center_y=int(h+y/2)
            cv2.circle(frame,(center_x,center_y),5,(0,0,255),-1)

    cv2.imshow('Original Frame',frame)
    cv2.imshow('Filtered Frame',result)
    if cv2.waitKey(1)&0xff==ord('q'):
        break

cap.release
cv2.destroyAllWindows