import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone1():
    """Создаем экземпляр класса в фикстуре"""
    return Phone("КрутойСмартфон", 10000, 20, 2)


def test_repr(phone1):
    """TestCase №1 отображение в режиме отладки"""
    assert repr(phone1) == "Phone('КрутойСмартфон', 10000, 20, 2)"


def test_str(phone1):
    """TestCase №2 отображение в пользовательском режиме"""
    assert str(phone1) == 'КрутойСмартфон'


def test_add(phone1):
    """TestCase № 3 проверка сложения количества товаров экземпляров Item и Phone"""
    item1 = Item('iPhone', 50000, 6)
    assert item1 + phone1 == 26


def test_number_of_sim_2():
    """TestCase №4 вывод ошибки при нулевом значении количества сим-карт"""
    phone1 = Phone("КрутойСмартфон", 10000, 20, 0)
    assert phone1.number_of_sim == 0
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
