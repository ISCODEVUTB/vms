import json
import os
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class ShoppingController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'purchase.json')

    def show(self):
        with open(self.file, 'r') as file:
            json_object = json.load(file)
        return json_object

    def select(self, value):
        with open(self.file, 'r') as file:
            data = json.load(file)
        shopping_cart = [purchase for purchase in data.values() if value in purchase["dni"]]
        return shopping_cart
