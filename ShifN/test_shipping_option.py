import unittest
from shipping import Carrier, ShippingOption, Shop

class TestShippingOption(unittest.TestCase):
    def test_shipping_option_initialization(self):
        shipping_option = ShippingOption("Carrier 1", "Country 1")
        self.assertEqual(shipping_option.name, "Carrier 1")
        self.assertEqual(shipping_option.country, "Country 1")

    def test_get_shipping_cost_standard(self):
        shipping_option = ShippingOption("Carrier 1", "Country 1")
        shipping_option.shipping_method = "standard"
        shipping_cost = shipping_option.get_shipping_cost(3.5)
        self.assertEqual(shipping_cost, 1.75)

    def test_get_shipping_cost_express(self):
        shipping_option = ShippingOption("Carrier 1", "Country 1")
        shipping_option.shipping_method = "express"
        shipping_cost = shipping_option.get_shipping_cost(3.5)
        self.assertEqual(shipping_cost, 3.5)

    def test_get_shipping_cost_with_zero_weight(self):
        shipping_option = ShippingOption("Carrier 1", "Country 1")
        shipping_option.shipping_method = "standard"
        shipping_cost = shipping_option.get_shipping_cost(0)
        self.assertEqual(shipping_cost, 0)

if __name__ == '__main__':
    unittest.main()
