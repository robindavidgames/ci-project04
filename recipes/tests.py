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
        User.objects.create(
            username='Robin',
            email="robin@example.com",
            password="supersecurePASS11!"
            )
        Recipe.objects.create(
            title='Test Recipe Item',
            author=User.objects.get(id=1),
            slug="sample-slug",
            content="<p>This is text <b>content</b> with HTML tags.</p>",
            featured_image="https://www.mozilla.org/media/protocol/img/logos/firefox/browser/logo-word-hor.7ff44b5b4194.svg",
            # created_on="",
            status="0"
            )

    # This test modified from https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#overview
    def test_title_label(self):
        example = Recipe.objects.get(id=1)
        field_label = example._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_slug_label(self):
        example = Recipe.objects.get(id=1)
        field_label = example._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_content_label(self):
        example = Recipe.objects.get(id=1)
        field_label = example._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_featured_image_label(self):
        # example = Recipe.objects.get(id=1)
        # field_label = example._meta.get_field('featured_image').verbose_name
        # self.assertEqual(field_label, 'featured_image')
        pass

    def test_status_label(self):
        example = Recipe.objects.get(id=1)
        field_label = example._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    # This test modified from https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#overview
    def test_title_max_length(self):
        example = Recipe.objects.get(id=1)
        max_length = example._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_slug_max_length(self):
        example = Recipe.objects.get(id=1)
        max_length = example._meta.get_field('slug').max_length
        self.assertEqual(max_length, 200)
    
    # def test_get_absolute_url(self):
    #     author = Author.objects.get(id=1)
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEqual(author.get_absolute_url(), '/catalog/author/1')

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
        self.user = User.objects.create(
            username='Robin',
            email="robin@example.com",
            password="supersecurePASS11!"
            )
        self.item = Recipe.objects.create(
            title='Test Recipe Item',
            author=self.user,
            slug="sample-slug",
            status=1,
            )

    # def tearDown(self):
    #     Clean up run after every test method.
    #     pass

    # From Hello Django
    def test_get_recipe_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # Built with assistance from Tutor Support
    def test_get_recipe_details(self):
        url = reverse('recipe_detail', kwargs={'slug': self.item.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
