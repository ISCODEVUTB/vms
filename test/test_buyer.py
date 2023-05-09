import unittest
from datetime import date
from logic.Address import Address
from logic.Buyer import Buyer
from test_Person import TestPerson


class TestBuyer(TestPerson):
    Buyer = Buyer()

    def test_instance(self):
        self.assertIsInstance(self.Buyer, Buyer, "it's a instance")

    def test_buy_date(self):
        self.assertEqual(self.Buyer.buy_date, date)

    def test__str__(self):
        self.assertEqual(self.Buyer.__str__(), '({0},{1},{2},{3},{4},{5},{6})'.format(1, 'Name', 'LastName',
                                                                                      1, Address(), 0, date))


if __name__ == '__main__':
    unittest.main()
