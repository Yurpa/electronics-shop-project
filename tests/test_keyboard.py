"""Здесь надо написать тесты с использованием pytest для модуля phone."""


import pytest


# Homework-4

def test__init__(test_keyboard):
    assert test_keyboard.name == 'Three'
    assert test_keyboard.price == 7
    assert test_keyboard.quantity == 8
    assert test_keyboard.language == 'EN'
    test_keyboard.language = 'RU'
    assert test_keyboard.language == 'RU'
    with pytest.raises(AttributeError):
        test_keyboard.language = 'ES'
    test_keyboard.change_lang()
    test_keyboard.change_lang()
    assert test_keyboard.language == 'RU'
