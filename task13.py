import math
from helper import Helper


class Task13:

    __task_number = 13

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Определить, какая из двух фигур (круг или квадрат) имеет большую площадь. Известно, что сторона'
              '\nквадрата равна а, радиус круга r. Вывести на экран название и значение площади большей фигуры. ')
        a = helper.set_real_number('Сторона квадрата', True, 0)
        r = helper.set_real_number('Радиус круга', True, 0)
        print('----------------------------------------------------------')
        print(f'Большую площадь имеет: {self.__get_bigger_area(a, r)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_bigger_area(a: float, r: float) -> str:
        square_area = a * a
        circle_area = math.pi * (r * r)
        if square_area > circle_area:
            return f'Квадрат ({square_area})'
        elif circle_area > square_area:
            return f'Круг ({circle_area})'
        else:
            return f'Площади фигур равны ({square_area})'
