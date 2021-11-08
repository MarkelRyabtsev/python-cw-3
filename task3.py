import math

from helper import Helper


class Task3:

    __task_number = 3

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дано натуральное n. Вычислить: 1 / (sin(1) + sin(n)')
        n = helper.set_natural_number('n')
        print('----------------------------------------------------------')
        self.__print_formula(n)
        print(f' = {self.__calculate(n)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __print_formula(n: int):
        count = 1
        while count <= n:
            if count == 1:
                print(f'1 / (sin(1))', end='')
            else:
                print(f'1 / (sin(1) + sin({count}))', end='')
            count += 1
            if count <= n:
                print(' + ', end='')

    @staticmethod
    def __calculate(n: int) -> float:
        value = 0.0
        count = 1
        while count <= n:
            value += 1 / (math.sin(n * (math.pi / 180)))
            count += 1

        return round(value, 2)
