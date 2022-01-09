
from tkinter.messagebox import showinfo
import tkinter
from tkinter import *
from tkinter import ttk
import time
from tkinter import messagebox
import Select
import Encrypt


def service_changed(event):
    cloud = CloudProvider.get()
    if cloud == "AWS":
        label_1.place(x=68,y=180)
        entry_1.place(x=240,y=180)
        label_2.place(x=70,y=230)
        entry_2.place(x=240,y=230)

def button1click():
    messagebox.showinfo("Information", "Correctly entered")
    return


root = Tk()
root.geometry('500x500')
root.title("Register")
label_0 = Label(root, text="Secure File Storage",width=20,font=("bold", 20))
label_0.place(x=90,y=60)

label_select = Label(root, text="Cloud Provider",width=20,font=("bold", 10))
label_select.place(x=68,y=130)

selected_cloud= StringVar()
CloudProvider = ttk.Combobox(root, textvariable=selected_cloud)
CloudProvider.place(x=240,y=130)
CloudProvider['values'] = ["AWS" , "GCLOUD" , "IBM" , "AZURE"]
CloudProvider['state'] = 'readonly'
CloudProvider.bind('<<ComboboxSelected>>', service_changed)
label_1 = Label(root, text="AWS Access Key",width=20,font=("bold", 10))

entry_1 = Entry(root)

label_2 = Label(root, text="AWS Secret Access Key",width=20,font=("bold", 10))

entry_2 = Entry(root)

button1 = Button(root, text='Submit',width=20,bg='brown',fg='white',command=button1click)
button1.place(x=100,y= 280)


button2 = Button(root,text='Clear',width=20,bg='brown',fg='white')
button2.place(x=300,y= 280)


# it is use for display the registration form on the window
root.mainloop()