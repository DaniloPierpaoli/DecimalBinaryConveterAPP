'''
Main loop event script. It then calls other functions when the choice has been made.

'''



from tkinter import *
from tkinter import messagebox
from conv_package import widgets, convertors


root = Tk()
root.title("Simple IP Converter")
input_bar = Entry(width = 35,borderwidth = 5)

    
   
       

        
        
    
frame = LabelFrame(root,padx = 5, pady = 5)
frame.grid(row = 1, column = 0, padx = 200, pady = 20)
my_label = Label(frame,text = "Hello and welcome to IP converter tool. Please choose which convertion you need to calculate, then click enter")
my_label.grid(row = 1, column = 0)
modes = [
    # (What you visualise, the value)
    ("Binary to decimal","binary"),
    ("Decimal to binary","decimal"),
 
] 
choice = StringVar()
choice.set("Choose your conversion type")

buttonsBin = Radiobutton(root, text = "Binary to decimal", variable =  choice, value = "binary").grid(row = 2, column = 0)
buttonsDec = Radiobutton(root, text = "Decimal to binary", variable =  choice, value = "decimal").grid(row = 4, column = 0)
button = Button(root, text = 'Enter',command = lambda: widgets.clicked(choice.get())).grid(row  = 6, column = 0)   
    


if __name__ == '__main__':
    root.mainloop()
