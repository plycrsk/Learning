import tkinter as tk
Time_selected = tk.StringVar()
Task_selected = tk.StringVar()

def Printer():
    Time_selected.set(e1.get())
    Task_selected.set(e2.get())

master = tk.Tk()

tk.Label(master, textvariable=Time_selected).grid(row=0)
tk.Label(master, textvariable=Task_selected).grid(row=1)

master.mainloop()

import tkinter as tk

master = tk.Tk()

L = tk.Label(master, text='Timer Length?').grid(row=0)
L2 = tk.Label(master, text='Which Task?').grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b = tk.Button(master, text="Start", command=Printer).grid(row=3, column=0,  pady=4)

master.mainloop()
