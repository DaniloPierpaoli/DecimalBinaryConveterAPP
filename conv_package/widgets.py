
from tkinter import *
from tkinter import messagebox
from conv_package import convertors

def popup():
    response = messagebox.showerror("Wrong input","Your input is not correct, please insert a valid value")

        
def button_click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))

  
    
def button_clear():
    entry.delete(0,END)
    entry.insert(0,'')
    
def cancel():
    to_cancel = entry.get()
    entry.delete(0,END)
    splitted = []
    for letter in to_cancel:
        splitted.append(letter)
    splitted.pop()
    new = "".join(splitted)
    entry.insert(0,new)

def ask_confirmation():
    return messagebox.askyesno("Confirm your choice","Please confirm your choice")

def clicked(value):
    global conv_type
    conv_type = value
    response = ask_confirmation()
    if response == True:
        inserting()
        

def returning():
    value = entry.get()
    top.destroy()
    if conv_type == 'binary':
        convertors.binary_to_decimal(value)
    else:
        convertors.decimal_to_binary(value)

def inserting():
    global entry
    global top
    top = Toplevel()
    entry = Entry(top, width = 35,borderwidth = 5)
    entry.insert(0,"Insert here the IP address")
    
    button_r = Button(top, text = "Send", padx = 40, pady = 20, command = returning)
    button1 = Button(top, text = 1, padx = 40, pady=20,command = lambda: button_click(1))
    button2 = Button(top, text = 2, padx = 40, pady=20,command = lambda: button_click(2))
    button3 = Button(top, text = 3, padx = 40, pady=20,command = lambda: button_click(3))
    button4 = Button(top, text = 4, padx = 40, pady=20,command = lambda: button_click(4))
    button5 = Button(top, text = 5, padx = 40, pady=20,command = lambda: button_click(5))
    button6 = Button(top, text = 6, padx = 40, pady=20,command = lambda: button_click(6))
    button7 = Button(top, text = 7, padx = 40, pady=20,command = lambda: button_click(7))
    button8 = Button(top, text = 8, padx = 40, pady=20,command = lambda: button_click(8))
    button9 = Button(top, text = 9, padx = 40, pady=20,command = lambda: button_click(9))
    button0 = Button(top, text = 0, padx = 40, pady=20,command = lambda: button_click(0))
    buttondot = Button(top, text = '.', padx = 40, pady=20,command = lambda: button_click('.'))
    buttonCancel = Button(top, text = "Cancel", padx = 40, pady = 20, command = cancel)
    buttonClear = Button(top, text = "Clear All", padx = 70, pady = 20, command = button_clear)
    #Put the buttons on the screen
    entry.grid(row = 0, column = 0, columnspan = 3)
    buttonCancel.grid(row = 4, column = 3)
    button_r.grid(row = 0, column = 3)
    button1.grid(row = 3,column = 0)
    button2.grid(row =  3, column =1)
    button3.grid(row =  3, column =2)
    button4.grid(row = 2 , column =0)
    button5.grid(row =  2, column =1)
    button6.grid(row =  2, column =2)
    button7.grid(row = 1 , column =0)
    button8.grid(row =  1, column =1)
    button9.grid(row = 1 , column =2)
    button0.grid(row =  4, column =0)
    buttonClear.grid(row= 4, column = 1, columnspan = 2)
    buttondot.grid(row = 2, column = 3)        