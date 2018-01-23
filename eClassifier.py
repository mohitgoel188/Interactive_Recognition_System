import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier
#from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
from sklearn.multiclass import OneVsRestClassifier
from datetime import datetime

def main():
    print("Loading Training data...")
    df=pd.read_csv('train.csv')
    #gen=pd.read_csv('train.csv',chunksize=1)
    #df=gen.get_chunk(12000)
    X_train=np.array(df.drop(['emotion'],1))
    y_train=np.array(df['emotion'])

    #print("Feature Scaling...")
    #X_train=preprocessing.scale(X_train)                  

    d1=datetime.now()
    print("Preparing classifier...")
    print("Using KNeighborsClassifier without Feature Normalization.")
    #clf=OneVsRestClassifier(svm.SVC(),n_jobs=-1)
    clf=KNeighborsClassifier(n_neighbors=1000,weights='distance',algorithm='ball_tree',n_jobs=-1)
    #clf=MLPClassifier()
    print("Training classifier...")
    clf.fit(X_train,y_train)
    d2=datetime.now()

    print("Saving classifier...")
    #save the classifier
    joblib.dump(clf, 'KND1000clf_fn.pkl')    

    #load it again
    #print("Loading classifier...")
    #clf = joblib.load('knclf.pkl')

    print("Loading Testing data...")
    df2=pd.read_csv('cross_validation.csv')
    X_test=np.array(df2.drop(['emotion'],1))
    y_test=np.array(df2['emotion'])

    print("Measuring accuracy...")
    accuracy=clf.score(X_test,y_test)
    print(f"Accuracy: {accuracy}")
    print(f"Training Time: {d2-d1}")

if __name__ == '__main__':
    main()

