from tkinter import *  # to create GUI we will import tkinter

from tkinter import messagebox  # to import message

import mysql.connector

from PIL import ImageTk  # to import jpg image in our code

import os

from tkinter import ttk


def Exitt():
    root.destroy()  # Close the main login window
    os.system('python customerMain.py')

def Search():


    if (srcChoosen.get() == '' or depChoosen.get() == ''):
        messagebox.showerror('Error', 'Empty Source Or Departure')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "SELECT * FROM flight WHERE departure = %s AND source = %s"
            val = (depChoosen.get(), srcChoosen.get())
            cur.execute(query, val)
            rows = cur.fetchall()

            for item in table.get_children():
                table.delete(item)
            # Iterate over fetched rows and insert them into the Treeview table
            for row in rows:
                table.insert("", "end", values=row)

        except mysql.connector.Error as err:
            print("Error:", err)

        finally:
            if db.is_connected():
                cur.close()
                cur.close()

def find():


                    if csId.get() == '':
                        messagebox.showerror('Error', 'Empty ID')
                    else:
                        try:
                            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
                            cur = db.cursor()
                            query = "SELECT fName,lName,passport FROM customer WHERE cs_id = %s"
                            val = (csId.get(),)
                            cur.execute(query, val)
                            record = cur.fetchone()

                            if record is None:
                                messagebox.showinfo("Message", "Not Found ")
                            else:
                                FirstN.config(text=record[0])
                                LastN.config(text=record[1])
                                PassNum.config(text=record[2])

                        except mysql.connector.Error as e:
                            messagebox.showerror('Error', f'Error: {e}')
                        finally:
                            if db.is_connected():
                                cur.close()
                                db.close()

def update_total_price(*args):
    # Assume 'current_base_price' holds the base price for one seat of the selected class
    # Check if the base price is a digit and get the number of seats
    if priceLab.cget("text").replace("$", "").isdigit():
        current_base_price = int(priceLab.cget("text").replace("$", ""))
        num_seats = int(seatsSpin.get())
        total_price = current_base_price * num_seats
        totalLab.config(text=f"${total_price}")
    else:
        totalLab.config(text="$0")
def book_ticket():
    # Collect data
    flight_number = FliNumLab.cget("text")
    customer_id = csId.get()
    flight_class = clasChoosen.get()
    price = priceLab.cget("text")
    seats = seatsSpin.get()  # Assuming seatsSpin is your Spinbox for the number of seats
    date = Date.cget("text")

    # Convert price to a number
    price = price.replace("$", "")  # Remove dollar sign if present
    if price.isdigit():
        price = int(price)
    else:
        price = 0  # Default to 0 if there's an issue
    if csId.get() == '':
        messagebox.showerror('Error', 'Empty ID')
    else:
     try:
        db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
        cur = db.cursor()

        # Prepare SQL query to insert a record into the database.
        query = ("INSERT INTO ticket ( flight_id, cs_id, class, price, seats, date) "
                 "VALUES ( %s, %s, %s, %s, %s, %s)")
        values = (flight_number, customer_id, flight_class, price, seats, date)

        cur.execute(query, values)
        db.commit()

        messagebox.showinfo("Success", "Ticket booked successfully!")
     except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to book ticket: {err}")
     finally:
        if db.is_connected():
            cur.close()
            db.close()
def book_and_update_price():
    # Update the total price first
    update_total_price()
    # Then, proceed to book the ticket
    book_ticket()
def on_flight_selected(event):
    for selected_item in table.selection():
        item = table.item(selected_item)
        flight_data = item['values']
        if flight_data:
            FliNumLab.config(text=flight_data[0])
            FliNameLab.config(text=flight_data[1])
            depTimeLab.config(text=flight_data[5])
            Date.config(text=flight_data[4])
            # Update other labels as needed

def update_price(event):
    # Sample prices for demonstration; you might retrieve these from the database or another source
    class_prices = {
        'Economy': 100,
        'Premium Economy': 150,
        'Business': 200,
        'First class': 300
    }
    selected_class = clasChoosen.get()  # Get the currently selected class from the Combobox
    price = class_prices.get(selected_class, 0)  # Get the price for the selected class, default to 0 if not found
    priceLab.config(text=f"${price}")
def autoId():
    try:
        db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
        cur = db.cursor()

        cur.execute("ALTER TABLE ticket AUTO_INCREMENT = 1")
        db.commit()

        cur.execute("SELECT MAX(tkNum) FROM ticket")
        rs = cur.fetchone()[0]
        if rs is None:
            tkNum = 1
            return tkNum
        else:
            num = rs + 1
            tkNum = num
            return tkNum

    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if db.is_connected():
            cur.close()
            db.close()


root = Tk()
root.title("Book Tickets")
root.geometry('1360x760+0+0')
root.configure(bg="sky blue")
# ************************************************************************************************
tkNum = Label(root, text="Ticket Num", font=("times new roman", 17, 'bold'), bg='sky blue', fg='black', anchor="w")
tkNum.place(x=90, y=20)

tkNumEntry = Label(root, text=autoId(), font=('times new roman', 22, 'bold'), bg='sky blue', fg='red', anchor=CENTER,
                   width=5)
tkNumEntry.place(x=90, y=50)
# ************************************************************************************************

head_frame = Frame(root, bg='#f0f0f0', bd=4, relief='ridge')
head_frame.place(x=250, y=20, width=430, height=270)

label1 = Label(head_frame, text="Select Country", font=('times new roman', 16, 'bold'), bg='#f0f0f0')
label1.place(x=110, y=30)

label2 = Label(head_frame, text="Source: ", font=('times new roman', 15), bg='#f0f0f0')
label2.place(x=10, y=100)

n = StringVar()
srcChoosen = ttk.Combobox(head_frame, width=27, textvariable=n)

country_names = [
    'USA', 'UK', 'France', 'Germany', 'Japan', 'Australia', 'Canada',
    'Saudi Arabia', 'United Arab Emirates', 'Egypt', 'Jordan', 'Iraq', 'Kuwait', 'Qatar', 'Oman', 'Bahrain']
# Adding combobox drop down list
srcChoosen['values'] = country_names

srcChoosen.place(x=110, y=100)
srcChoosen.current()

label3 = Label(head_frame, text="Departure: ", font=('times new roman', 15), bg='#f0f0f0')
label3.place(x=10, y=150)

n1 = StringVar()
depChoosen = ttk.Combobox(head_frame, width=27, textvariable=n1)

# Adding combobox drop down list
depChoosen['values'] = country_names

depChoosen.place(x=110, y=150)
depChoosen.current()

button = Button(head_frame, text="Search", font=('times new roman', 15, 'bold'), bg='#f7faf7', fg='black',
                activebackground='red', activeforeground='white', command=Search)
button.place(x=320, y=190)

# *************************************  SECOND FRAME  *******************************************
head_frame1 = Frame(root, bg='#f0f0f0', bd=4, relief='ridge')
head_frame1.place(x=710, y=20, width=500, height=270)

# ************************************  CsId   ***************************************************************
csId = Label(head_frame1, text='Customer ID ', font=('times new roman', 14, 'bold'), bg='#f0f0f0')
csId.grid(row=1, column=0, pady=15, padx=4)

csId = Entry(head_frame1, font=('times new roman', 15), bg="white", fg="red", bd=3, width=20)
csId.grid(row=1, column=1, pady=15, padx=4)

# **************************** First Name ***********************************************************************
FirstN = Label(head_frame1, text="First Name", bg="#f0f0f0", font=("times new roman", 14, 'bold'))
FirstN.grid(row=2, column=0, pady=15, padx=4)

FirstN = Label(head_frame1, font=('times new roman', 15), bg='#f0f0f0', bd=2, fg='black', width=20, anchor='w')
FirstN.grid(row=2, column=1, pady=15, padx=4)

# ************************************* Last Name *******************************************
LastN = Label(head_frame1, text="Last Name", bg="#f0f0f0", font=("times new roman", 14, 'bold'))
LastN.grid(row=3, column=0, pady=15, padx=4)

LastN = Label(head_frame1, font=('times new roman', 15), bg='#f0f0f0', bd=2, fg='black', width=20, anchor='w')
LastN.grid(row=3, column=1, pady=15, padx=4)
# ************************************* Passport Num *******************************************
PassNum = Label(head_frame1, text="Passport ", bg="#f0f0f0", font=("times new roman", 15, 'bold'))
PassNum.grid(row=4, column=0, pady=15, padx=4)

PassNum = Label(head_frame1, font=('times new roman', 14), bg='#f0f0f0', bd=2, fg='black', width=20, anchor='w')
PassNum.grid(row=4, column=1, pady=15, padx=4)

button1 = Button(head_frame1, text="Search", font=('times new roman', 14, 'bold'), bg='#f7faf7', fg='black',
                 activebackground='red', activeforeground='white', command=find)
button1.grid(row=1, column=4, padx=15, pady=20)

# *************************************  THIRD FRAME  *******************************************

table = ttk.Treeview(root, columns=("FliNumber", "FliName", "Source", "Dep", "date", "DepTime", "arriTime", "Change$"),
                     show="headings")
table.column("FliNumber", width=70)
table.heading("FliNumber", text="Flight Number")

table.column("FliName", width=60)
table.heading("FliName", text="Flight Name")

table.column("Source", width=60)
table.heading("Source", text="Source")

table.column("Dep", width=60)
table.heading("Dep", text="Departure")

table.column("date", width=60)
table.heading("date", text="Date")

table.column("DepTime", width=70)
table.heading("DepTime", text="Departure Time")

table.column("arriTime", width=60)
table.heading("arriTime", text="Arrival Time")

table.column("Change$", width=60)
table.heading("Change$", text="Charge $")
table.place(x=30, y=310, width=650, height=300)

table.bind('<<TreeviewSelect>>', on_flight_selected)

# ***********************************************************************************************************************
head_frame2 = Frame(root, bg='#f0f0f0', bd=4, relief='ridge')
head_frame2.place(x=710, y=310, width=500, height=300)

# ************************************  Flight Number   ***************************************************************
FliNum = Label(head_frame2, text='Flight Number', font=('times new roman', 13, 'bold'), bg='#f0f0f0')
FliNum.place(x=10, y=10)

FliNumLab = Label(head_frame2, font=('times new roman', 14), bg='#f0f0f0', bd=2, fg='black', width=8
                  , anchor='w')
FliNumLab.place(x=140, y=10)

# ************************************  Flight Name   ***************************************************************
FliName = Label(head_frame2, text='Flight Name ', font=('times new roman', 13, 'bold'), bg='#f0f0f0')
FliName.place(x=10, y=50)

FliNameLab = Label(head_frame2, font=('times new roman', 14), bg='#f0f0f0', bd=2, fg='black', width=8, anchor='w')
FliNameLab.place(x=140, y=50)

# ************************************* Last Name *******************************************
depTime = Label(head_frame2, text="Departure Time", bg="#f0f0f0", font=("times new roman", 13, 'bold'))
depTime.place(x=10, y=90)

depTimeLab = Label(head_frame2, font=('times new roman', 14), bg='#f0f0f0', bd=2, fg='black', width=8, anchor='w')
depTimeLab.place(x=140, y=90)
# ************************************* Date *******************************************
Date = Label(head_frame2, text="Date", bg="#f0f0f0", font=("times new roman", 13, 'bold'))
Date.place(x=10, y=130)

Date = Label(head_frame2, font=('times new roman', 14), bg='#f0f0f0', bd=2, fg='black', width=8, anchor='w')
Date.place(x=140, y=130)
# ************************************* Class *******************************************
clas = Label(head_frame2, text="Class ", font=('times new roman', 15, 'bold'), bg='#f0f0f0')
clas.place(x=10, y=170)

n = StringVar()
clasChoosen = ttk.Combobox(head_frame2, width=25, textvariable=n)

claa_names = ['Economy', 'Premium Economy', 'Business', 'First class']
# Adding combobox drop down list
clasChoosen['values'] = claa_names

clasChoosen.place(x=140, y=170)
clasChoosen.current()

clasChoosen.bind('<<ComboboxSelected>>', update_price)
# ************************************* Price *******************************************
price = Label(head_frame2, text="Price", bg="#f0f0f0", font=("times new roman", 13, 'bold'))
price.place(x=10, y=210)

priceLab = Label(head_frame2, font=('times new roman', 14), bg='#f0f0f0', bd=2, fg='black', width=8, anchor='w')
priceLab.place(x=140, y=210)
# ************************************* Seats *******************************************
seats = Label(head_frame2, text="Seats", bg="#f0f0f0", font=("times new roman", 13, 'bold'))
seats.place(x=10, y=250)

seatsSpin = Spinbox(head_frame2, from_=1, to=4, font=('times new roman', 12))
seatsSpin.place(x=140, y=250)

# ***************************************total****************************************************
total = Label(root, text="Total Price: ", bg='sky blue', font=("times new roman", 18, 'bold'), fg='red')
total.place(x=450, y=620)

totalLab = Label(root, bg='sky blue', font=("times new roman", 18, 'bold'), fg='red')
totalLab.place(x=580, y=620)

# **********************Button*********************************************************************
bookButton = Button(root, text='Book', font=('times new roman', 15, 'bold'), bg='gray87', fg='red',
                    activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=3, command=book_and_update_price)

bookButton.place(x=1020, y=620)

BkButton = Button(root, text='Cancel', font=('times new roman', 15, 'bold'), bg='gray87', fg='black',
                  activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=3,
                  command=Exitt)

BkButton.place(x=1125, y=620)

root.mainloop()
