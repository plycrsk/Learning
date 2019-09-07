#!/usr/bin/env python
# coding: utf-8

# In[2]:

import time

def Start_timer():          
    new_time = int(e1.get())*60
    #print(new_time)
    which_task = e2.get()
    #print(which_task)
    time_record = int(new_time/60)
    start_time=time.time()
    while new_time > 0:
        new_time -= 1
        Minutes = new_time//60
        Seconds = new_time%60
        #Current_time = print(Minutes, 'Minutes', Seconds, 'Seconds', end='\r')
        #L3 = tk.Label(master, text=Current_time).grid(row=4)
        time.sleep(1-((time.time()-start_time)%1))
        if new_time == 0:
            print('Time Up! Take a 5 Minute Break          ')
            sheep_timer_record = open("sheep_timer.txt", 'a')
        # print(time_record)
        # print(which_task)
        # print(time.gmtime())
            sheep_timer_record.writelines([str(time_record), ',', str(which_task), ',', str(time.gmtime()), '\n'])
            sheep_timer_record.close()

def Printer():
    Stopwatch = int(e1.get())
    Task = e2.get() 
    print(Stopwatch)
    print(Task)
    L3 = tk.Label(master, text=Stopwatch).grid(row=4)
    L4 = tk.Label(master, text=Task).grid(row=5)

import tkinter as tk

master = tk.Tk()

L = tk.Label(master, text='Timer Length?').grid(row=0)
L2 = tk.Label(master, text='Which Task?').grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b = tk.Button(master, text="Start", command=Start_timer).grid(row=3, column=0,  pady=4)
b2 = tk.Button(master, text="Stop", command=Printer).grid(row=3, column=1,  pady=4)

master.mainloop()

# In[ ]:




