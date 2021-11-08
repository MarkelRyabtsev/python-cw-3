import math
from helper import Helper


class Task4:

    __task_number = 4

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить значение a при t')
        x = helper.set_real_number("x")
        t1 = helper.set_real_number("t1")
        t2 = helper.set_real_number("t2")
        print('----------------------------------------------------------')
        a = self.__get_a(t1, t2, x)
        a_formula = f'{self.__get_a_formula(t1, t2, x)}'
        print(f'a = {a_formula} = {a}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_a(t1: float, t2: float, x: float) -> float:
        try:
            if t1 < math.sqrt(t2 + 2):
                return round(pow(math.e, 2 * t1) + math.cos(x * t2), 4)
            elif t1 > math.sqrt(t2 + 2):
                return round(x * t1, 4)
            else:
                return round(math.log(x * t1, math.e) * math.sqrt(math.sin(t2)), 4)
        except:
            print('Ошибка')

    @staticmethod
    def __get_a_formula(t1: float, t2: float, x: float) -> str:
        try:
            if t1 < math.sqrt(t2 + 2):
                return f'e^(2 * {t1}) + cos({x} * {t1})'
            elif t1 > math.sqrt(t2 + 2):
                return f'{x} * {t1}'
            else:
                return f'ln({x} * {t1}) * √(sin({t1}))'
        except:
            print('Ошибка')
