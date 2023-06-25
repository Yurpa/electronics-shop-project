import csv
import os


class InstantiateCSVError(Exception):

    def __init__(self, message):
        self.message = message


class Item:
    """
    Main Class for project
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __str__(self):
        return self.__name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            raise ValueError('Складывать можно только объекты Item')

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            return print('Длина наименования товара превышает 10 символов.')

    @name.getter
    def name(self): return  self.__name

    @classmethod
    def instantiate_from_csv(cls, filename='items.csv'):
        try:
            Item.all.clear()
            file = os.path.join(os.path.dirname(__file__), filename)
            with open(file, newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        name, price, quantity = row['name'], row['price'], row['quantity']
                        cls(name, price, quantity)
                    except (KeyError, ValueError):
                        raise InstantiateCSVError(f'Файл {filename} поврежден')
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {filename}')

    @staticmethod
    def string_to_number(data):
        num = float(data)
        return int(num)


class MixinLanguage:
    languages = ('EN', 'RU')

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if language in self.languages:
            self.__language = language
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self
