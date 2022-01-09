import tkinter as tk

class Encrypt(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self)
        label = tk.Label(self, text="Hello from %s" % __file__)
        label.pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    gui = Encrypt(root)
    gui.pack(fill="both", expand=True)
    tk.mainloop()