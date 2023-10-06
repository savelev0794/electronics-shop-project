import pytest
from src.keyboard import Keyboard


@pytest.fixture
def kb():
    """Создаем экземпляр класса в фикстуре"""
    return Keyboard('Logitech 123', 5000, 2)


def test_name(kb):
    """TestCase #1 отображение имени"""
    kb = Keyboard('Logitech 123', 5000, 2)
    assert str(kb) == 'Logitech 123'


def test_lang(kb):
    """TestCase #2 отображнеие языка раскладки по умолчанию"""
    assert str(kb.language) == 'EN'


def test_change_lang(kb):
    """TestCase #3 функция смены языка раслкдаки"""
    kb.change_lang()
    assert str(kb.language) == 'RU'
    kb.change_lang()
    assert str(kb.language) == 'EN'


def test_wrong_lang(kb):
    """TestCase #4 вывод ошибки при смене на несуществующую раскладку"""
    with pytest.raises(AttributeError):
        kb.language = 'CH'
