import time
import tkinter
from tkinter import *
from tkinter import messagebox

win = Tk()

app_running = True
size_m = 500
size_n = 500
s_x = s_y = 10  # Размер игрового поля
step_x = size_m // s_x  # Шаг по горизонтале
step_y = size_n // s_y  # Шак по вертикали
size_m = step_x * s_x
size_m = step_y * s_y

menu_x = 250


# функция нового окна закрытия окна
def on_closing():
    global app_running
    if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры?"):
        app_running = False
        win.destroy()


win.title("Морской бой")
win.protocol("WM_DELETE_WINDOW", on_closing)
canvas = Canvas(win, width=size_m, height=size_n, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_m, size_n, fill="white")
canvas.pack()

win.update()


#  функция для создания игрового поля
def draw_table():
    for i in range(0, s_x * 1):
        canvas.create_line(step_x * i, 0, step_x * i, size_m)
    for i in range(0, s_y * 1):
        canvas.create_line(0, step_y * i, size_n, step_y * i)


draw_table()


# функция для иконы
def icons():
    icons = tkinter.PhotoImage(file='battleship.png')
    win.iconphoto(False, icons)


icons()

while app_running:
    if app_running:
        win.update_idletasks()
        win.update()
    time.sleep(0.005)

win.mainloop()