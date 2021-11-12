import math
from helper import Helper, Range


class Task7:

    __task_number = 7

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить w; Параметр x изменяется от x=xн=1 до x=xк=4,5  с шагом h=0,5. a, z, y – константы.'
              '\nИспользовать цикл while или repeat')
        a = helper.set_real_number('a')
        z = helper.set_real_number('z')
        y = helper.set_real_number('y')
        x_start = 1.0
        x_stop = 4.5
        x_step = 0.5
        x_range = Range(
            x_start,
            x_stop,
            x_step
        )
        print('----------------------------------------------------------')
        values = self.__get_dict_values(x_range, a, z, y)
        for value in values:
            print(f'При x = {value}: w = {values[value]}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_dict_values(self, x_range: Range, a: float, z: float, y: float) -> dict[float, float]:
        try:
            dict_values = dict()
            x = x_range.start
            while x <= x_range.stop:
                dict_values[round(x, 1)] = self.__get_w(a, x, z, y)
                x += x_range.step
            return dict_values
        except:
            print('Ошибка входных данных')
            return dict()

    @staticmethod
    def __get_w(a: float, x: float, z: float, y: float) -> float:
        try:
            return round((a * x ** 2 + math.sin(z) ** 2) / math.sqrt(1 + pow(math.e, y)), 4)
        except:
            raise Exception
