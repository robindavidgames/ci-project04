from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Recipe, Comment

# To run tests, comment out current database in settings.py and then
# uncomment other database settings. Revert this change after testing.
# Command to run tests is: python3 manage.py test recipes


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
            featured_image="https://www.mozilla.org/media/protocol/img/logos/firefox/browser/logo-word-hor.7ff44b5b4194.svg", # noqa
            status="0"
            )

    # This test modified from
    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#overview # noqa
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

    def test_status_label(self):
        example = Recipe.objects.get(id=1)
        field_label = example._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    # This test modified from
    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#overview # noqa
    def test_title_max_length(self):
        example = Recipe.objects.get(id=1)
        max_length = example._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_slug_max_length(self):
        example = Recipe.objects.get(id=1)
        max_length = example._meta.get_field('slug').max_length
        self.assertEqual(max_length, 200)


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
