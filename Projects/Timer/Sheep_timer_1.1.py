#!/usr/bin/env python
# coding: utf-8

# In[2]:

import time

def Start_timer():          
    new_time = (int(input("Timer length in Minutes? ")))*60
    which_task = (input("Task? "))
    time_record = int(new_time/60)
    start_time=time.time()
    while new_time > 0:
        new_time -= 1
        Minutes = new_time//60
        Seconds = new_time%60
        print(Minutes, 'Minutes', Seconds, 'Seconds', end='\r')
        time.sleep(1-((time.time()-start_time)%1))
        if new_time == 0:
            print('Time Up! Take a 5 Minute Break          ')
            sheep_timer_record = open("sheep_timer.txt", 'a')
        # print(time_record)
        # print(which_task)
        # print(time.gmtime())
            sheep_timer_record.writelines([str(time_record), ',', str(which_task), ',', str(time.gmtime()), '\n'])
            sheep_timer_record.close()

import tkinter as tk

master = tk.Tk()

Label(master, text='Timer Length?').grid(row=0)

b = tk.Button(master, text="Start", command=Start_timer)
b.pack()
master.mainloop()

# In[ ]:




