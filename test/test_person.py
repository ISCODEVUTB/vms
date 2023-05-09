import unittest
from logic.Person import Person
from logic.Address import Address


class TestPerson(unittest.TestCase):
    person = Person()

    def test_instance(self):
        self.assertIsInstance(self.person, Person, "Its instance!")

    def test_id_person(self):
        self.assertEqual(self.person.dni, 1)

    def test_name(self):
        self.assertEqual(self.person.name, "Name")

    def test_last_name(self):
        self.assertEqual(self.person.last_name, "Last name")

    def test_address(self):
        self.assertIsInstance(self.person.address, Address)

    def test_contact(self):
        self.assertEqual(self.person.contact, 0)

    def test_permission(self):
        self.assertEqual(self.person.permission, 0)

    def test__str__(self):
        self.assertEqual(self.person.__str__(), '({0}, {1}, {2}, {3}, {4}, {5})'.format(1, "Name", "Last name", 0,
                                                                                        Address(), 0))


if __name__ == '__main__':
    unittest.main()
