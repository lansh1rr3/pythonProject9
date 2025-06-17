from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Product, Category

CustomUser = get_user_model()

class ProductTests(TestCase):
    def setUp(self):
        self.account = CustomUser.objects.create_user(
            username='sampleuser',
            password='samplepass456'
        )
        self.product_group = Category.objects.create(
            name='Sample Category'
        )
        
    def test_product_creation(self):
        item = Product.objects.create(
            name='Sample Item',
            price=15.50,
            quantity=10,
            category=self.product_group,
            seller=self.account
        )
        self.assertEqual(item.name, 'Sample Item')
        self.assertEqual(item.price, 15.50)
        self.assertEqual(item.quantity, 10)
        
    def test_invalid_quantity(self):
        with self.assertRaises(ValidationError):
            Product.objects.create(
                name='Invalid Item',
                price=20.00,
                quantity=-5,
                category=self.product_group,
                seller=self.account
            )
