from helper import Helper


class Task15:

    __task_number = 15

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Написать программу ввода буквы, цифры или спецзнака. Выводить сообщения «Это цифра …» или «Это буква …»,'
              '\n«Это спецзнак …». К сообщению добавлять саму цифру, букву или спецзнак. Использовать оператор case')
        symbol = helper.set_one_symbol("Введите ОДИН символ")
        print('----------------------------------------------------------')
        self.__check_symbol(symbol)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __check_symbol(symbol: str):
        if symbol.isnumeric():
            print(f'{symbol} - это цифра')
        elif symbol.isalpha():
            print(f'{symbol} - это буква')
        else:
            print(f'{symbol} - это спец символ')
