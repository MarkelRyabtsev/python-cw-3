from helper import Helper


class Task9:

    __task_number = 9

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Определить знак заданного целого числа. Ответом должно быть «+», «-», «0». Использовать оператор case')
        x = helper.set_real_number('x')
        print('----------------------------------------------------------')
        print(f'Знак заданного числа: {self.__get_sign(x)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_sign(x: float) -> str:
        if x > 0:
            return '"+"'
        elif x < 0:
            return '"-"'
        else:
            return '"0"'
