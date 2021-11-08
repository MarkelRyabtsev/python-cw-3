import math
from helper import Helper


class Task10:

    __task_number = 10

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить значение функции Y для заданного пользователем значения X')
        x = helper.set_real_number('x')
        a = self.__get_a(x)
        b = self.__get_b(x)
        y = self.__get_y(a, b)
        print('----------------------------------------------------------')
        print(f'a = (1 / ({x} + 5)) - (1 / ({x} - 9)) = {a}')
        b_formula = f'cos({x})' if x >= 0 else f'sin({x})'
        print(f'b = {b_formula} = {b}')
        print(f'y = √({a} + {b}) = {y}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_a(x: float) -> float:
        return round((1 / (x + 5)) - (1 / (x - 9)), 2)

    @staticmethod
    def __get_b(x: float) -> float:
        if x >= 0:
            return round(math.cos(x), 4)
        else:
            return round(math.sin(x), 4)

    @staticmethod
    def __get_y(a: float, b: float) -> float:
        try:
            return round(math.sqrt(a + b), 2)
        except:
            print('Ошибка!')
