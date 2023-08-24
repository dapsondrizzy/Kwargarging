from tkinter import *
from time import strftime
import time
root=Tk()
root.title('Alarm')

def set_time():
    pattern=strftime('%I:%M:%S')
    label.config(text=pattern)
    label.after(10,time)

label=Label(root,font=('Playbill',80),background='black',foreground='blue')
label.pack(anchor='center')




def start_end_time():
    while True:
        
        start=int(input())
        if start == 0 or start < 1:
            raise Exception('enter a hour format between range 1 and 12')
        
        continue
        

            

    
    