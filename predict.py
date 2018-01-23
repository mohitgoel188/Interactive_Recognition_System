import pandas as pd
import numpy as np
import joblib
from playfunc import playfunc
from imgcap import imgcap
import cv2
import random
def predict(X,clf='KNDclf_fn.pkl'):   
    '''Function to load classifier clf(default: KNeighbors Classifier) 
                and predict result(0-6) from passed data X''' 
    #load classifier
    clf = joblib.load(clf)
    return clf.predict(X);

def main():
    img,data=imgcap()
    content=random.randint(0,1)
    try:
        if data==-1:
            print("Try Again!!")
    except:
        # playfunc(predict(data),'audio')
        dic=['Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']
        ans=predict(data)
        print(ans)
        print(dic[ans[0]])
        playfunc(ans,content)
        cv2.imshow('IMAGE',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()