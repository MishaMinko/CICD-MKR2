from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Category 1')
        Category.objects.create(name='Category 2')

        Recipe.objects.create(name='Recipe 1', category='Category 1')
        Recipe.objects.create(name='Recipe 2', category='Category 2')
        Recipe.objects.create(name='Recipe 3', category='Category 1')
