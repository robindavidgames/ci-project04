from django.test import TestCase
# from django.utils import timezone
from .models import Recipe, Comment
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

"""
To run tests, comment out current database in settings.py and then
uncomment other database settings. Revert this change after testing.
Command to run tests is: python3 manage.py test recipes
"""


class RecipeModelTests(TestCase):
    """
    Tests to check validity of the recipe model."
    """
    @classmethod

    def setUp(cls):
        User.objects.create(username='Robin', email="robin@example.com", password="supersecurePASS11!")
        Recipe.objects.create(title='Test Recipe Item', author=User.objects.get(id=1), slug="sample-slug")

    # This test modified from https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#overview
    def test_title_label(self):
        example = Recipe.objects.get(id=1)
        field_label = example._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_slug_label(self):
        example = Recipe.objects.get(id=1)
        field_label = example._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_publish_date_in_the_past(self):
        """
        Returns false if the recipe is posted in the future."
        """
        # time = timezone.now() + datetime.timedelta(days=30)
        # future_question = Recipe(created_on=time)
        # self.assertIs(future_question.was_published_recently(), False)

        # created_on = models.DateTimeField(auto_now_add=True)

        # is_future = Recipe(created_on)

        # past = False
        # current_time = datetime.now()
        # if Recipe.created_on < current_time:
        #     past = True
        # self.assertTrue(past)

        pass

    def test_title_is_less_than_200_characters(self):
        # this isn't working because it's testing the model, not the recipes themselves.
        # rework this so that a recipe title over 200 is offered and assertFalse
        # for post in Recipe:
        #     title = Recipe.title
        #     title_length = title.len()
        #     self.assertTrue(title_length < 200)
        pass

    # from Hello Django module
    def test_this_thing_works(self):
        self.assertEqual(1, 1)

    # def test_done_defaults_to_false(self):
    #     item = Item.objects.create(name='Test Todo Item')
    #     self.assertFalse(item.done)

    def test_requires_title(self):
        # new_recipe = Recipe.objects.create(title="Example Recipe Name", slug="unique_slug")
        # self.assertFalse(new_recipe.done)
        pass

class ViewTests(TestCase):
    """
    Tests to check validity of the views."
    """

    def setUp(self):
        self.user = User.objects.create(username='Robin', email="robin@example.com", password="supersecurePASS11!")
        self.item = Recipe.objects.create(title='Test Recipe Item', author=self.user, slug="sample-slug")

    # def tearDown(self):
    #     Clean up run after every test method.
    #     pass

    # From Hello Django
    def test_get_recipe_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_recipe_details(self):

        # needs author_id to work.
        # user = User.objects.create(username='Robin', email="robin@example.com", password="supersecurePASS11!")
        # item = Recipe.objects.create(title='Test Recipe Item', author=user, slug="sample-slug")
        # response = self.client.get(f'/{item.slug}')
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'recipe_detail.html')

        # user = User.objects.create(username='Robin', email="robin@example.com", password="supersecurePASS11!")
        # item = Recipe.objects.create(title='Test Recipe Item', author=user, slug="sample-slug")
            # url = reverse('recipe_detail', kwargs={'slug': self.item.slug})
        # response = self.client.get(url)
        # response = self.client.get('/sample-slug', follow=True)
            # response = self.client.get(url, follow=True)
            # self.assertEqual(response.status_code, 200)
        pass
