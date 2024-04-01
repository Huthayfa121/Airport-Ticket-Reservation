from tkinter import *  # to create GUI we will import tkinter
from PIL import ImageTk  # to import jpg image in our code
import os


def Exitt():
    main.destroy()  # Close the main login window
    os.system('python welcome.py')  # Open the addCustomer.py page


def addAdmin():
    main.destroy()
    os.system('python addAdmin.py')


def findAdmin():
    main.destroy()
    os.system('python findAdmin.py')


def findCustomer():
    main.destroy()
    os.system('python findCustomer.py')


def addFlight():
    main.destroy()
    os.system('python addFlight.py')


def findFlight():
    main.destroy()
    os.system('python findFlight.py')


def ticketsReport():
    main.destroy()
    os.system('python ticketsReport.py')


main = Tk()
main.title('Admin Main')
main.geometry('1390x750+0+0')  # use geometry method to set width 1350 and height 700 from x 0 and y 0
main.configure(bg='sky blue2')

# ********************define image for each menu****************************************
addAdminImage = PhotoImage(file='img/addAdmin.png')
findAdminImage = PhotoImage(file='img/search-profile.png')
findCustomerImage = PhotoImage(file='img/findCustomer.png')

# ********************************Create Setting menu bar*************************************
menubar = Menu(main)
main.config(menu=menubar)

SettingMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="HRM", menu=SettingMenu)
SettingMenu.add_command(label='Add admin', font=('times new roman', 10), image=addAdminImage, compound=LEFT,
                        command=addAdmin)
SettingMenu.add_command(label='Find admin', font=('times new roman', 10), image=findAdminImage, compound=LEFT,
                        command=findAdmin)
SettingMenu.add_separator()
SettingMenu.add_command(label='Find Customer', font=('times new roman', 10), image=findCustomerImage, compound=LEFT,
                        command=findCustomer)

# ********************define image for each menu****************************************
addFlightImage = PhotoImage(file='img/addFlight.png')
findFlightImage = PhotoImage(file='img/search.png')

# ********************************Create flight menu bar *************************************

flightMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Flight", menu=flightMenu)
flightMenu.add_command(label='Add flight', font=('times new roman', 10), image=addFlightImage, compound=LEFT,
                       command=addFlight)
flightMenu.add_command(label='Find flight', font=('times new roman', 10), image=findFlightImage, compound=LEFT,
                       command=findFlight)

# ********************define image for each menu****************************************
ticketImage = PhotoImage(file='img/airplane-ticket.png')

# ********************************Create Setting Bar menu *************************************

tktReportMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tickets Report", menu=tktReportMenu)
tktReportMenu.add_command(label='Flight Tickets', font=('times new roman', 10), image=ticketImage, compound=LEFT,
                          command=ticketsReport)

# **********************************Cancel******************************************************
BkButton = Button(main, text='Cancel', font=('times new roman', 15, 'bold'), bg='gray85', fg='black',
                  activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=2,
                  command=Exitt)
BkButton.place(x=1230, y=600)

main.mainloop()
