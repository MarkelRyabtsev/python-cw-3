import math

from helper import Helper, Range


class Task1:

    __task_number = 1

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить z; Параметр y изменяется от y=yн=0,3 до y=yк=0,9  с шагом h6=0,2. a, x, t – константы.'
              '\nИспользовать цикл while или repeat')
        a = helper.set_real_number('a')
        x = helper.set_real_number('x')
        t = helper.set_real_number('t')
        y_start = 0.3
        y_stop = 0.9
        y_step = 0.2
        y_range = Range(
            y_start,
            y_stop,
            y_step
        )
        print('----------------------------------------------------------')
        values = self.__get_dict_values(y_range, a, x, t)
        for value in values:
            print(f'При y = {value}: z = {values[value]}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_dict_values(self, y_range: Range, a: float, x: float, t: float) -> dict[float, float]:
        dict_values = dict()
        y = y_range.start
        while y < y_range.stop:
            dict_values[round(y, 1)] = self.__get_z(y, a, x, t)
            y += y_range.step
        return dict_values

    @staticmethod
    def __get_z(y: float, a: float, x: float, t: float) -> float:
        return round((a * pow(x + ((4 / x) * math.log(y, math.e)), 1 / 3)) / abs(pow(t, 3)), 4)
