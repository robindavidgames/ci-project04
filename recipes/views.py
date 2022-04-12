from django.shortcuts import render
from django.views import generic
from .models import Recipe

class RecipeList(generic.ListView):
    """
    Use the Generic Views to create a list of recipes.
    """
    model = Recipe
    # queryset = Recipe.objects.filter(status=1).order_by(-'created_on')
    queryset = Recipe.objects.filter(status=1)
    template_name = index.html
    paginate_by = 6
