from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_add_item(self):
        item = Menu.objects.create(title='IceCream', price=20.00, inventory=60)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream : 20.0")