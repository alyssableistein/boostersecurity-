from tkinter import *
import tkinter as tk

interface = tk.Tk()
interface.title("Prototype")  # Interface title
interface.geometry("1280x720")  # Interface size

# create label with project title
projectTitle = Label(interface, text="Welcome To Booster Security+!", font='Arial 30 bold')
# send label text to be seen on the interface
projectTitle.pack()

# create label to tell users to enter their password to check
userPass = Label(interface, text="Please enter password to check:", font='Arial 15')
#send label text to be seen on the interface
userPass.pack()

# this will be the user's password entered in as an entry
e = Entry(interface, width=80)
e.pack() 

#
def enterButtonClicked():
    userPassword = Label(interface, text=e.get())
    userPassword.pack()
enterButton = tk.Button(interface, text="Enter", width="15", font="Arial 18", command=enterButtonClicked)
enterButton.pack()

interface.mainloop()













# String Variable Initialization
rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()


# Function that makes the reset button set all the String Values to nothing.
def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


# Labels

"""
textInp = Label(Interface, font = ('arial', 20, 'bold'),
                text="Enter your Plaintext:", bd = 10, anchor = "w")

textInp.grid(row = 0, column = 0)

textOutLbl = Label(encoder, font = ('arial', 20, 'bold'),
                   text="Results:", bd = 10, anchor = "w")

textOutLbl.grid(row = 4, column = 0)

# Text Input
plainText = Entry(encoder, font = ('arial', 16, 'bold'),
                textvariable = rand, bd = 10, insertwidth = 6,
                justify = 'left')

plainText.grid(row = 0 , column = 1)

textOut = Entry(encoder, font = ('arial', 16, 'bold'),
                textvariable = Result, bd = 10, insertwidth = 6,
                justify = 'left')

textOut.grid(row = 4, column = 1) """

Interface.mainloop()
