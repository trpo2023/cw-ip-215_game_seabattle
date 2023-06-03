import unittest
from tkinter import *
from main import *
from inspect import signature

class MainTest(unittest.TestCase):
    # Тест размера окна
    def test_WindowSize(self):
        self.assertEqual(size_m, 500)
        self.assertEqual(size_n, 500)
    # Тест корректности названия иконки
    def test_Icons(self):
        self.assertEqual(icon_tag, "battleship.png")
    # Тест на количество аргументов
    def test_ValueFunctoins(self):
        cw_arg = signature(check_winner)
        ata_arg = signature(add_to_all)
        dp_arg = signature(draw_point)
        self.assertEqual(len(cw_arg.parameters), 2)
        self.assertEqual(len(ata_arg.parameters), 1)
        self.assertEqual(len(dp_arg.parameters), 2)
    # Тест на тип массива
    def test_ArrayType(self):
        self.assertEqual(generate_enemy_ships(), True)
    # Тест на параметры окна
    def test_WindowSettings(self):
        self.assertEqual(s_x, 10)
        self.assertEqual(s_y, 10)
        self.assertEqual(step_x, 50)
        self.assertEqual(step_y, 50)
        self.assertEqual(ships, 10)
        self.assertEqual(ship_len1, 1)
        self.assertEqual(ship_len2, 2)
        self.assertEqual(ship_len3, 3)
        self.assertEqual(ship_len4, 4)

if __name__ == '__main__':
    unittest.main()