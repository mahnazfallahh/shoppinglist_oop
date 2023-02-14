import pandas as pd
from abc import ABC, abstractmethod


class FactoryPrice(ABC):

    def __init__(self, category):
        self.category = category

    @abstractmethod
    def display_price(self):
        pass

    def call_price(self):
        product = self.display_price()
        result = product.show_price()
        return result


class DisplayGroceryPrice(FactoryPrice):
    def display_price(self):
        return GroceryPrice()


class DisplayCosmeticsPrice(FactoryPrice):
    def display_price(self):
        return CosmeticPrice()


class DisplayVegetablePrice(FactoryPrice):
    def display_price(self):
        return VegetablePrice()


class GroceryPrice:
    @staticmethod
    def show_price():
        """ method for display grocery prices and items in one simple table """
        data = {
            '': [90000, 1000, 80000]
        }
        grocery = pd.DataFrame(data, index=['walnut', 'rice', 'sugar'])
        print("\N{peanuts}", "GROCERY PRICES", "\N{peanuts}")
        return grocery


class CosmeticPrice:
    @staticmethod
    def show_price():
        """ method for display cosmetics prices and items in one simple table """ # noqa E501
        data = {
            '': [3400000, 1200, 340000]
        }
        cosmetics = pd.DataFrame(data, index=['lipstick', 'cream', 'spray'])
        print("\N{nail polish}", "COSMETICS PRICES", "\N{nail polish}")
        return cosmetics


class VegetablePrice:
    @staticmethod
    def show_price():
        """ method for display vegetable prices and items in one simple table """ # noqa E501
        data = {
            '': [4000, 40000, 1000]
        }
        vegetable = pd.DataFrame(data, index=['cucumber', 'carrot', 'lettuce'])
        print("\N{leafy green}", "VEGETABLE PRICES", "\N{leafy green}")
        return vegetable


def client(category, format):
    formats = {
        'grocery': DisplayGroceryPrice,
        'cosmetics': DisplayCosmeticsPrice,
        'vegetable': DisplayVegetablePrice
    }
    result = formats[category](format)
    return result.call_price()
