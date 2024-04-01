from tkinter import *  # to create GUI we will import tkinter

from tkinter import messagebox  # to import message

import mysql.connector

from PIL import ImageTk  # to import jpg image in our code

import os

from tkinter import ttk


def Exitt():
    main.destroy()  # Close the main login window
    os.system('python adminMain.py')


def find():
    fNameEntry.delete(0, 'end')
    srcChoosen.delete(0, 'end')
    depChoosen.delete(0, 'end')
    dateEntry.delete(0, 'end')
    depTimeEntry.delete(0, 'end')
    arrTimeEntry.delete(0, 'end')
    chargeEntry.delete(0, 'end')

    if flightIdEntry.get() == '':
        messagebox.showerror('Error', 'Empty ID')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "SELECT * FROM flight WHERE flight_id = %s"
            val = (flightIdEntry.get(),)
            # cur.execute("SELECT * FROM admin WHERE admin_id = %s", (adminIdEntry.get(),))
            cur.execute(query, val)
            record = cur.fetchone()

            if record is None:
                messagebox.showinfo("Message", "Not Found ")
            else:
                fNameEntry.insert(0, record[1])
                srcChoosen.insert(0, record[2])
                depChoosen.insert(0, record[3])
                dateEntry.insert(0, record[4])
                depTimeEntry.insert(0, record[5])
                arrTimeEntry.insert(0, record[6])
                chargeEntry.insert(0, record[7])

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error: {e}')
        finally:
            if db.is_connected():
                cur.close()
                db.close()


def delete():
    if flightIdEntry.get() == '':
        messagebox.showerror('Error', 'Empty ID')
    else:
        confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
        if not confirmed:
            return
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "DELETE FROM flight WHERE flight_id = %s"
            val = (flightIdEntry.get(),)
            cur.execute(query, val)
            db.commit()
            messagebox.showinfo("Success", "Record deleted successfully!")

            flightIdEntry.delete(0, 'end')
            fNameEntry.delete(0, 'end')
            srcChoosen.delete(0, 'end')
            depChoosen.delete(0, 'end')
            dateEntry.delete(0, 'end')
            depTimeEntry.delete(0, 'end')
            arrTimeEntry.delete(0, 'end')
            chargeEntry.delete(0, 'end')

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error: {e}')
        finally:
            if db.is_connected():
                cur.close()
                db.close()


def update():
    if flightIdEntry.get() == '':
        messagebox.showerror('Error', 'Empty ID')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "UPDATE flight SET fName = %s, source = %s, departure = %s, date = %s, depTime = %s, arrTime = %s, flightCharge = %s WHERE flight_id = %s"
            val = (fNameEntry.get(), srcChoosen.get(), depChoosen.get(), dateEntry.get(),
                   depTimeEntry.get(), arrTimeEntry.get(), chargeEntry.get(), flightIdEntry.get())
            cur.execute(query, val)
            db.commit()  # Remember to commit the changes after an update operation
            messagebox.showinfo("Success", "Record Updated successfully!")

            flightIdEntry.delete(0, 'end')
            fNameEntry.delete(0, 'end')
            srcChoosen.delete(0, 'end')
            depChoosen.delete(0, 'end')
            dateEntry.delete(0, 'end')
            depTimeEntry.delete(0, 'end')
            arrTimeEntry.delete(0, 'end')
            chargeEntry.delete(0, 'end')

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error: {e}')
        finally:
            if db.is_connected():
                cur.close()
                db.close()


main = Tk()

main.title('Find Flight')

main.geometry('1350x760+0+0')

# main.resizable(False, False)
backgroundImage = ImageTk.PhotoImage(file='img/plan1.jpeg')  # ImageTk.PhotoImage allows as to use image from type jpg

bgLabel = Label(main, image=backgroundImage)

bgLabel.place(x=0, y=0)

loginFrame = Frame(main, bg='powder blue')

loginFrame.place(x=150, y=130, width=550, height=480)

# ************************************Flight ID*******************************************************
flightId = Label(main, text='Flight ID ', compound=LEFT, font=('times new roman', 17, 'bold'), bg='#8cc4d6')

flightId.place(x=170, y=60)

flightIdEntry = Entry(main, font=('times new roman', 15, 'bold'), bg='gray95', bd=3, fg='red',
                      width=30)

flightIdEntry.place(x=300, y=60)

findButton = Button(main, text='Find', font=('times new roman', 13, 'bold'), bg='gray87', fg='black',
                    activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=3, command=find)

findButton.place(x=625, y=60)

# ************************************Flight Name*******************************************************
fName = Label(loginFrame, text='Flight Name ', compound=LEFT, font=('times new roman', 15), bg='powder blue')

fName.grid(row=2, column=1, pady=15, padx=5)

fNameEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray95', bd=3, fg='midnight blue', width=30)

fNameEntry.grid(row=2, column=2, pady=15, padx=5)

# ************************************Source*******************************************************
source = Label(loginFrame, text='Source ', compound=LEFT, font=('times new roman', 15), bg='powder blue')

source.grid(row=3, column=1, pady=15, padx=5)


srcChoosen = ttk.Combobox(loginFrame, width=47)

country_names = [
    'USA', 'UK', 'France', 'Germany', 'Japan', 'Australia', 'Canada',
    'Saudi Arabia', 'United Arab Emirates', 'Egypt', 'Jordan', 'Iraq', 'Kuwait', 'Qatar', 'Oman', 'Bahrain']
# Adding combobox drop down list
srcChoosen['values'] = country_names

srcChoosen.grid(row=3, column=2, pady=15, padx=5)

# ************************************Departure*******************************************************
departure = Label(loginFrame, text='Departure ', compound=LEFT, font=('times new roman', 15), bg='powder blue')

departure.grid(row=4, column=1, pady=15, padx=5)

depChoosen = ttk.Combobox(loginFrame, width=47)

# Adding combobox drop down list
depChoosen['values'] = country_names

depChoosen.grid(row=4, column=2, pady=15, padx=5)

# ************************************date*******************************************************
date = Label(loginFrame, text='Date ', compound=LEFT, font=('times new roman', 15), bg='powder blue')

date.grid(row=5, column=1, pady=15, padx=5)

dateEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray95', bd=3, fg='midnight blue', width=30)

dateEntry.grid(row=5, column=2, pady=15, padx=5)

# ************************************date*******************************************************
depTime = Label(loginFrame, text='Departure Time ', compound=LEFT, font=('times new roman', 15), bg='powder blue')

depTime.grid(row=6, column=1, pady=15, padx=5)

depTimeEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray95', bd=3, fg='midnight blue', width=30)

depTimeEntry.grid(row=6, column=2, pady=15, padx=5)

# ************************************date*******************************************************
arrTime = Label(loginFrame, text='Arrival Time ', compound=LEFT, font=('times new roman', 15), bg='powder blue')

arrTime.grid(row=7, column=1, pady=15, padx=5)

arrTimeEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray95', bd=3, fg='midnight blue', width=30)

arrTimeEntry.grid(row=7, column=2, pady=15, padx=5)

# ************************************date*******************************************************
charge = Label(loginFrame, text='Flight Charge $ ', compound=LEFT, font=('times new roman', 15), bg='powder blue')

charge.grid(row=8, column=1, pady=15, padx=5)

chargeEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray95', bd=3, fg='midnight blue', width=30)

chargeEntry.grid(row=8, column=2, pady=15, padx=5)

# ************************************* buttons ***************************************************
updateButton = Button(loginFrame, text='Update', font=('times new roman', 15, 'bold'), bg='gray87', fg='black',
                      activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=3, command=update)
updateButton.place(x=170, y=430)

deleteButton = Button(loginFrame, text='Delete', font=('times new roman', 15, 'bold'), bg='red', fg='white',
                      activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=3, command=delete)

deleteButton.place(x=270, y=430)

BkButton = Button(loginFrame, text='Cancel', font=('times new roman', 15, 'bold'), bg='gray87', fg='black',
                  activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=3,
                  command=Exitt)

BkButton.place(x=370, y=430)

main.mainloop()