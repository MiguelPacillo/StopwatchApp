from tkinter import *

window = Tk()
window.title("Stopwatch App")
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

secs = -1
mins = 0

start = True

def counter():

    global secs, mins, start

    if start is True:

        seclabel.after(1000, counter)

        secs += 1

        if secs == 60:

            secs = 0

            mins += 1

        minlabel.configure(text=str(mins))

        seclabel.configure(text=str(secs))

        startbutt.configure(state=DISABLED, bg="grey")
        stopbutt.configure(state=NORMAL, bg="red")

def stopper():

    global start

    start = False

    stopbutt.configure(state=DISABLED, bg="grey")
    clearbutt.configure(state=NORMAL, bg="blue")


def clearer():

    global start, secs, mins

    secs = -1
    mins = 0

    minlabel.configure(text="0")
    seclabel.configure(text="0")

    clearbutt.configure(state=DISABLED, bg="grey")
    startbutt.configure(state=NORMAL, bg="green")

    start = True

stopbutt = Button(window, text="Stop", bg="grey", fg="white", font="arial 15 bold", command=stopper, state=DISABLED)
stopbutt.grid(row=2, column=1, pady=20, padx=20)

clearbutt = Button(window, text="Clear", bg="grey", fg="white", font="arial 15 bold", command=clearer, state=DISABLED)
clearbutt.grid(row=3, column=1, pady=20, padx=20)

startbutt = Button(window, text="Start", bg="green", fg="white", font="arial 15 bold", command=counter, state=NORMAL)
startbutt.grid(row=2, column=0, pady=20, padx=20)

window.mainloop()