from tkinter import *
import sqlite3
from tkinter import messagebox
con = sqlite3.connect('database.db')
cur = con.cursor()

class Display(Toplevel):
    def __init__(self,person_id):
        Toplevel.__init__(self)
        self.geometry("650x650+600+200")
        self.title("Display person")
        self.resizable(False, False)
        print("person_id=",person_id)
        query= " select * from adressbook where person_id='{}'".format(person_id)
        result= cur.execute(query).fetchone()
        print(result)
        self.person_id=person_id
        person_name=result[1]
        person_surname = result[2]
        person_mail = result[3]
        person_phone = result[4]
        person_address = result[5]
        print("person name=",person_name)

        self.top = Frame(self, height=150, bg='#c12020')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg='#d0dc1d')
        self.bottom.pack(fill=X)
        # -------------Top frame design------------------------------
        self.top_image = PhotoImage(file="icons/Book-phones-icon.png")
        self.top_image_lable = Label(self.top, image=self.top_image)
        self.top_image_lable.place(x=300, y=10)
        self.heading = Label(self.top, text="Person details", bg='#c12020', font='arial 15 bold')
        self.heading.place(x=270, y=80)
        # --------------------------Add name--------------
        self.lable_neme = Label(self.bottom, text="First Name", font='arial 15 bold', bg='#c12020')
        self.lable_neme.place(x=49, y=40)
        self.entry_name = Entry(self.bottom, width=50, bd=7)
        self.entry_name.insert(0, person_name)
        self.entry_name.config(state='disabled')
        self.entry_name.place(x=180, y=40)
        # ----------------------sirname--------------------------------------
        self.lable_sirneme = Label(self.bottom, text="Last Name", font='arial 15 bold', bg='#c12020')
        self.lable_sirneme.place(x=49, y=80)
        self.entry_sirname = Entry(self.bottom, width=50, bd=7)
        self.entry_sirname.insert(0, person_surname)
        self.entry_sirname.config(state='disabled')
        self.entry_sirname.place(x=180, y=80)
        # ---------------------email------------------------------
        self.lable_mail = Label(self.bottom, text="Email Id    ", font='arial 15 bold', bg='#c12020')
        self.lable_mail.place(x=49, y=120)
        self.entry_mail = Entry(self.bottom, width=50, bd=7)
        self.entry_mail.insert(0, person_mail)
        self.entry_mail.config(state='disabled')
        self.entry_mail.place(x=180, y=120)
        # --------------------phone----------------------------------
        self.lable_phone = Label(self.bottom, text="Phone Number", font='arial 15 bold', bg='#c12020')
        self.lable_phone.place(x=33, y=160)
        self.entry_phone = Entry(self.bottom, width=50, bd=7)
        self.entry_phone.insert(0,person_phone)
        self.entry_phone.config(state='disabled')
        self.entry_phone.place(x=180, y=160)
        # ----------------Address-----------------------------------
        self.lable_address = Label(self.bottom, text="Address", font='arial 15 bold', bg='#c12020')
        self.lable_address.place(x=33, y=200)
        self.entry_address = Entry(self.bottom, width=50, bd=5)
        self.entry_address.insert(0,person_address)
        self.entry_address.config(state='disabled')
        self.entry_address.place(x=180, y=200)
