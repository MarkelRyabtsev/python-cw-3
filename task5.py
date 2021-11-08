from helper import Helper


class Task5:

    __task_number = 5

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Даны действительные положительные числа x, y, z. Выяснить, существует ли треугольник с длинами '
              '\nсторон x, y, z (треугольник существует, если длина каждой стороны меньше суммы двух  других сторон)')
        x = helper.set_real_number('x', True, 0.0)
        y = helper.set_real_number('y', True, 0.0)
        z = helper.set_real_number('z', True, 0.0)
        print('----------------------------------------------------------')
        print(f'Треугольник со сторанами:'
              f'\n x = {x}'
              f'\n y = {y}'
              f'\n z = {z}')
        print(self.__is_exist(x, y, z))
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __is_exist(x: float, y: float, z: float) -> str:
        if x < y + z and y < x + z and z < x + y:
            return 'Существует'
        else:
            return 'Не существует'
