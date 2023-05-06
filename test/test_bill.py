import unittest
from logic.Purchase import Purchase
from logic.Bill import Bill
from logic.Person import Person
from logic.Buyer import Buyer
from logic.Address import Address
from logic.Payment_Method import PaymentMethod


class TestBill(unittest.TestCase):
    Bill = Bill()

    def test_instance(self):
        self.assertIsInstance(self.Bill, Bill, "It's instance.")

    def test_id_bill(self):
        self.assertEqual(self.Bill.id_bill, 1)

    def test_description_purchase(self):
        self.assertIsInstance(self.Bill.description_purchase, Purchase)

    def test_seller(self):
        self.assertIsInstance(self.Bill.seller, Person)

    def test_buyer(self):
        self.assertIsInstance(self.Bill.buyer, Buyer)

    def test_address_buyer(self):
        self.assertIsInstance(self.Bill.address_buyer, Address)

    def test_payment_method(self):
        self.assertIsInstance(self.Bill.payment_method, PaymentMethod)

    def test_(self):
        self.assertEqual(self.Bill.__str__(), '({0}, {1}, {2}, {3}, {4}, {5})'.format(1, Purchase().__str__(),
                                                                                      Person().__str__(),
                                                                                      Buyer().__str__(),
                                                                                      Address().__str__(),
                                                                                      PaymentMethod().__str__()))


if __name__ == '__main__':
    unittest.main()
