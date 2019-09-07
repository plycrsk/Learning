import tkinter as tk
import time

def stop_watch():
    label.configure(text=time.strftime("%H: %M: %S"))
    root.after(1000, stop_watch)

root = tk.Tk()
label = tk.Label(root, text="Time Remaining")
label.pack()
stop_watch()
root.mainloop()
