from helper import Helper


class Task4:

    __task_number = 4

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Для введенной последовательности целых чисел признаком конца которой является ноль определить'
              '\nмаксимальное число, сумму всех чисел и среднее арифметическое. Использовать цикл repeat.')
        sequence = helper.set_sequence("Введите последовательность целых чисел", 0)
        print('----------------------------------------------------------')
        print(f'Максимальное число: {self.__get_max(sequence)}')
        print(f'Сумма всех чисел: {self.__get_sum(sequence)}')
        print(f'Среднее арифметическое: {self.__get_average(sequence)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_max(sequence: list[int]) -> int:
        try:
            max_number = 0
            for number in sequence:
                if number > max_number:
                    max_number = number
            return max_number
        except:
            print('Ошибка')

    @staticmethod
    def __get_sum(sequence: list[int]) -> int:
        try:
            total_sum = 0
            for number in sequence:
                total_sum += number
            return total_sum
        except:
            print('Ошибка')

    @staticmethod
    def __get_average(sequence: list[int]) -> float:
        try:
            total_sum = 0
            for number in sequence:
                total_sum += number
            return round(total_sum / len(sequence), 2)
        except:
            print('Ошибка')
