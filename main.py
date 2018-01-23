from tkinter import *
import tkinter.messagebox
import cv2
from imgcap import imgcap
from playfunc import playfunc
import joblib
class MainWindow:

    def __init__(self,master):

        self.master=master
        self.master.title('IER System')
        self.master.geometry('1250x650+70+30')
        self.master.configure(background='#404344')

    def welcome(self):
        self.topframe = Frame(self.master, bg='#404344')
        self.topframe.pack(fill =X)
        self.label1 = Label(self.topframe, text='Welcome To ', fg='white', bg='#404344', font=('Cooper Black', 30))
        self.label2 = Label(self.topframe, text='Interactive Emotion Recognition ', fg='white', bg='#404344', font=('Cooper Black', 30))
        self.label3 = Label(self.topframe, text='System ', fg='white', bg='#404344', font=('Cooper Black', 30))
        self.label1.pack(pady=10)
        self.label2.pack(pady=10)
        self.label3.pack(pady=10)

        self.bottomframe= Frame(self.master, bg='#404344')
        self.bottomframe.pack(side= BOTTOM)


        self.photo= PhotoImage(file=r"test.png")
        self.label4 = Label(self.bottomframe, image = self.photo, border = 0)
        self.label4.pack(side= LEFT, padx=150, pady = 60)

        self.label5 = Label(self.bottomframe, text = r"Hey bud! how's your mood today?", fg='#FFF', bg='#404344', font =('Cooper Black', 20))
        self.label5.pack(side = TOP, padx=50, pady= 60)

        self.button1 = Button(self.bottomframe, text='Lets test it!', fg= '#FFF', bg='#404344', font = ('Cooper Black',20))
        self.button1.bind("<Button-1>", self.delete)
        self.button1.pack()


    def delete(self,event):
        self.topframe.destroy()
        self.bottomframe.destroy()
        start(self.master)


class WorkWindow:

    def __init__(self,master):
        self.answer = tkinter.messagebox.askquestion('Warning!','This App wants to use your webcam, Continue?')
        if self.answer == 'yes':
            #**** Open the new working window*****
            self.master = master

            # ****** Status*******
            self.status = Label(self.master, text='This is the status bar...', border=1, relief=SUNKEN, anchor=W)
            self.status.pack(side=BOTTOM, fill=X)
            #self.input()

        else:
            root.destroy()

    def option_text(self):
        self.textlabel= Label(self.rightframe, text= playfunc(), bg= '#00C997', fg= 'blue', font=('Algerian', 26, 'bold'))
        self.textlabel.pack(side= BOTTOM,pady = 30)


    def option_audio(self):
        self.textlabel.pack_forget()
        print('audio!')

    def option_video(self):
        self.textlabel.pack_forget()
        print('video!')

    def input(self):

        self.master.configure(background='#00C997')
        self.leftframe = Frame(self.master, bg='#00C997')
        self.leftframe.pack(fill=Y, side = LEFT)
        self.scan_photo = PhotoImage(file=r"scan.png")
        self.photolabel = Label(self.leftframe, image=self.scan_photo, border= 5, relief = GROOVE)
        self.photolabel.image = self.scan_photo
        self.photolabel.pack(pady = 70, side= TOP, padx= 50)
        self.click = Button(self.leftframe, text= 'Take snap!', bg= '#FFB3B3', fg= '#0A1829', font= ('Algerian', 26, 'bold'))
        self.click.bind("<Button-1>", self.screenshot)
        self.click.pack(pady = 30)

        #*****Middleframe********

        self.middleframe = Frame(self.master, bg='#00C997')
        self.middleframe.pack(fill= Y, side= LEFT, padx= 80, pady=50)

        #**** Radio Buttons*******
        option = IntVar()
        radio1 = Radiobutton(self.middleframe, variable=option, value=1, text='Text', command=self.option_text, fg='brown',bg='#00C997', font= ('Algerian', 20, 'bold'))
        radio1.pack(pady=30)
        radio2 = Radiobutton(self.middleframe, variable=option, value=2, text='Audio', command=self.option_audio,fg='brown',bg='#00C997', font= ('Algerian', 20, 'bold'))
        radio2.pack(pady=30)
        radio3 = Radiobutton(self.middleframe, variable=option, value=3, text='Video', command=self.option_video,fg='brown',bg='#00C997', font= ('Algerian', 20, 'bold'))
        radio3.pack(pady=30)

        #******* Right Frame*******

        self.rightframe = Frame(self.master, bg='#00C997')
        self.rightframe.pack(fill= Y, side= LEFT, padx= 80, pady=50)


    def screenshot(self):
        img,data=imgcap()
        try:
            if data==-1:
                print("Try Again!!")
        except:
            # playfunc(predict(data),'audio')
            clf = joblib.load('KNDclf_fn.pkl')
            ans=clf.predict(X);
            playfunc(ans,randint())
            cv2.imshow('IMAGE',img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()



def start(master):
    detect = WorkWindow(master)
    detect.input();





root = Tk()
main= MainWindow(root)
main.welcome()
root.mainloop()
