import unittest
from logic.Air_Vehicle import AirVehicle


class TestAirVehicle(unittest.TestCase):
    AirVehicle = AirVehicle()

    def test_instance(self):
        self.assertIsInstance(self.AirVehicle, AirVehicle, "Its instance.")

    def test_id_vehicle(self):
        self.assertEqual(self.AirVehicle.id_vehicle, 1)

    def test_model(self):
        self.assertEqual(self.AirVehicle.model, "Model of vehicle")

    def test_description(self):
        self.assertEqual(self.AirVehicle.description, "Description of vehicle")

    def test_status(self):
        self.assertEqual(self.AirVehicle.status, "New")

    def test_brand(self):
        self.assertEqual(self.AirVehicle.brand, "Brand of vehicle")

    def test_type(self):
        self.assertEqual(self.AirVehicle.type, "Vehicle type")

    def test_weight(self):
        self.assertEqual(self.AirVehicle.weight, 1.0)

    def test_age(self):
        self.assertEqual(self.AirVehicle.age, 0)

    def test_price(self):
        self.assertEqual(self.AirVehicle.price, 1.0)

    def test_flight_hours(self):
        self.assertEqual(self.AirVehicle.flight_hours, 0.0)

    def test_people_capacity(self):
        self.assertEqual(self.AirVehicle.people_capacity, 1)

    def test_engine_type(self):
        self.assertEqual(self.AirVehicle.engine_type, "Engine type")

    def test_(self):
        self.assertEqual(self.AirVehicle.__str__(),
                         '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11})'.format(
                             1, "Model of vehicle", "Description of vehicle", "New", "Brand of vehicle", "Vehicle type",
                             1.0, 0, 1.0, 0.0, 1, "Engine type"))


if __name__ == '__main__':
    unittest.main()
