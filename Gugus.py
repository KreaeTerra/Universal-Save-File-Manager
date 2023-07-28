
import tkinter as tk
from shutil import copy2




#initialization and configuration of the main window
Window = tk.Tk()
Window.title("Save File Manager")
Window.geometry("300x80")

#creating the filepath entry boxes and their labels
source_label = tk.Label(root, text= "Source").grid(row=0, column=0)
source_entry = tk.Entry(root).grid(row=0, column=1)
dest_label = tk.Label(root, text= "Destination").grid(row=1, column=0)
dest_entry = tk.Entry(root).grid(row=1, column=1)


def SaveFile(source_entry, dest_entry):
    source = source_entry.get()
    dest = dest_entry.get()

    print(source, dest)



save_button = tk.Button(root, text= "Save", command=SaveFile).grid(row=2, column=1)


tk.mainloop()

