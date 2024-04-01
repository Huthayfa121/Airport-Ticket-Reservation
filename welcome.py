from tkinter import *
from PIL import ImageTk  # to import jpg image in our code
import os


def Exitt():
    main.destroy()


def Login():
    main.destroy()  # Close the main login window
    os.system('python login.py')

def add():
    main.destroy()  # Close the main login window
    os.system('python customerMain.py')

main = Tk()

main.title('Welcome')  # set title

main.geometry('1360x760+0+0')  # use geometry method to set width 1350 and height 700 from x 0 and y 0

# main.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='img/plan.jpg')

bgLabel = Label(main, image=backgroundImage)

bgLabel.place(x=0, y=0)  # to see the image in our window from x=0 and y=0

TlImage = ImageTk.PhotoImage(file='img/1111.jpg')
mainFrame = Frame(main, bg='#a5d1e4')  # Setting bg parameter to empty string creates a frame without any background color

mainFrame.place(x=350, y=180)

tLabel = Label(mainFrame, text='Welcome In Airline Reservation\n System', font=('times new roman', 20, 'bold'),
               bg='#a5d1e4')

# row=0, column=0 because inside this login frame this is the first thing getting added, pady = padding in y-axis
tLabel.grid(row=0, column=1)

# ********************************Air Travel*******************************
airTrav = PhotoImage(file='img/airpor.png')
airTravLabel = Label(mainFrame, image=airTrav, bg='#a5d1e4')

airTravLabel.grid(row=1, column=0, padx=20, pady=10)

airButton = Button(mainFrame, text='Air Travel', font=('times new roman', 15, 'bold', 'italic'), bg='#a5d1e4', fg='black',
                   activebackground='light sky blue', activeforeground='black', cursor='hand2', command=add)
airButton.grid(row=2, column=0, padx=20, pady=5)

# ********************************admin***************************************
adminLog = PhotoImage(file='img/admi.png')
adminLabel = Label(mainFrame, image=adminLog, bg='#a5d1e4')

adminLabel.grid(row=1, column=2, padx=15, pady=10)

adminButton = Button(mainFrame, text='Admin Login', font=('times new roman', 15, 'bold', 'italic'), bg='#a5d1e4',
                     fg='black',
                     activebackground='light sky blue', activeforeground='black', cursor='hand2', command=Login)
adminButton.grid(row=2, column=2, padx=20, pady=5)

# **********************************Exit**************************************

Exit = PhotoImage(file='img/logou.png')
ExitLabel = Label(mainFrame, image=Exit, compound=BOTTOM, bg='#a5d1e4')

ExitLabel.grid(row=3, column=1, pady=10)

loginButton = Button(mainFrame, text='Exit', font=('times new roman', 15, 'bold', 'italic'), bg='#a5d1e4', fg='black',
                     activebackground='light sky blue', activeforeground='black', cursor='hand2', width=6,
                     command=Exitt)
loginButton.grid(row=4, column=1, pady=5)


main.mainloop()
