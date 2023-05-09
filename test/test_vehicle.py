import unittest
from logic.Vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    Vehicle = Vehicle()

    def test_instance(self):
        self.assertIsInstance(self.Vehicle, Vehicle, "Its instance.")

    def test_id_vehicle(self):
        self.assertEqual(self.Vehicle.id_vehicle, 1)

    def test_model(self):
        self.assertEqual(self.Vehicle.model, "Model of vehicle")

    def test_description(self):
        self.assertEqual(self.Vehicle.description, "Description of vehicle")

    def test_brand(self):
        self.assertEqual(self.Vehicle.brand, "Brand of vehicle")

    def test_type(self):
        self.assertEqual(self.Vehicle.type, "Vehicle type")

    def test_weight(self):
        self.assertEqual(self.Vehicle.weight, 1.0)

    def test_age(self):
        self.assertEqual(self.Vehicle.age, 0)

    def test_price(self):
        self.assertEqual(self.Vehicle.price, 1.0)

    def test_status(self):
        self.assertEqual(self.Vehicle.status, "Status of vehicle")

    def test_(self):
        self.assertEqual(self.Vehicle.__str__(),
                         '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})'.format(1, "Model of vehicle",
                                                                                "Description of vehicle",
                                                                                "Brand of vehicle", "Vehicle type",
                                                                                1.0, 0, 1.0,
                                                                                "Status of vehicle"))


if __name__ == '__main__':
    unittest.main()
