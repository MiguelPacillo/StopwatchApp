import time
from tkinter import *

'''
xsecs = 0
secs = 0
mins = 0

while True:
    time.sleep(1/60)
    xsecs += 1

    if xsecs == 60:
        secs += 1
        xsecs = 0

    if secs == 60:
        mins += 1
        secs = 0

    print(str(secs) + "." + str(xsecs) + " seconds and " + str(mins) + " minutes.")

'''
window = Tk()
window.title("Timer App")
window.resizable(0, 0)
window.geometry("400x250")
window.configure(background="white")

minlabel = Label(window, text="0", bg="white", fg="black", font="arial 20 bold")
minlabel.grid(row=0, column=0)

mintext = Label(window, text="Minutes", bg="white", fg="black", font="arial 20 bold")
mintext.grid(row=1, column=0)

seclabel = Label(window, text="0", bg="white", fg="black", font="arial 20 bold")
seclabel.grid(row=0, column=1)

sectext = Label(window, text="Seconds", bg="white", fg="black", font="arial 20 bold")
sectext.grid(row=1, column=1)

window.mainloop()
