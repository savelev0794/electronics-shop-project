"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone
from src.item import InstantiateCSVError


@pytest.fixture
def item1():
    """Создаем экземпляр класса в фикстуре"""
    return Item("КрутойСмартфон", 10000, 20)


def test_apply_discount(item1):
    """TestCase №1 применение скидки"""
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_calculate_total_price(item1):
    """TestCase №2 общая стоимость товара в магазине"""
    assert item1.calculate_total_price() == 200000


def test_name(item1):
    """TestCase №3 проверка имени"""
    assert item1.name == 'КрутойСмартфон'


def test_len_name():
    """TestCase №4 максимальная длина имени"""
    item1 = Item('ДлинныйСмартфон', 100, 20)
    assert len(item1.name) >= 10


def test_len_cut(item1):
    """TestCase №5 обрезка имени имени"""
    item1.name = 'КрутойСмартфон'
    assert item1.name == 'КрутойСмар'


def test_string_to_number(item1):
    """TestCase №6 возвращение числа из строки"""
    string_to_number = item1.string_to_number('5.4')
    assert string_to_number == 5


def test_instantiate_from_csv():
    """TestCase №7 создание объекта из файла csv"""
    Item.all = []
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5


def test_repr(item1):
    """TestCase №8 отображение в режиме отладки"""
    assert repr(item1) == "Item('КрутойСмартфон', 10000, 20)"


def test_str(item1):
    """TestCase №8 отображение в пользовательском режиме"""
    assert str(item1) == 'КрутойСмартфон'


def test_add(item1):
    """TestCase № 9 сложение товаров экземпляров Item и Phone"""
    phone1 = Phone('iPhone', 50000, 6, 1)
    assert item1 + phone1 == 26


def test_file_not_found_error():
    """TestCase № 10 вывод сообщения об ошибке при отсутствующем файле"""
    with pytest.raises(FileNotFoundError):
        assert Item.instantiate_from_csv('') == print('FileNotFoundError: Отсутствует файл item.csv')


def test_instantiate_csv_error():
    """TestCase № 11 вывод сообщение об ошибке при поврежденном файле"""
    with pytest.raises(InstantiateCSVError):
        assert Item.instantiate_from_csv('../tests/test_items.csv') == print('InstantiateCSVError:'
                                                                             'Файл item.csv поврежден')
