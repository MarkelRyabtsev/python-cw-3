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
        print('Дано действительное число x, натуральное n. Вычислить: x ( x - n )( x - 2 n )( x - 3 n )…( x - n2 )')
        x = helper.set_real_number('x')
        n = helper.set_natural_number('n')
        print('----------------------------------------------------------')
        self.__print_formula(x, n)
        print(f' = {self.__calculate(x, n)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __print_formula(x: float, n: int):
        count = 0
        while count <= n:
            print(f'({x} - {count} * {n})', end='')
            count += 1
            if count <= n:
                print(' * ', end='')

    @staticmethod
    def __calculate(x: float, n: int) -> float:
        value = 1
        count = 0
        while count <= n:
            value *= x - (count * n)
            count += 1

        return round(value, 2)
