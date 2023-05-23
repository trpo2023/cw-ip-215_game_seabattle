from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Морской бой")

size_m = 500
size_n = 500

canvas = Canvas(win, width=size_m, height=size_n, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_m, size_n, fill="white")
canvas.pack()
win.update()

win.mainloop()

