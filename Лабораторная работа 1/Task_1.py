class Mouse:
    def __init__(self, color: str, number_of_ears, model_type: str):
        self.health = None
        if not isinstance(color, str):
            raise TypeError('Название цвета str')
        self.color = color
        if number_of_ears < 0:
            raise TypeError('Количество ушек не может быть отрицательным числом.')
        self.number_of_ears = number_of_ears
        if not isinstance(model_type, str):
            raise TypeError('Модель str')
        self.model_type = model_type

    def broken(self):
        print('Это не лабораторная мышь')
        self.health = 0


class Word:
    def __init__(self, number_of_words: int, heading: str):
        if not isinstance(number_of_words, int):
            raise TypeError('Количество слов должно быть числом')
        if number_of_words > 500:
            raise ValueError('Количество слов не должно превышать 500')
        self.number_of_words = number_of_words
        if not isinstance(heading, str):
            raise TypeError('Название str')
        self.heading = heading


class Bottle:
    def __init__(self, wrap_status, liquid_status, liquid_capacity):
        """
        Создание объекта класса "бутылка"
        :param wrap_status: статус бутылки (открыта или закрыта), задаётся латинскими буквами "C" или "O"
        :param liquid_status: текущее количество жидкости в бутылке
        :param liquid_capacity: вместимость бутылки

        Примеры:
        >>> my_bottle = Bottle(0, 10, 100) # инициализация экземпляра класса
        """

        if (wrap_status != 0) and (wrap_status != 1):
            raise ValueError("bottle must be opened (0) or closed (1)")
        self.wrap_status = wrap_status
        if not isinstance(liquid_status, (int, float)):
            raise TypeError("Wrong type for liquid_status")
        if not isinstance(liquid_capacity, (int, float)):
            raise TypeError("Wrong type for liquid_capacity")
        if liquid_status > liquid_capacity:
            raise ValueError("Capacity must be graiter than occupied volume")
        if liquid_status < 0:
            raise ValueError("Amount of liquid must not be lesser than zero")
        if liquid_capacity < 0:
            raise ValueError("Amount of liquid must not be lesser than zero")
        self.liquid_status = liquid_status
        self.liquid_capacity = liquid_capacity

    def open_bottle(self):
        """
        Функция открывает бутылку, если та была закрыта,
        в случае успеха выводится сообщение (бутылка открыта).
        :raise ValueError: вызывает ошибку, если бутылка была открыта при вызове метода
        Примеры:
        >>> my_bottle = Bottle(1, 10, 100)
        >>> my_bottle.open_bottle()
        """

    def close_bottle(self):
        """
        Функция закрывает бутылку, если та была открыта,
        в случае успеха выводится сообщение (бутылка закрыта).
        :raise ValueError: вызывает ошибку, если бутылка была закрыта при вызове метода
        Примеры:
        >>> my_bottle = Bottle(0, 10, 100)
        >>> my_bottle.close_bottle()
        """

    def add_liquid(self, liquid_input):
        """
        Функция добавляет жидкость в бутылку, если бутылка открыта
        :raise TypeErroe: вызывает ошибку при попытке налить не целое и не вещественное число жидкости
        :raise ValueError: вызывает ошибку при попытке переполнить бутылку или налить отрицательные значения
        :return: новое число занятого объёма бутылки
        примеры:
        >>> my_bottle = Bottle(0, 10, 100)
        >>> my_bottle.add_liquid(50)
        """


if __name__ == "__main__":
    mouse_model = Mouse('Белая', 2, '1')
    IVT_conditions = Word(488, 'Проверка условий IVT')
    import doctest

    pass
    doctest.testmod()
