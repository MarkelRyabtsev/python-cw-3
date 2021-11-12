from helper import Helper


class Task6:

    __task_number = 6

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дано действительное число x, натуральное n. Вычислить: 1/x + 1/x(x+1) +..+ 1/x(x+1)...(x+n)')
        x = helper.set_real_number('x', False, 0)
        n = helper.set_natural_number('n')
        print('----------------------------------------------------------')
        self.__print_formula(x, n)
        print(f' = {self.__calculate(x, n)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __print_formula(x: float, n: int):
        count = 1
        formula = f'1/{x} + '
        while count <= n:
            denominator = ''
            for i in range(0, count + 1):
                denominator += f'({x} + {i})'
                if n != 0 and i != count:
                    denominator += ' * '
            formula += f'1/({denominator})'
            count += 1
            if count <= n:
                formula += ' + '
        print(formula)

    @staticmethod
    def __calculate(x: float, n: int) -> float:
        result = 1 / x
        count = 1
        while count <= n:
            denominator = x
            for i in range(0, count + 1):
                denominator *= (x + i)
            result += 1 / denominator
            count += 1

        return round(result, 2)
