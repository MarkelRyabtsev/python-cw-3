import math
from helper import Helper, Point


class Task11:

    __task_number = 11

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Определить, какая из двух точек - M1(x1,y1) или M2(x2,y2) - расположена ближе к началу координат.'
              '\nВывести на экран дисплея координаты этой точки')
        x1 = helper.set_real_number('x1')
        y1 = helper.set_real_number('y1')
        x2 = helper.set_real_number('x2')
        y2 = helper.set_real_number('y2')
        point_m_1 = Point(x1, y1)
        point_m_2 = Point(x2, y2)
        print('----------------------------------------------------------')
        print(f'К началу координат ближе: {self.__get_point(point_m_1, point_m_2)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_point(m1: Point, m2: Point) -> str:
        distance_m_1 = math.sqrt(m1.x ** 2 + m1.y ** 2)
        distance_m_2 = math.sqrt(m2.x ** 2 + m2.y ** 2)

        if distance_m_1 < distance_m_2:
            return f'M1({m1.x}, {m1.y})'
        elif distance_m_2 < distance_m_1:
            return f'M2({m2.x}, {m2.y})'
        else:
            return 'Точки расположены одинаково'
