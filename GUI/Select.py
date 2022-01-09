from tkinter.messagebox import showinfo
import tkinter
from tkinter import *
from tkinter import ttk
import time
from tkinter import messagebox


class Select(Frame):
    def Encrypt():
        pass
    
    def __init__(self, window):
        Frame.__init__(self)
        label = Label(self, text="Hello from %s" % __file__)
        label.pack(padx=20, pady=20)
        button1 = Button(self, text='Encrypt',width=20,bg='brown',fg='white',command=Encrypt)
        button2 = Button(self, text='Decrypt',width=20,bg='brown',fg='white',command=Decrypt)
        button3 = Button(self, text='Download',width=20,bg='brown',fg='white',command=Download)
        button1.place()
        button2.pack()
        button3.pack()
        

if __name__ == "__main__":
    root = Tk()
    root.geometry("500x500")
    root.mainloop()
    

