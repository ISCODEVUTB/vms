import unittest
from logic.Address import Address


class TestAddress(unittest.TestCase):
    address = Address()

    def test_instance(self):
        self.assertIsInstance(self.address, Address, "Its instance!")

    def test_house_number(self):
        self.assertEqual(self.address.house_number, 1)

    def test_street(self):
        self.assertEqual(self.address.street, "street")

    def test_apartment(self):
        self.assertEqual(self.address.apartment, 0)

    def test_postal_code(self):
        self.assertEqual(self.address.postal_code, "00000")

    def test_locality(self):
        self.assertEqual(self.address.locality, "locality")

    def test_department(self):
        self.assertEqual(self.address.department, "department")

    def test_country(self):
        self.assertEqual(self.address.country, "country")

    def test__str__(self):
        self.assertEqual(self.address.__str__(), '({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(1, 0, "street", "00000",
                                                                                              "locality", "department",
                                                                                              "country"))


if __name__ == '__main__':
    unittest.main()
