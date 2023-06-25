import pytest

from src.item import Item
from src.keyboard import Keyboard
from src.phone import Phone


@pytest.fixture
def test_item():
    return Item('One', 2, 3)


@pytest.fixture
def test_phone():
    return Phone('Two', 4, 5, 6)


@pytest.fixture
def test_keyboard():
    return Keyboard('Three', 7, 8)
