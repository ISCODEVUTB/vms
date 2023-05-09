import unittest
from logic.Purchase import Purchase
from logic.Vehicle import Vehicle
from logic.Buyer import Buyer
from logic.Person import Person


class TestPurchase(unittest.TestCase):
    purchase = Purchase()

    def test_instance(self):
        self.assertIsInstance(self.purchase, Purchase, "It's instance")

    def test_id_purchase(self):
        self.assertEqual(self.purchase.id_purchase, 1)

    def test_description(self):
        self.assertIsInstance(self.purchase.description, Vehicle)

    def test_cost(self):
        self.assertEqual(self.purchase.cost, 1)

    def test_buyer(self):
        self.assertIsInstance(self.purchase.buyer, Buyer)

    def test_seller(self):
        self.assertIsInstance(self.purchase.seller, Person)

    def test__str__(self):
        self.assertEqual(self.purchase.__str__(), '({0}, {1}, {2}, {3}, {4})'.format(1, Vehicle(), 1.0, Buyer(), Person()))


if __name__ == '__main__':
    unittest.main()
