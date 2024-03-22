import tkinter as tk

from tkinter import ttk

root = tk.Tk()

root.title("Yaz Lib")
root.iconbitmap('icon.ico')
width, height = 500, 500
display_width= root.winfo_screenwidth()
display_height= root.winfo_screenheight()
left = int(display_width/2 - width/2)
top = int(display_height/2 - height/2)
root.geometry(f'{width}x{height}+{left}+{top}')


def button_click_func():
    label.configure(text=entry.get())
    #button.configure(state='disabled')


entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root,text='Click Me', command=button_click_func)
button.pack()

label = ttk.Label(root)
label.pack()





root.mainloop()