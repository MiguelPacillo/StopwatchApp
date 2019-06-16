from tkinter import *
from tkinter.ttk import Separator

# Draw tkinter window
window = Tk()
window.title("Stopwatch App")
window.resizable(0, 0)
window.configure(background="white")

# Adds a label for minutes and seconds as well as captions
minlabel = Label(window, text="0", bg="white", fg="black", font="arial 20 bold")
minlabel.grid(row=0, column=0, pady=(20, 0), padx=10)

mintext = Label(window, text="Minutes", bg="white", fg="black", font="arial 20 bold")
mintext.grid(row=1, column=0, padx=10)

seclabel = Label(window, text="0", bg="white", fg="black", font="arial 20 bold")
seclabel.grid(row=0, column=2, pady=(20, 0), padx=10)

sectext = Label(window, text="Seconds", bg="white", fg="black", font="arial 20 bold")
sectext.grid(row=1, column=2, padx=10)

midline = Separator(window, orient="vertical")
midline.grid(row=0, column=1, sticky="ns", rowspan=2)

# Seconds starts at -1 because when you press Start it immediately adds a second for some reason
secs = -1
mins = 0

start = True

def counter():  # Function for counting up the time when you press start

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

def stopper():  # Function for stopping the count

    global start

    start = False

    stopbutt.configure(state=DISABLED, bg="grey")

    clearbutt.after(1000)  # To prevent a bug where if you press clear too quickly it'll start the counter
    clearbutt.configure(state=NORMAL, bg="blue")


def clearer():  # Function for clearing the counter

    global start, secs, mins

    secs = -1
    mins = 0

    minlabel.configure(text="0")
    seclabel.configure(text="0")

    clearbutt.configure(state=DISABLED, bg="grey")
    startbutt.configure(state=NORMAL, bg="green")

    start = True

startbutt = Button(window, text="Start", bg="green", fg="white", font="arial 15 bold", command=counter, state=NORMAL)
startbutt.grid(row=2, column=0, pady=20)

stopbutt = Button(window, text="Stop", bg="grey", fg="white", font="arial 15 bold", command=stopper, state=DISABLED)
stopbutt.grid(row=2, column=1, pady=20)

clearbutt = Button(window, text="Clear", bg="grey", fg="white", font="arial 15 bold", command=clearer, state=DISABLED)
clearbutt.grid(row=2, column=2, pady=20)

window.mainloop()