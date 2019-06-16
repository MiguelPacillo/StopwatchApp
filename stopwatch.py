from tkinter import *

window = Tk()
window.title("Timer App")
window.resizable(0, 0)
window.configure(background="white")

minlabel = Label(window, text="0", bg="white", fg="black", font="arial 20 bold")
minlabel.grid(row=0, column=0, pady=(20, 0), padx=20)

mintext = Label(window, text="Minutes", bg="white", fg="black", font="arial 20 bold")
mintext.grid(row=1, column=0, padx=20)

seclabel = Label(window, text="0", bg="white", fg="black", font="arial 20 bold")
seclabel.grid(row=0, column=1, pady=(20, 0), padx=20)

sectext = Label(window, text="Seconds", bg="white", fg="black", font="arial 20 bold")
sectext.grid(row=1, column=1, padx=20)

secs = 0
mins = 0

start = True

def counter():

    global secs, mins, start

    if start is not False:

        seclabel.after(1000, counter)

        secs += 1

        if secs == 60:

            secs = 0

            mins += 1

        minlabel.configure(text=str(mins))

        seclabel.configure(text=str(secs))

        startbutt.configure(state=DISABLED, bg="grey")



def stopper():

    global start

    start = False

startbutt = Button(window, text="Start", bg="green", fg="white", font="arial 20 bold", command=counter, state=NORMAL)
startbutt.grid(row=2, column=0, pady=20, padx=20)

stopbutt = Button(window, text="Stop", bg="red", fg="white", font="arial 20 bold", command=stopper)
stopbutt.grid(row=2, column=1, pady=20, padx=20)

window.mainloop()