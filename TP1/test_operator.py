import unittest
from logic.address import Address
from logic.operator import Operator
from test_person import TestPerson


class TestOperator(TestPerson):
    operator = Operator()

    def test_instance(self):
        self.assertIsInstance(self.operator, Operator, "it's a instance")

    def test_authorization(self):
        self.assertEqual(self.operator.authorization, 0)

    def test__str__(self):
        self.assertEqual(self.operator.__str__(), '({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(1, "Name", "Last name",
                                                                                               0, Address(), 0, 0))


if __name__ == '__main__':
    unittest.main()
