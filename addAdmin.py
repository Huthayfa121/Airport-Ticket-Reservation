from tkinter import *  # to create GUI we will import tkinter

from tkinter import messagebox  # to import message

import mysql.connector

from PIL import ImageTk  # to import jpg image in our code

import os


def autoId():
    try:
        db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
        cur = db.cursor()

        cur.execute("ALTER TABLE customer AUTO_INCREMENT = 1")
        db.commit()

        cur.execute("SELECT MAX(admin_id) FROM admin")
        rs = cur.fetchone()[0]
        if rs is None:
            adminId = 1001
            return adminId
        else:
            id_num = rs + 1
            adminId = id_num
            return adminId

    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if db.is_connected():
            cur.close()
            db.close()


def Exitt():
    main.destroy()  # Close the main login window
    os.system('python adminMain.py')


def add():
    if fNameEntry.get() == '' or lNameEntry.get() == '' or unameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            sql = "INSERT INTO admin (fName, lName, username, password) VALUES (%s, %s, %s, %s)"
            val = (fNameEntry.get(), lNameEntry.get(), unameEntry.get(), passwordEntry.get())
            cur.execute(sql, val)
            db.commit()
            messagebox.showinfo('Success', 'Record inserted successfully')
            adminIdEntry.configure(text=autoId())
            fNameEntry.delete(0, 'end')
            lNameEntry.delete(0, 'end')
            unameEntry.delete(0, 'end')
            passwordEntry.delete(0, 'end')
        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error: {e}')
        finally:
            if db.is_connected():
                cur.close()
                db.close()


main = Tk()

main.title('Add Admin')

main.geometry('1350x760+0+0')

# main.resizable(False, False)
backgroundImage = ImageTk.PhotoImage(file='img/plan1.jpeg')  # ImageTk.PhotoImage allows as to use image from type jpg

bgLabel = Label(main, image=backgroundImage)

bgLabel.place(x=0, y=0)

loginFrame = Frame(main, bg='powder blue')

loginFrame.place(x=150, y=120, width=500, height=380)

label = Label(loginFrame, text='Admin Creation ', font=('times new roman', 25, 'bold'), bg='powder blue')

label.grid(row=0, column=1, columnspan=3, pady=10)

# ************************************Admin ID*******************************************************
adminId = Label(loginFrame, text='Admin ID ', compound=LEFT, font=('times new roman', 15, 'bold'), bg='powder blue')

adminId.grid(row=1, column=1, pady=10, padx=5)

adminIdEntry = Label(loginFrame, text=autoId(), font=('times new roman', 15, 'bold'), bg='powder blue', bd=3, fg='red',
                     width=30)

adminIdEntry.grid(row=1, column=2, pady=10, padx=5)

# ************************************First Name*******************************************************
fName = Label(loginFrame, text='First Name ', compound=LEFT, font=('times new roman', 15), bg='powder blue')

fName.grid(row=2, column=1, pady=10, padx=5)

fNameEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray85', bd=3, fg='midnight blue', width=30)

fNameEntry.grid(row=2, column=2, pady=10, padx=5)

# ************************************Last Name*******************************************************
lName = Label(loginFrame, text='Last Name ', compound=LEFT, font=('times new roman', 15), bg='powder blue')

lName.grid(row=3, column=1, pady=10, padx=5)

lNameEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray85', bd=3, fg='midnight blue', width=30)

lNameEntry.grid(row=3, column=2, pady=10, padx=5)

# ************************************Username*******************************************************
uname = Label(loginFrame, text='Username ', compound=LEFT, font=('times new roman', 15), bg='powder blue')

uname.grid(row=4, column=1, pady=10, padx=5)

unameEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray85', bd=3, fg='midnight blue', width=30)

unameEntry.grid(row=4, column=2, pady=10, padx=5)

# ************************************password*******************************************************
password = Label(loginFrame, text='Password ', compound=LEFT, font=('times new roman', 15), bg='powder blue')

password.grid(row=5, column=1, pady=10, padx=5)

passwordEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray85', bd=3, fg='midnight blue', width=30)

passwordEntry.grid(row=5, column=2, pady=10, padx=5)

# ************************************* Add button ***************************************************
addButton = Button(loginFrame, text='Add', font=('times new roman', 15, 'bold'), bg='red', fg='white',
                   activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=3, command=add)
addButton.place(x=280, y=320)

# ************************************* Cancel button ***************************************************
BkButton = Button(loginFrame, text='Cancel', font=('times new roman', 15, 'bold'), bg='gray87', fg='black',
                  activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=3,
                  command=Exitt)

BkButton.place(x=380, y=320)

main.mainloop()
