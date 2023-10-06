from src.item import Item


class MixinLang:
    """Независимый класс, в котором реализован функционал по смене языка раскладки"""
    LANGUAGE = 'EN'

    def __init__(self):
        self.__language = 'EN'
        MixinLang.__language = self.__language

    def change_lang(self):
        """Функция смены языка раслкдаки с запоминанием текущей раскладки"""
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLang):
    """Класс для товара 'клавиатура'"""
    pass
