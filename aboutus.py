from tkinter import *


class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("About us")
        self.resizable(False, False)

        self.top = Frame(self, height=150)
        self.top.pack()

        self.text=Label(self.top,text="Hay, this is about us................")
        self.text.pack(x=40,y=50)