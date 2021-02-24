
'''
Convertors function that do the conversions and visualisation of result.

'''
from tkinter import *
from tkinter import messagebox
from conv_package import widgets


def binary_to_decimal(value):

    #Converting the binary IP-framed value into binary.
    #Creating a new window to visualise the result.

    top = Toplevel()
    splitted = value.split('.')
    decimal_value = [''for x in splitted]
    try:
        IP_position = 0
        for x in splitted:
            value = 0
            iterator = '76543210'
            for i in range(8):
                if x[i] == '1':
                 value += 2**int(iterator[i])
        decimal_value[IP_position] = str(value)
        IP_position += 1
    
    except:
           messagebox.showerror("Value error", "The value inserted are not correct, please try again")   
           top.destroy()
           return None

    else:       
         converted = '.'.join(decimal_value)
   
         sub_frame = LabelFrame(top,padx = 5, pady = 5)
         sub_frame.grid(row = 9, column = 0,padx = 100, pady = 20)
         Label(sub_frame,text = f"Result: {converted}").grid(row= 0, column = 0)
   
    
    
    
def decimal_to_binary(value):

    #Converting the binary IP-framed value into binary

    top = Toplevel()
    splitted = value.split('.')
    bin_value = ['' for x in splitted]
    IP_position = 0

    try:
        for x in splitted:
            decimal = int(x)
            iterator = '76543210'
            value = ['0','0','0','0','0','0','0','0']
            count = 0
            for i in range(8):
                divisor = int(iterator[i])
                if decimal / (2**divisor) >= 1:
                    value[count] = '1'
                    decimal = decimal - 2**divisor
                count +=1    
           
            conv_value = ''
            for bit in value:
                conv_value = conv_value + bit
            bin_value[IP_position] = conv_value
            IP_position += 1
    except:
           messagebox.showerror("Value error", "The value inserted are not correct, please try again")   
           top.destroy()
           return None    
    else:
        converted = '.'.join(bin_value)
 
        sub_frame = LabelFrame(top,padx = 5, pady = 5)
        sub_frame.grid(row = 9, column = 0,padx = 100, pady = 20)
        Label(sub_frame,text = f"Result: {converted}").grid(row= 0, column = 0)
   
    
   