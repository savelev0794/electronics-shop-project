"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    """TestCase №1 общая стоимость товара в магазине"""
    Item("помидор", 10000, 5)
    assert 50000


def test_apply_discount():
    """TestCase №2 применение скидки"""
    Item.pay_tate = 0.8
    Item("помидор", 10000, 5)
    assert 8000
