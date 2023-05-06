import unittest
from logic.Payment_Method import PaymentMethod


class TestPaymentMethod(unittest.TestCase):
    PaymentMethod = PaymentMethod()

    def test_instance(self):
        self.assertIsInstance(self.PaymentMethod, PaymentMethod, "It's a instance")

    def test_payment_method(self):
        self.assertEqual(self.PaymentMethod.payment_method, "payment method")

    def test_(self):
        self.assertEqual(self.PaymentMethod.__str__(), '({0})'.format("payment method"))


if __name__ == '__main__':
    unittest.main()
