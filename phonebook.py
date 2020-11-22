from tkinter import *
import datetime
from mypeople import Mypeople
from addpeople import AdddPeople
from aboutus import About
date=datetime.datetime.now().date()
date=str(date)
class Application(object):
    def __init__(self , master):
        self.master=master
#--------------------------Frames---------------------------
        self.top=Frame(master,height=150,bg='#c12020')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=500, bg='#d0dc1d')
        self.bottom.pack(fill=X)
#-------------Top frame design------------------------------
        self.top_image=PhotoImage(file="icons/Book-phones-icon.png")
        self.top_image_lable=Label(self.top,image=self.top_image)
        self.top_image_lable.place(x=300,y=10)
        self.heading=Label(self.top,text="My PhoneBook",bg='#c12020',font='arial 15 bold')
        self.heading.place(x=270,y=80)
        self.date_lbl=Label(self.top,text="Date:"+date,font='arial 15 bold',fg='#c12020')
        self.date_lbl.place(x=450,y=10)
#---------------------ADD BUTTON1 FOR VIEW PEOPLE---------------
        self.addviewbtn=Button(self.bottom,text="My people",font='arial 15 bold',command=self.my_people)
        self.addviewbtn.place(x=250,y=70)
#---------------------ADD BUTTON2 FOR ADD PEOPLE---------------
        self.addpeoplebtn = Button(self.bottom, text="Add people", font='arial 15 bold',command=self.addpeoplefunction)
        self.addpeoplebtn.place(x=245, y=115)
#---------------------ADD BUTTON3 FOR ABOUT US---------------
        self.aboutbtn = Button(self.bottom, text="About us", font='arial 15 bold',width=9,command=self.about_us)
        self.aboutbtn.place(x=250, y=160)

    def about_us(self):
        aboutpage=About()
    def my_people(self):
        people=Mypeople()

    def addpeoplefunction(self):
        addpeoplewindow=AdddPeople()
def main():
    root=Tk()
    app=Application(root)
    root.title("PhoneBook")
    root.geometry("650x500+350+200")
    root.resizable(False,False)
    root.mainloop()

if __name__== '__main__':
    main()