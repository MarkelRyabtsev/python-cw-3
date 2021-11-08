from helper import Helper


class Task12:

    __task_number = 12

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('В японском календаре принят двенадцатилетний цикл. Годы внутри цикла носят названия животных: крысы,'
              '\nкоровы, тигра, зайца, дракона, змеи, лошади, овцы, обезьяны, петуха, собаки, свиньи. Написать'
              '\nпрограмму, которая позволяет ввести номер года нашей эры и выводит его название по'
              '\nяпонскому календарю. (1996 г. – начало очередного цикла). Использовать оператор case')
        year = helper.set_natural_number('Введите год')
        print('----------------------------------------------------------')
        print(f'Название {year} г. по японскому календарю: {self.__get_year_name(year)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_year_name(year: int) -> str:
        start = 1996
        x_year = ((year - start) % 12) + 1
        if x_year == 1:
            return 'Крыса'
        elif x_year == 2:
            return 'Корова'
        elif x_year == 3:
            return 'Тигр'
        elif x_year == 4:
            return 'Заяц'
        elif x_year == 5:
            return 'Дракон'
        elif x_year == 6:
            return 'Змея'
        elif x_year == 7:
            return 'Лошадь'
        elif x_year == 8:
            return 'Овца'
        elif x_year == 9:
            return 'Обезьяна'
        elif x_year == 10:
            return 'Петух'
        elif x_year == 11:
            return 'Собака'
        elif x_year == 12:
            return 'Свинья'
        else:
            return 'Ошибка'
