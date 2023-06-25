"""Здесь надо написать тесты с использованием pytest для модуля phone."""


import pytest


# Homework-4


def test__init__(test_phone):
    assert test_phone.name == 'Two'
    assert test_phone.number_of_sim == 6
    test_phone.number_of_sim = 7
    assert test_phone.number_of_sim == 7
    with pytest.raises(ValueError):
        test_phone.number_of_sim = -1


def test__str__(test_phone):
    assert str(test_phone) == 'Two'


def test__repr__(test_phone):
    assert repr(test_phone) == "Phone('Two', 4, 5, 6)"
