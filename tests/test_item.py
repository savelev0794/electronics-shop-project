"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item1():
    """Создаем экземпляр класса в фикстуре"""
    return Item("Смартфон", 10000, 20)


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
    assert item1.name == 'Смартфон'


def test_len_name():
    """TestCase №4 максимальная длины имени"""
    item1 = Item('ДлинныйСмартфон', 100, 20)
    assert len(item1.name) >= 10


def test_string_to_number(item1):
    """TestCase №5 возвращение числа из строки"""
    string_to_number = item1.string_to_number('5.4')
    assert string_to_number == 5