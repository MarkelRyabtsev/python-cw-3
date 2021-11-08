import math
from helper import Helper


class Task8:

    __task_number = 8

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Из величин, определяемых выражениями a=sinx, b=cosx, c=ln|x| при заданном х,'
              '\nопределить и вывести на экран дисплея минимальное значение')
        x = helper.set_real_number('x')
        a = round(math.sin(x), 4)
        b = round(math.cos(x), 4)
        c = round(math.log(abs(x), math.e), 4)
        print('----------------------------------------------------------')
        self.__check_min(a, b, c, x)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __check_min(a: float, b: float, c: float, x: float):
        min_value = min([a, b, c])

        if a == min_value:
            print(f'Минимальное значение: a = sin({x}) = {a}')
        elif b == min_value:
            print(f'Минимальное значение: b = cos({x}) = {b}')
        else:
            print(f'Минимальное значение: c = ln(|{x}|) = {c}')

