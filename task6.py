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
        print('Написать программу простейшего калькулятора (сложение, вычитание, умножение, деление).'
              '\nПредусмотреть невозможность деления на 0. Использовать оператор case.')
        x = helper.set_real_number('x')
        y = helper.set_real_number('y')
        operation = helper.set_math_operation('Операция')
        print('----------------------------------------------------------')
        result = self.__calculate(x, y, operation)
        print(f'{x} {operation} {y} = {result}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __calculate(x: float, y: float, operation: str) -> str:
        if operation == '+':
            return str(x + y)
        elif operation == '-':
            return str(x - y)
        elif operation == '*':
            return str(x * y)
        elif operation == '/':
            if y == 0.0:
                print('Нельзя делить на 0!')
                return 'Ошибка!'
            return str(x / y)
        else:
            print('Ошибка!')
