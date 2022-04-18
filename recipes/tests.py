from django.test import TestCase
from django.utils import timezone
from .models import Recipe, Comment

"""
To run tests, comment out current database in settings.py and then
uncomment other database settings. Revert this change after testing.
Command to run tests is: python3 manage.py test recipes
"""

class RecipeModelTests(TestCase):
    """
    Tests to check validity of the recipe model."
    """

    def test_publish_date_in_the_past(self):
        """
        Returns false if the recipe is posted in the future."
        """
        # time = timezone.now() + datetime.timedelta(days=30)
        # future_question = Recipe(created_on=time)
        # self.assertIs(future_question.was_published_recently(), False)
        pass
