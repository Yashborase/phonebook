from tkinter import *
import sqlite3
from addpeople import AdddPeople
from updatepeople import Update
from display import Display
from tkinter import messagebox
con= sqlite3.connect('database.db')
cur= con.cursor()

class Mypeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+600+200")
        self.title("My people")
        self.resizable(False,False)

        self.top = Frame(self, height=150, bg='#c12020')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg='#d0dc1d')
        self.bottom.pack(fill=X)
        # -------------Top frame design------------------------------
        self.top_image = PhotoImage(file="icons/Book-phones-icon.png")
        self.top_image_lable = Label(self.top, image=self.top_image)
        self.top_image_lable.place(x=300, y=10)
        self.heading = Label(self.top, text="My Contacts", bg='#c12020', font='arial 15 bold')
        self.heading.place(x=270, y=80)
        #-----------------Scroll bar creation-----------------------------------
        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)
    #-----------------listbox created for seving details----------------------------
        self.listBox=Listbox(self.bottom,width=60,height=27)
        self.listBox.grid(row=0,column=0,padx=(60,0))
        self.scroll.config(command=self.listBox.yview())
        self.listBox.config(yscrollcommand=self.scroll.set)

        persons=cur.execute("select * from 'adressbook'").fetchall()
        print(persons)
        count=0
        for person in persons:
            self.listBox.insert(count,str(person[0])+"."+person[1] +" "+person[2])
            count+=1
        self.scroll.grid(row=0,column=1,sticky=N+S)
    #------------adding buttons-------------------
        addntn=Button(self.bottom,text="Add",width=12,font='areal 15 bold',command=self.add_people)
        addntn.grid(row=0,column=2,padx=10,sticky=N,pady=200)

        updatentn = Button(self.bottom, text="Update", width=12, font='areal 15 bold',command=self.updatefunction)
        updatentn.grid(row=0,column=2,sticky=S, pady=150)

        displayntn = Button(self.bottom, text="Display", width=12, font='areal 15 bold',command=self.display_person)
        displayntn.grid(row=0, column=2, sticky=S, pady=100)

        deletentn = Button(self.bottom, text="Delete", width=12, font='areal 15 bold',command=self.delete_person)
        deletentn.grid(row=0, column=2, sticky=S, pady=50)

    def delete_person(self):
        selected_item = self.listBox.curselection()
        print(selected_item)
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        print(person_id)

        query="delete from adressbook where person_id={}".format(person_id)
        answer=messagebox.askquestion("Warning","Are you sure.....")
        if answer=='yes':
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("success","Deleted")
                self.destroy()
            except Exception as e:
                messagebox.showinfo("Info",str(e))


    def add_people(self):
        add_page=AdddPeople()
        self.destroy()

    def updatefunction(self):
        selected_item=self.listBox.curselection()
        print(selected_item)
        person=self.listBox.get(selected_item)
        person_id=person.split(".")[0]
        print(person_id)

        updatepage=Update(person_id)

    def display_person(self):
        selected_item = self.listBox.curselection()
        print(selected_item)
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        print(person_id)

        displaypage = Display(person_id)

