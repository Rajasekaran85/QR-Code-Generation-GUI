import pyqrcode
import png
import os
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext



def conv():
    print("\n QR Code Generation\n")
    print("\n Date: 26 April 2023 \n\n")
    qrvalue = qrval.get("1.0",'end-1c')
    qr = pyqrcode.create(qrvalue)
    qr.svg("qrcode.svg", scale = 8)
    qr.png('qrcode.png', scale = 6)
    messagebox.showinfo("QR Code Generation", "Completed")
    

def Clear():
	qrval.delete("1.0","end")         # for clearing the text widget values use 1.0 to end

root = Tk()
root.geometry("400x400")
root.title("QR Code Generation")
root.config(bg='#5CB5FA') 

lbl1 = Label(root, text='QR Code Generation', font='helvetica 15', bg='#5CB5FA')
lbl1.pack(pady=10)
qrval = Text(root, height=6, width=25, font=("Courier", 12))
qrval.pack(pady=25)
button1 = Button(root, text="Submit", command=conv, bg='royalblue', fg = 'white').pack(pady=25)
button2 = Button(root, text="Clear", command=Clear, bg='royalblue', fg = 'white').pack(pady=25)

mainloop()

