def printer():
    global user_input
    string = user_input.get()
    label3= tk.Label(root, text=string)
    label3.pack()

import tkinter as tk
root = tk.Tk()

root.title('Sheep Timer 1.0')

user_input = tk.Entry(root)
user_input.pack()
user_input.focus_set()

b = tk.Button(root, text='Timer Length?', command=printer)
b.pack(side='bottom')
root.mainloop()
