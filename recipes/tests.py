from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        category_1 = Category.objects.create(name='Category 1')
        category_2 = Category.objects.create(name='Category 2')

        Recipe.objects.create(name='Recipe 1', category=category_1)
        Recipe.objects.create(name='Recipe 2', category=category_2)
        Recipe.objects.create(name='Recipe 3', category=category_1)

    def test_main_view(self):
            response = self.client.get(reverse('main'))
            self.assertEqual(response.status_code, 200)
            self.assertQuerysetEqual(response.context['latest_recipes'], ['<Recipe: Recipe 3>', '<Recipe: Recipe 2>', '<Recipe: Recipe 1>'])