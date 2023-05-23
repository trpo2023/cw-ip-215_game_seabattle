import tkinter
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Морской бой")

app_running = True
size_m = 500
size_n = 500

canvas = Canvas(win, width=size_m, height=size_n, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_m, size_n, fill="white")
canvas.pack()
win.update()

# функция нового окна закрытия окна
def on_closing():
    global app_running
    if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры?"):
        app_running = False
        win.destroy()


# функция для иконы
def icons():
    icons = tkinter.PhotoImage(file='battleship.png')
    win.iconphoto(False, icons)


icons()
win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()