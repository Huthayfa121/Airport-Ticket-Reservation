from tkinter import *  # to create GUI we will import tkinter
from PIL import ImageTk  # to import jpg image in our code
import os
import mysql.connector
from tkinter import ttk

def Exitt():
    main.destroy()  # Close the main login window
    os.system('python adminMain.py')  # Open the addCustomer.py page


main = Tk()
main.title('Ticket  Report')
main.geometry('1390x750+0+0')  # use geometry method to set width 1350 and height 700 from x 0 and y 0
main.configure(bg='white')

backgroundImage = ImageTk.PhotoImage(file='img/plan1.jpeg')  # ImageTk.PhotoImage allows as to use image from type jpg

bgLabel = Label(main, image=backgroundImage)

bgLabel.place(x=0, y=0)
# *******************************************************************************************************
frame = Frame(main)
frame.place(x=80, y=80, width=850, height=400)

table = ttk.Treeview(frame, columns=("tkNum", "flight_id", "cs_id", "class", "price", "seats", "date"), show="headings")

table.column("tkNum", width=50)
table.heading("tkNum", text="Ticket Number")

table.column("flight_id", width=50)
table.heading("flight_id", text="Flight Number")

table.column("cs_id", width=50)
table.heading("cs_id", text="Customer ID")

table.column("class", width=50)
table.heading("class", text="Class")

table.column("price", width=50)
table.heading("price", text="Price")

table.column("seats", width=50)
table.heading("seats", text="Seats")

table.column("date", width=50)
table.heading("date", text="date")


# Create a vertical scrollbar and associate it with the Treeview
vsb = Scrollbar(frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")

table.pack(expand=True, fill="both")
# ******************************************************************************************************

try:
    db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
    cur = db.cursor()
    cur.execute("SELECT * FROM ticket")
    # Fetch all rows
    rows = cur.fetchall()

    # Iterate over fetched rows and insert them into the Treeview table
    for row in rows:
        table.insert("", "end", values=row)

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if db.is_connected():
        cur.close()
        cur.close()

# ************************************* Cancel button ***************************************************

BkButton = Button(main, text='Cancel', font=('times new roman', 15, 'bold'), bg='gray85', fg='black',
                  activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=2,
                  command=Exitt)
BkButton.place(x=850, y=500)

main.mainloop()
