import math
from helper import Helper, Point


class Task14:

    __task_number = 14

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Определить, попадает ли точка M(x,y) в круг радиусом r с центром в точке (x0,y0). ')
        r = helper.set_real_number('Радиус круга', True, 0)
        x = helper.set_real_number('x')
        y = helper.set_real_number('y')
        m = Point(x, y)
        print('----------------------------------------------------------')
        print(f'{self.__is_point_inside(m, r)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __is_point_inside(m: Point, r: float) -> str:
        hyp = math.sqrt(m.x ** 2 + m.y ** 2)
        if r >= hyp:
            return f'Точка принадлежит кругу'
        else:
            return f'Точка не принадлежит кругу'
