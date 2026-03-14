class ZeroProductQuantity(Exception):
    """ Класс, для формирования ошибки при добавлении товара с нулевым количеством. """
    message: str

    def __init__(self, message: str):
        """ Метод - конструктор, для формирования исключения. """
        super().__init__(message)