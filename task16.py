import math
from helper import Helper


class Task16:

    __task_number = 16

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить значение функции Y для заданного пользователем значения X')
        x = helper.set_real_number("X")
        a = self.__get_a(x)
        b = self.__get_b(x)
        y = self.__get_y(a, b)
        print('----------------------------------------------------------')
        a_formula = f'cos({x})' if x >= 0 else f'sin({x})'
        print(f'a = {a_formula} = {a}')
        print(f'b = √(1 / ({x} + 1)) = {b}')
        y_formula = f'1 / ({a} + {b})' if a <= b else f'{a} + √{b}'
        print(f'y = {y_formula} = {y}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_a(x: float) -> float:
        if x >= 0:
            return round(math.cos(x), 4)
        else:
            return round(math.sin(x), 4)

    @staticmethod
    def __get_b(x: float) -> float:
        return round(math.sqrt(1 / (x + 1)), 2)

    @staticmethod
    def __get_y(a: float, b: float) -> float:
        if a <= b:
            return round(1 / (a + b), 4)
        else:
            return round(a + math.sqrt(b), 4)
