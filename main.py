from tkinter import *
from tkinter import ttk
import tkinter as tk

import random
import time
import datetime
import math
import base64
import hashlib

Interface = Tk()
Interface.title("Prototype")  # Interface title
Interface.geometry("600x400")  # Interface size

# bottomframe = Frame(Interface)
# bottomframe.pack(side=BOTTOM)



# def update_width():
#     frame.config(width=100)


Label(Interface, text='Enter Password').grid(row=5)
e1 = Entry(Interface)
e1.grid(row=5, column=1)

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
