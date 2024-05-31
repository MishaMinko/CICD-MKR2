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
            expected_recipe_names = ['Recipe 3', 'Recipe 2', 'Recipe 1']
            self.assertQuerysetEqual(response.context['latest_recipes'], expected_recipe_names, transform=lambda x: x.name)

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        expected_recipe_counts = {'Category 1': 2, 'Category 2': 1}
        categories_with_counts = {category.name: category.recipe_count for category in response.context['categories']}
        for category_name, expected_count in expected_recipe_counts.items():
            self.assertEqual(categories_with_counts[category_name], expected_count)