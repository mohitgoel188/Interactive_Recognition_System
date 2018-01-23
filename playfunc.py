import os,sys,subprocess

def playfunc(emotion,content):
    if emotion[0]==0:
        if content==0:
            os.startfile("1.mp3")
        elif content==1:
            os.startfile("11.mkv")
        else:
            os.startfile("")

    elif emotion[0]==1:
        if content==0:
            os.startfile("2.mp3")
        elif content==1:
            os.startfile("12.mkv")
        else:
            os.startfile("")

    elif emotion[0]==2:
        if content==0:
            os.startfile("3.mp3")
        elif content==1:
            os.startfile("13.mkv")
        else:
            os.startfile("")

    elif emotion[0]==3:
        if content==0:
            os.startfile("4.mp3")
        elif content==1:
            os.startfile("14.mkv")
        else:
            os.startfile("")

    elif emotion[0]==4:
        if content==0:
            os.startfile("5.mp3")
        elif content==1:
            os.startfile("15.mkv")
        else:
            os.startfile("")

    elif emotion[0]==5:
        if content==0:
            os.startfile("7.mp3")
        elif content==1:
            os.startfile("16.mkv")
        else:
            os.startfile("")

    elif emotion[0]==6:
        if content==0:
            os.startfile("6.mp3")
        elif content==1:
            os.startfile("17.mkv")
        else:
            os.startfile("")
