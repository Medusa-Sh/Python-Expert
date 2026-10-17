import cv2
import numpy as np

def apply_filter(image,ftype):
    """apply filter to the image based on the filter type"""
    img=image.copy()
    if ftype=='red tint':
        img[:,:,1]=img[:,:,0]=0
    elif ftype=='green tint':
        img[:,:,0]=img[:,:,2]=0
    elif ftype=='blue tint':
        img[:,:,1]=img[:,:,2]=0
    elif ftype=='sobel':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sob = cv2.bitwise_or(sx.astype('uint8'), sy.astype('uint8'))
        img = cv2.cvtColor(sob, cv2.COLOR_GRAY2BGR)
    elif ftype=='canny':
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        can=cv2.Canny(gray,100,200)
        img=cv2.cvtColor(can,cv2.COLOR_GRAY2BGR)
    elif ftype=="cartoon":
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        gray=cv2.medianBlur(gray,5)
        edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
        color=cv2.bilateralFilter(image,9,300,300)
        img=cv2.bitwise_and(color,color,mask=edges)
    return img

def main():
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    ftype="original"
    print("keys: r=red g=green b=blue c=canny s=sobey o=original t=cartoon q=quit")
    while True:
        ret,frame=cap.read()
        if not ret:
            print("Cant't recieve frame")
            break
        out=apply_filter(frame,ftype)
        cv2.imshow("filter",out)
        key=cv2.waitKey(1) & 0xFF
        if key==ord('q'):
            exit()
        elif key==ord('r'):
            ftype="red tint"
        elif key==ord('g'):
            ftype="green tint"
        elif key==ord('b'):
            ftype="blue tint"
        elif key==ord('c'):
            ftype="canny"
        elif key==ord('s'):
            ftype="sobel"
        elif key==ord('o'):
            ftype="original"
        elif key==ord('t'):
            ftype="cartoon"
    cap.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()