import unittest
from logic.Maritime_Vehicle import MaritimeVehicle


class TestMaritimeVehicle(unittest.TestCase):
    MaritimeVehicle = MaritimeVehicle()

    def test_instance(self):
        self.assertIsInstance(self.MaritimeVehicle, MaritimeVehicle, "Its instance.")

    def test_id_vehicle(self):
        self.assertEqual(self.MaritimeVehicle.id_vehicle, 1)

    def test_model(self):
        self.assertEqual(self.MaritimeVehicle.model, "Model of vehicle")

    def test_description(self):
        self.assertEqual(self.MaritimeVehicle.description, "Description of vehicle")

    def test_status(self):
        self.assertEqual(self.MaritimeVehicle.status, "New")

    def test_brand(self):
        self.assertEqual(self.MaritimeVehicle.brand, "Brand of vehicle")

    def test_type(self):
        self.assertEqual(self.MaritimeVehicle.type, "Vehicle type")

    def test_weight(self):
        self.assertEqual(self.MaritimeVehicle.weight, 1.0)

    def test_age(self):
        self.assertEqual(self.MaritimeVehicle.age, 0)

    def test_price(self):
        self.assertEqual(self.MaritimeVehicle.price, 1.0)

    def test_length(self):
        self.assertEqual(self.MaritimeVehicle.length, 1.0)

    def test_weight_capacity(self):
        self.assertEqual(self.MaritimeVehicle.weight_capacity, 1.0)

    def test_engine_capacity(self):
        self.assertEqual(self.MaritimeVehicle.engine_capacity, 1.0)

    def test_distance_travelled(self):
        self.assertEqual(self.MaritimeVehicle.distance_travelled, 0.0)

    def test_(self):
        self.assertEqual(self.MaritimeVehicle.__str__(),
                         '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12})'.format(
                             1, "Model of vehicle", "Description of vehicle", "New", "Brand of vehicle", "Vehicle type",
                             1.0, 0, 1.0, 1.0, 1.0, 1.0, 0.0))


if __name__ == '__main__':
    unittest.main()
