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

if __name__ == '__main__':
    unittest.main()