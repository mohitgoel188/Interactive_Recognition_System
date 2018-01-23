import cv2
import numpy as np
def imgcap():
    """Function to capture image from web cam and return image as 1D numpy array(grayscale)""" 
    video=cv2.VideoCapture(0)
    check,img=video.read()
    video.release()
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img_g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(img_g,
        scaleFactor=1.1,
        minNeighbors=5)
    try:
        x,y,w,h=faces[0]
        img_g=cv2.resize(img_g[y:y+h,x:x+w],(48,48))
        imarr=np.array(img_g)
        imarr=imarr.flatten()
        return (img,imarr.reshape(1, -1))
        #cv2.imshow('Cropped',img_g)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
    except:
        #print("no face")
        return (-1,-1)
def main():
    img,data=imgcap()
    try:
        if data==-1:
            print("Try again!!!")
    except:
        print(data)

if __name__ == '__main__':
    main()