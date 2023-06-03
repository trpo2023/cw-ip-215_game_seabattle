import random
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
ships = s_x  # определяем максимальное кол-во кораблей
ship_len1 = 1  # длина первого типа корабля
ship_len2 = 2  # длина второго типа корабля
ship_len3 = 3  # длина третьего типа корабля
ship_len4 = 4  # длина четвертого типа корабля
enemy_ships = [[0 for i in range(s_x + 1)] for i in range(s_y + 1)]
list_ids = []  # список объектов canvas

point_list = []  # список, куда мы кликнули мышкой

menu_x = 250

# points - список куда мы кликнули мышкой
points = [[-1 for i in range(s_x)] for i in range(s_y)]

# boom - список попаданий по кораблям противника
boom = [[0 for i in range(s_x)] for i in range(s_y)]


# функция нового окна закрытия окна
def on_closing():
    global app_running
    if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры?"):
        app_running = False
        win.destroy()


win.title("Морской бой")
win.resizable(False, False)
win.protocol("WM_DELETE_WINDOW", on_closing)
canvas = Canvas(win, width=size_m + menu_x, height=size_n, bd=0, highlightthickness=0)
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

def check_winner(x, y):
    win = False
    if enemy_ships[y][x] > 0:
        boom[y][x] = enemy_ships[y][x]
    sum_enemy_ships = sum(sum(i) for i in zip(*enemy_ships))
    sum_boom = sum(sum(i) for i in zip(*boom))
    print(sum_enemy_ships, sum_boom)
    if sum_enemy_ships == sum_boom:
        win = True
    return win


def check_winner2():
    win = True
    for i in range(0, s_x):
        for j in range(0, s_y):
            if enemy_ships[j][i] > 0:
                if points[j][i] == -1:
                    win = False
    print(win)
    return win


def button_show_enemy():
    for i in range(0, s_x):
        for j in range(0, s_y):
            if enemy_ships[j][i] > 0:
                color = "red"
                if points[j][i] != -1:
                    color = "green"
                _id = canvas.create_rectangle(i * step_x, j * step_y, i * step_x + step_x, j * step_y + step_y,
                                              fill=color)
                list_ids.append(_id)


def button_play_again():
    global list_ids
    global points
    for el in list_ids:
        canvas.delete(el)
    list_ids = []
    generate_enemy_ships()
    points = [[-1 for i in range(s_x)] for i in range(s_y)]


b0 = Button(win, text="Показать корабли противника", command=button_show_enemy)
b0.place(x=size_m + 20, y=30)

b1 = Button(win, text="Начать заново", command=button_play_again)
b1.place(x=size_m + 20, y=70)


def draw_point(x, y):
    print(enemy_ships[y][x])
    if enemy_ships[y][x] == 0:
        color = "red"
        id1 = canvas.create_oval(x * step_x, y * step_y, x * step_x + step_x, y * step_y + step_y, fill=color)
        id2 = canvas.create_oval(x * step_x + step_x // 3, y * step_y + step_y // 3, x * step_x + step_x - step_x // 3,
                                 y * step_y + step_y - step_y // 3, fill="white")
        list_ids.append(id1)
        list_ids.append(id2)
    if enemy_ships[y][x] > 0:
        color = "blue"
        id1 = canvas.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,
                                      y * step_y + step_y // 2 + step_y // 10, fill=color)
        id2 = canvas.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y,
                                      x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color)
        list_ids.append(id1)
        list_ids.append(id2)


def add_to_all(event):
    global points
    _type = 0  # ЛКМ
    if event.num == 3:
        _type = 1  # ПКМ
    # print(_type)
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    # print(mouse_x, mouse_y)
    ip_x = mouse_x // step_x
    ip_y = mouse_y // step_y
    print(ip_x, ip_y, "_type:", _type)
    if ip_x < s_x and ip_y < s_y:
        if points[ip_y][ip_x] == -1:
            points[ip_y][ip_x] = _type
            draw_point(ip_x, ip_y)
            if check_winner2():
                print("Победа!!!!!")
                points = [[10 for i in range(s_x)] for i in range(s_y)]
        print(len(list_ids))


canvas.bind_all("<Button-1>", add_to_all)  # ЛКМ
canvas.bind_all("<Button-3>", add_to_all)  # ПКМ


# функция для иконы
def icons():
    icon = tkinter.PhotoImage(file='battleship.png')
    win.iconphoto(True, icon)


icons()


def generate_enemy_ships():
    global enemy_ships
    ships_list = []
    # генерируем список случайных длин кораблей
    for i in range(0, ships):
        ships_list.append(random.choice([ship_len1, ship_len2, ship_len3]))

    # подсчет суммарной длины кораблей
    sum_1_all_ships = sum(ships_list)
    sum_1_enemy = 0

    while sum_1_enemy != sum_1_all_ships:
        # обнуляем массив кораблей врага
        enemy_ships = [[0 for i in range(s_x + 1)] for i in
                       range(s_y + 1)]  # +1 для доп. линии справа и снизу, для успешных проверок генерации противника

        for i in range(0, ships):
            len = ships_list[i]
            horizont_vertikal = random.randrange(1, 3)  # 1- горизонтальное 2 - вертикальное

            primerno_x = random.randrange(0, s_x)
            if primerno_x + len > s_x:
                primerno_x = primerno_x - len

            primerno_y = random.randrange(0, s_y)
            if primerno_y + len > s_y:
                primerno_y = primerno_y - len

            if horizont_vertikal == 1:
                if primerno_x + len <= s_x:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y][primerno_x - 1] + \
                                               enemy_ships[primerno_y][primerno_x + j] + \
                                               enemy_ships[primerno_y][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j]
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[primerno_y][primerno_x + j] = i + 1  # записываем номер корабля
                        except Exception:
                            pass
            if horizont_vertikal == 2:
                if primerno_y + len <= s_y:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y - 1][primerno_x] + \
                                               enemy_ships[primerno_y + j][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x - 1] + \
                                               enemy_ships[primerno_y + j][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j][primerno_x - 1]
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[primerno_y + j][primerno_x] = i + 1  # записываем номер корабля
                        except Exception:
                            pass

        # делаем подсчет 1ц
        sum_1_enemy = 0
        for i in range(0, s_x):
            for j in range(0, s_y):
                if enemy_ships[j][i] > 0:
                    sum_1_enemy = sum_1_enemy + 1


generate_enemy_ships()

while app_running:
    if app_running:
        win.update_idletasks()
        win.update()
    time.sleep(0.005)
