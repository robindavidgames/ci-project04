from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe

class RecipeList(generic.ListView):
    """
    Use the Generic Views to create a list of recipes.
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):
    """
    Create a view for recipe details.
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = Recipe.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'liked': liked
            },
        )

