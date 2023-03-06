from tkinter import *
from getpass import getpass
import tkinter as tk
from tkinter import messagebox
import re

#create the interface to work in
interface = tk.Tk()
interface.title("Prototype")  # Interface title
interface.geometry("1020x720")  # Interface size

#define showPassword so users can see their input or keep it confidential
def showPassword():
    if enter.cget('show') == '*':
        enter.config(show='')
    else:
        enter.config(show='*')

#define checkPassword. This will check all of the requirements that the user's password needs in order for it to be a valid input
def checkPassword():
    if enter.get() == "": #check if there is no input
        messagebox.showinfo("Error", "Please enter a password to check.") #prompt user for text input
    elif (len(enter.get())) < 12: #check the length of the user's password if it is more than 12 characters
                messagebox.showinfo("Error", "Please enter a password with 12 or more characters.") #prompt user for more characters
    elif not re.search("[a-z]", enter.get()): #check for lowercase letters
                messagebox.showinfo("Error", "Please enter a password with at least one lowercase letter.") #prompt user to use a lowercase letter
    elif not re.search("[A-Z]", enter.get()): #check for uppercase letters
                messagebox.showinfo("Error", "Please enter as password with at least one uppercase letter") #prompt user to use a uppercase letter
    elif not re.search("[0-9]", enter.get()): #check for numbers in password
                messagebox.showinfo("Error", "Please enter a password with at least one number.") #prompt user to enter a number
    elif re.search("\s" , enter.get()): #check for spacing
                messagebox.showinfo("Error", "Please enter a password with no spaces.") #prompt user to not enter spaces
    elif not re.search("[_@$]" , enter.get()): #check for special characters
                messagebox.showinfo("Error", "Please enter at least one character being a valid special character.") #prompt user to input a valid special character


header = tk.Label(interface, text="Booster Security+", font=("Arial", 25, "bold"))#create a top header with tool name
header.pack(ipadx=20, ipady=20) #display onto the screen and set the padding for x & y coordinates 

inputText = Label(interface, text="Please enter a password to test the strength:", font=("Arial", 12)) #prompt user to enter text
inputText.pack(ipadx=10, ipady=10) #display onto the screen and set the padding for x & y coordinates

enter = tk.Entry(interface, show="*") #create the text entry box for users to input the password they are checking
enter.pack(ipadx=10, ipady=10) #display onto the screen and set the padding for x & y coordinates

hideAndShow = Checkbutton(interface, text="show password", command=showPassword) #create a checkbox to show password and link it to the showPassword command
hideAndShow.pack() #display onto the screen and set the padding for x & y coordinates

enterButton = Button(interface, text="Check Password", font=("Arial", 12), command=checkPassword) #create the check password button where users can enter their password and it will check for the strength
enterButton.pack() #display onto the screen and set the padding for x & y coordinates

interface.mainloop()
