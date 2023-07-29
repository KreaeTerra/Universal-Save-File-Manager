
import tkinter as tk
from shutil import copy2




#initialization and configuration of the main window
Window = tk.Tk()
Window.title("Save File Manager")
Window.geometry("300x80")


#creating the filepath entry boxes and their labels
source_label = tk.Label(text= "Source")
source_label.grid(row=0, column=0)

source_entry = tk.Entry(width= 35)
source_entry.insert(0, r"C:\Users\tugsa\Desktop\Saitama.plr")
source_entry.grid(row=0, column=1)

dest_label = tk.Label(text= "Destination")
dest_label.grid(row=1, column=0)

dest_entry = tk.Entry(width= 35)
dest_entry.insert(0, r"D:\Files\SaveBackup")
dest_entry.grid(row=1, column=1)



def SaveFile():
    copy2(str(source_entry.get()), str(dest_entry.get()))



save_button = tk.Button(text= "Save", command= SaveFile).grid(row=2, column=1)


tk.mainloop()

