
import tkinter as tk
from shutil import copy2

Window = tk.Tk()
Window.title("Save File Manager")
Window.geometry("300x50")

source_label = tk.Label(text= "Source").grid(row=0, column=0)
source_entry = tk.Entry().grid(row=0, column=1)
dest_label = tk.Label(text= "Destination").grid(row=1, column=0)
dest_entry = tk.Entry().grid(row=1, column=1)


tk.mainloop()

