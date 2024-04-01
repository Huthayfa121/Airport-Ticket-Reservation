from tkinter import *  # to create GUI we will import tkinter
from tkcalendar import *
from tkinter import messagebox  # to import message

import mysql.connector

from PIL import ImageTk  # to import jpg image in our code

import os

from tkinter import ttk

import sys

# Retrieve the admin ID passed as a command-line argument
admin_id = sys.argv[1] if len(sys.argv) > 1 else None
def addFlight():
    global admin_id
    if (flName.get() == '' or srcChoosen.get() == '' or depChoosen.get() == '' or date.get() == ''
            or depTime.get() == '' or arrivTime.get() == '' or charge.get() == ''):
        messagebox.showerror('Error', 'Fields cannot be empty')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "INSERT INTO flight (fName, source, departure, date, depTime, arrTime, flightCharge, admin_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (flName.get(), srcChoosen.get(), depChoosen.get(), date.get(), depTime.get(),
                   arrivTime.get(), charge.get(), admin_id)
            cur.execute(query, val)
            db.commit()
            messagebox.showinfo('Success', 'Record inserted successfully')

            Exitt()

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error: {e}')

        finally:
            if db.is_connected():
                cur.close()
                db.close()

def Exitt():
    root.destroy()  # Close the main login window
    os.system('python adminMain.py')


def pick_date(event):
    global cal, date_window
    date_window = Toplevel()
    date_window.grab_set()
    date_window.title('Choose date of birth')
    date_window.geometry('250x230+650+150')
    date_window.resizable(False, False)
    cal = Calendar(date_window, selectmode='day', date_pattern='yyyy-mm-dd')
    cal.place(x=0, y=0)
    submit = Button(date_window, text='Submit', font=("times new roman", 12, 'bold'), command=grab_date, bg='red',
                    fg='white',
                    activebackground='white', activeforeground='black', cursor='hand2', bd=2)
    submit.place(x=100, y=190)


def grab_date():
    date.delete(0, END)
    date.insert(0, cal.get_date())
    date_window.destroy()


def autoId():
    try:
        db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
        cur = db.cursor()

        # Reset the auto-increment value to the next available ID
        cur.execute("ALTER TABLE flight AUTO_INCREMENT = 1")
        db.commit()

        # Get the maximum ID value after deletion
        cur.execute("SELECT MAX(flight_id) FROM flight")
        max_id = cur.fetchone()[0]

        # If there are no existing IDs, start from a predefined value
        if max_id is None:
            flight_id = 20001
        else:
            # Increment the maximum ID by 1 to get the next available ID
            flight_id = max_id + 1

        return flight_id

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if db.is_connected():
            cur.close()
            db.close()


root = Tk()
root.title("Add Flight")
root.geometry("1350x760+0+0")
root.configure(bg="sky blue2")
backgroundImage = ImageTk.PhotoImage(file='img/plan1.jpeg')  # ImageTk.PhotoImage allows as to use image from type jpg

bgLabel = Label(root, image=backgroundImage)

bgLabel.place(x=0, y=0)

# ***************************************************************************************************************************
head_frame = Frame(root)
head_frame.configure(bg="sky blue2")
head_frame.place(x=150, y=90, width=590, height=550)

label1 = Label(head_frame, text="Flight ID ", font=('times new roman', 15), bg='sky blue2')
label1.grid(row=1, column=0, pady=15, padx=4)

label2 = Label(head_frame, text=autoId(), font=('times new roman', 16, 'bold'), bg='sky blue2', fg='red', width=35)
label2.grid(row=1, column=1, pady=15, padx=4)
# ***************************************************************************************************************************

label3 = Label(head_frame, text="Flight Name ", font=('times new roman', 15), bg='sky blue2')
label3.grid(row=2, column=0, pady=15, padx=4)

flName = Entry(head_frame, font=('times new roman', 12), bg="white", width=35, bd=3)
flName.grid(row=2, column=1, pady=15, padx=4)
# ***************************************************************************************************************************

label6 = Label(head_frame, text="Source ", font=('times new roman', 15), bg='sky blue2')
label6.grid(row=3, column=0, pady=15, padx=4)

n = StringVar()
srcChoosen = ttk.Combobox(head_frame, width=44, textvariable=n)

country_names = [
    'USA', 'UK', 'France', 'Germany', 'Japan', 'Australia', 'Canada',
    'Saudi Arabia', 'United Arab Emirates', 'Egypt', 'Jordan', 'Iraq', 'Kuwait', 'Qatar', 'Oman', 'Bahrain']
# Adding combobox drop down list
srcChoosen['values'] = country_names

srcChoosen.grid(row=3, column=1, pady=15, padx=4)

# ***************************************************************************************************************************

label7 = Label(head_frame, text="Departure ", font=('times new roman', 15), bg='sky blue2')
label7.grid(row=4, column=0, pady=15, padx=4)

n1 = StringVar()
depChoosen = ttk.Combobox(head_frame, width=44, textvariable=n1)

# Adding combobox drop down list
depChoosen['values'] = country_names

depChoosen.grid(row=4, column=1, pady=15, padx=4)


# **************************** Second Column ***********************************************************************

label8 = Label(head_frame, text="Date ", font=('times new roman', 15), bg='sky blue2')
label8.grid(row=5, column=0, pady=15, padx=4)

date = Entry(head_frame, font=('times new roman', 12), bg="white", width=35, bd=3)
date.grid(row=5, column=1, pady=15, padx=4)
date.bind('<1>', pick_date)
# ***************************************************************************************************************************

label10 = Label(head_frame, text="Departure Time ", font=('times new roman', 15), bg='sky blue2')
label10.grid(row=6, column=0, pady=15, padx=4)

depTime = Entry(head_frame, font=('times new roman', 12), bg="white", bd=3, width=35)
depTime.grid(row=6, column=1, pady=15, padx=4)

# ***************************************************************************************************************************

label12 = Label(head_frame, text="Arrival Time ", font=('times new roman', 15), bg='sky blue2')
label12.grid(row=7, column=0, pady=15, padx=4)

arrivTime = Entry(head_frame, font=('times new roman', 12), bg="white", bd=3, width=35)
arrivTime.grid(row=7, column=1, pady=15, padx=4)
# ***************************************************************************************************************************

label14 = Label(head_frame, text="Flight Charge $ : ", font=('times new roman', 15), bg='sky blue2')
label14.grid(row=8, column=0, pady=15, padx=4)

charge = Entry(head_frame, font=('times new roman', 12), bg="white", bd=3, width=35)
charge.grid(row=8, column=1, pady=15, padx=4)

# **********************************Button ***********************************************
addButton = Button(text='Add', font=('times new roman', 15, 'bold'), bg='red', fg='white',
                   activebackground='white', activeforeground='black', cursor='hand2', width=7, bd=3, command=addFlight)
addButton.place(x=510, y=580)

CancelButton = Button(text='Cancel', font=('times new roman', 15, 'bold'), bg='gray87', fg='black',
                  activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=3,
                  command=Exitt)
CancelButton.place(x=630, y=580)



root.mainloop()
