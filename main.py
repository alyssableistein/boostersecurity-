from tkinter import *
from getpass import getpass
import tkinter as tk
from tkinter import messagebox
import re

interface = tk.Tk()
interface.title("Prototype")  # Interface title
interface.geometry("1020x720")  # Interface size

def showPassword():
    if enter.cget('show') == '*':
        enter.config(show='')
    else:
        enter.config(show='*')

def checkPassword():
    if enter.get() == "":
        messagebox.showinfo("Error", "Please enter a password to check.")
    elif (len(enter.get())) < 12:
                messagebox.showinfo("Error", "Please enter a password with 12 or more characters.")
    elif not re.search("[a-z]", enter.get()):
                messagebox.showinfo("Error", "Please enter a password with at least one lowercase letter.")
    elif not re.search("[0-9]", enter.get()):
                messagebox.showinfo("Error", "Please enter a password with at least one number")
            
header = tk.Label(interface, text="Booster Security+", font=("Arial", 25, "bold"))
header.pack(ipadx=20, ipady=20)

inputText = Label(interface, text="Please enter a password to test the strength:", font=("Arial", 12))
inputText.pack(ipadx=10, ipady=10)

enter = tk.Entry(interface, show="*")
enter.pack(ipadx=10, ipady=10)

hideAndShow = Checkbutton(interface, text="show password", command=showPassword)
hideAndShow.pack()

enterButton = Button(interface, text="Check Password", font=("Arial", 12), command=checkPassword)
enterButton.pack()

interface.mainloop()
