from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """Инициализация наследованного класса с добавлением нового атрибута"""
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __str__(self):
        """Отображение в пользовательском режиме"""
        return f'{self.name}'

    def __repr__(self) -> str:
        """Отображение в режиме отладки"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        """Возвращает количество сим-карт"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Проверяет, что количество сим-карт больше нуля"""
        if value < 1 or not isinstance(value, int):
            raise ValueError('Количество физических SIM-карт должно быть больше нуля')
        else:
            self.__number_of_sim = value

    def __add__(self, other):
        """
        Складывает экземпляры класса `Phone` и `Item` (сложение по количеству товара в магазине)
        Проверяет, чтобы нельзя было сложить `Phone` или `Item` с экземплярами не `Phone` или `Item` классов.
        """
        if not issubclass(other.__class__, self.__class__):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

