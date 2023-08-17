from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Menu.objects.create(title="Dish1", price=15, inventory=500)
        Menu.objects.create(title="Dish2", price=25, inventory=50)
        Menu.objects.create(title="Dish3", price=150, inventory=5)

    def test_getall(self):
        response = self.client.get("/restaurant/menu-items")
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response, serializer.data)

    def test_getone(self):
        item = Menu.objects.create(title="Pizza", price=25.00, inventory=50)
        response = self.client.get(f"/restaurant/menu-items/{item.id}")
        serializer = MenuSerializer(item, many=False)
        self.assertEqual(response.data, serializer.data)		