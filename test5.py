import unittest
from main import Device, Smartphone, Laptop, Tablet, Cart


class TestDevice(unittest.TestCase):

    def setUp(self):
        self.phone = Smartphone("TestPhone", 1000, 10, 24, 6.5, 20)
        self.laptop = Laptop("TestLaptop", 2000, 5, 36, 16, 3.2)
        self.tablet = Tablet("TestTablet", 800, 8, 24, "2048x1536", 500)
        self.cart = Cart()

    # Test availability
    def test_is_available(self):
        self.assertTrue(self.phone.is_available(5))
        self.assertFalse(self.phone.is_available(20))

    # Test stock reduction
    def test_reduce_stock(self):
        self.phone.reduce_stock(2)
        self.assertEqual(self.phone.stock, 8)

    # Test discount
    def test_apply_discount(self):
        self.phone.apply_discount(10)
        self.assertEqual(self.phone.price, 900)

    # Test adding to cart
    def test_add_to_cart(self):
        self.cart.add_device(self.phone, 2)
        self.assertEqual(len(self.cart.items), 1)

    # Test checkout
    def test_checkout(self):
        self.cart.add_device(self.phone, 2)
        self.cart.checkout()
        self.assertEqual(self.phone.stock, 8)


if __name__ == '__main__':
    unittest.main()
