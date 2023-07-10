import unittest
from shipping import Shop

class ShopTests(unittest.TestCase):

    def test_shop_name_integer(self):
        with self.assertRaises(TypeError):
            shop = Shop(123, 5.0)

    def test_shop_name_complex(self):
        with self.assertRaises(TypeError):
            shop = Shop(3 + 2j, 5.0)

    def test_shop_name_boolean(self):
        with self.assertRaises(TypeError):
            shop = Shop(True, 5.0)

    def test_shop_package_weight_integer(self):
        with self.assertRaises(TypeError):
            shop = Shop("Test Shop", 10 + 3j)

    def test_shop_package_weight_complex(self):
        with self.assertRaises(TypeError):
            shop = Shop("Test Shop", 3 + 2j)

    def test_shop_name_string(self):
        shop = Shop("Test Shop", 5.0)
        self.assertEqual(shop.name, "Test Shop")

    def test_shop_package_weight_zero(self):
        shop = Shop("Test Shop", 0)
        self.assertEqual(shop.package_weight, 0.0)
    
    def test_shop_package_weight_string(self):
        with self.assertRaises(TypeError):
            shop = Shop("Test Shop", "5.0")

    def test_shop_package_weight_negative(self):
        with self.assertRaises(TypeError):
            shop = Shop("Test Shop", -5.0)

    def test_shop_name_empty_string(self):
        with self.assertRaises(TypeError):
            shop = Shop("", 5.0)

    def shop_test_package_weight_negative_value(self):
        with self.assertRaises(TypeError):
            shop = Shop("Shop 1", -12)

if __name__ == '__main__':
    unittest.main()
