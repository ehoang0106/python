from tkinter import *
from tkinter.ttk import *
import datetime
import platform
try:
        import winsound
        type='windows'
except:
        import os
        type='other'
window = Tk()
window.title("Clock")
window.geometry('300x250')
window.resizable(False, False)
window.configure(bg = 'green')
def clock():
        date_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S/%p")
        date,time1 = date_time.split()
        time2,time3 = time1.split('/')
        hour,minutes,seconds =  time2.split(':')
        if int(hour) > 11 and int(hour) < 24:
                time = str(int(hour)) + ':' + minutes + ':' + seconds + ' ' + time3
        else:
                time = time2 + ' ' + time3
        time_label.config(text = time)
        date_label.config(text= date)
        time_label.after(1000, clock)

tabs_control = Notebook(window)
clock_tab = Frame(tabs_control)
tabs_control.add(clock_tab, text="Clock")
tabs_control.pack(expand = 1, fill ="both")
time_label = Label(clock_tab, font = 'calibri 30 bold', foreground = 'blue')
time_label.pack(anchor='center')
date_label = Label(clock_tab, font = 'calibri 30 bold', foreground = 'blue')
date_label.pack(anchor='s')

clock()
window.mainloop()