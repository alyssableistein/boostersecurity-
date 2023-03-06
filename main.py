from tkinter import *
from getpass import getpass
import tkinter as tk
from tkinter import messagebox
import re

interface = tk.Tk()
interface.title("Prototype")  # Interface title
interface.geometry("1000x700")  # Interface size



def checkPassword():
    if enter.get() == "":
        messagebox.showinfo("Error", "Please enter a password to check.")
    elif (len(enter.get())) < 12:
                messagebox.showinfo("Error", "Please enter a password with 12 or more characters.")

header = tk.Label(interface, text="Booster Security+", font=("Arial", 25, "bold"))
header.pack(ipadx=20, ipady=20)

inputText = Label(interface, text="Please enter password to check:", font=("Arial", 12))
inputText.pack(ipadx=10, ipady=10)

enter = tk.Entry(interface)
enter.pack(ipadx=10, ipady=10)

enterButton = Button(interface, text="Check Password", font=("Arial", 12), command=checkPassword)
enterButton.pack(ipadx=5, ipady=5)

interface.mainloop()











"""
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

textOut.grid(row = 4, column = 1)

Interface.mainloop()"""
