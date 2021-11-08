from helper import Helper


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
        print('Определить и вывести на печать номер квадранта, в  котором расположена точка М(x, y),'
              '\nx и y заданные вещественные числа)')
        x = helper.set_real_number('x', False, 0)
        y = helper.set_real_number('y', False, 0)
        print('----------------------------------------------------------')
        print(f'Точка М({x}, {y}) лежит в квадранте {self.__get_quadrant(x, y)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_quadrant(x: float, y: float) -> int:
        if x * y > 0:
            return 1 if x > 0.0 and y > 0.0 else 3
        else:
            return 2 if x < 0.0 < y else 4
