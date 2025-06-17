from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import models


class Test(TestCase):

    def test_models_pass(self):
        model = models.objects.create(
            name=self.name,
            price=10,
            quantity=0,
        )
