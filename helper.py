class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Range:

    def __init__(self, start: float, stop: float, step: float):
        self.start = start
        self.stop = stop
        self.step = step


class Helper:

    @staticmethod
    def set_one_symbol(description: str) -> str:
        while True:
            value = input(f'{description} : ')
            if len(value) != 1:
                print(f'Введите только один символ!')
                continue
            return value

    @staticmethod
    def set_real_number(description: str, only_positive: bool = False, not_equal: float = None) -> float:
        while True:
            try:
                value = float(input(f'{description} : '))
                if only_positive:
                    if value < 0:
                        print(f'Введенное число должно быть больше 0!')
                        continue
                if not_equal is not None and value == not_equal:
                    print(f'Введенное число должно отличаться от {not_equal}!')
                    continue
                return value
            except:
                print('Введенное значение не является вещественным числом, повторите!')
                continue

    @staticmethod
    def set_natural_number(description: str, numbers_range: range = None) -> int:
        while True:
            try:
                value = int(input(f'{description} : '))
                if value < 1:
                    print('Число должно быть больше 0!')
                    continue
                if numbers_range is not None and value not in numbers_range:
                    print(f'Введенное число должно быть в диапозоне от {numbers_range.start} до {numbers_range.stop}!')
                    continue
                return value
            except:
                print('Введенное значение не является натуральным числом, повторите!')
                continue

    @staticmethod
    def set_math_operation(description: str) -> str:
        while True:
            value = str(input(f'{description} : '))
            if value == '+' or value == '-' or value == '*' or value == '/':
                return value
            else:
                print('Введите + - * или /')
                continue
