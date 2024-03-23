import tkinter as tk

from tkinter import ttk

root = tk.Tk()

root.title("Yaz Lib")
root.iconbitmap('icon2.ico')
width, height = 500, 500
display_width= root.winfo_screenwidth()
display_height= root.winfo_screenheight()
left = int(display_width/2 - width/2)
top = int(display_height/2 - height/2)
root.geometry(f'{width}x{height}+{left}+{top}')




label0 = ttk.Label(root)
label0.pack()
label0.configure(text="Calculator")


def button_func(num01,num02):
    sum = num01+num02
    Answer.set(f'Answer is {sum}')


num1 = tk.IntVar()
num2 = tk.IntVar()
Answer = tk.StringVar()


entry1 = ttk.Entry(root , textvariable=num1)
entry1.pack()

entry2 = ttk.Entry(root, textvariable=num2)
entry2.pack()

Button = ttk.Button(root, text="Calculate" , command=lambda: button_func(num1.get(), num2.get()))
Button.pack()


label = ttk.Label(root, textvariable=Answer)
label.pack()





root.mainloop()