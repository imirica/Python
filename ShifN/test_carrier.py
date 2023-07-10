import unittest
from shipping import Carrier, ShippingOption, Shop

class TestCarrier(unittest.TestCase):
    def test_carrier_initialization(self):
        carrier = Carrier("Carrier 1", "Country 1")
        self.assertEqual(carrier.name, "Carrier 1")
        self.assertEqual(carrier.country, "Country 1")

    def test_connect_to_shop(self):
        shop = Shop("Shop 1", 3.5)
        carrier = Carrier("Carrier 1", "Country 1")
        shipping_option = carrier.connect_to_shop(shop)
        self.assertIsInstance(shipping_option, ShippingOption)
        self.assertEqual(shipping_option.name, "Carrier 1")
        self.assertEqual(shipping_option.country, "Country 1")

    def test_connect_to_shop_with_invalid_shop(self):
        shop = "Shop 1"  # Invalid shop object
        carrier = Carrier("Carrier 1", "Country 1")
        with self.assertRaises(TypeError):
            carrier.connect_to_shop(shop)

    def test_get_shipping_cost_standard(self):
        shop = Shop("Shop 1", 3.5)
        carrier = Carrier("Carrier 1", "Country 1")
        shipping_option = carrier.connect_to_shop(shop)
        shipping_option.shipping_method = "standard"
        shipping_cost = shipping_option.get_shipping_cost(shop.package_weight)
        self.assertEqual(shipping_cost, 1.75)

if __name__ == '__main__':
    unittest.main()
