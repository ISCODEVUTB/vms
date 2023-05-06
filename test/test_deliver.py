import unittest
from datetime import date
from logic.Address import Address
from logic.Bill import Bill
from logic.Buyer import Buyer
from logic.Deliver import Deliver
from logic.Person import Operator, Person
from logic.Supplier import Supplier


class TestDeliver(unittest.TestCase):
    Deliver = Deliver()

    def test_instance(self):
        self.assertIsInstance(self.Deliver, Deliver, "It's instance")

    def test_id_deliver(self):
        self.assertEqual(self.Deliver.id_deliver, 1)

    def test_date(self):
        self.assertIsInstance(self.Deliver.date, date)

    def test_buyer(self):
        self.assertIsInstance(self.Deliver.buyer, Buyer)

    def test_buyer_add(self):
        self.assertIsInstance(self.Deliver.buyer_add, Address)

    def test_operator(self):
        self.assertIsInstance(self.Deliver.operator, Operator)

    def test_operator_add(self):
        self.assertIsInstance(self.Deliver.operator_add, Address)

    def test_conveyor(self):
        self.assertIsInstance(self.Deliver.conveyor, Supplier)

    def test_contact(self):
        self.assertIsInstance(self.Deliver.contact, Person)

    def test_bill(self):
        self.assertIsInstance(self.Deliver.bill, Bill)

    def test_(self):
        self.assertEqual(self.Deliver.__str__(), '({0},{1},{2},{3},{4},{5},{6},{7},{8})'.format(1, date, Buyer(),
                                                                                                Address, Operator(),
                                                                                                Address(), Supplier(),
                                                                                                Person(), Bill()))


if __name__ == '__main__':
    unittest.main()
