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
        print('Дано натуральное n. Вычислить: 1/(sin(1) + 1/(sin(1)+sin(2)) + ... + 1/(sin(1)+...+sin(n))')
        n = helper.set_natural_number('n')
        print('----------------------------------------------------------')
        self.__print_formula(n)
        print(f' = {self.__calculate(n)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __print_formula(n: int):
        count = 1
        formula = ''
        while count <= n:
            denominator = ''
            for i in range(1, count + 1):
                denominator += f'sin({i})'
                if n != 0 and i != count:
                    denominator += ' + '
            formula += f'1/({denominator})'
            count += 1
            if count <= n:
                formula += ' + '
        print(formula)

    @staticmethod
    def __calculate(n: int) -> float:
        result = 0.0
        count = 1
        while count <= n:
            denominator = 0.0
            for i in range(1, count + 1):
                denominator += math.sin(i)
            result += 1 / denominator
            count += 1

        return round(result, 2)
