from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import CommentForm, RecipeForm


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
        """
        Get the recipe and associated comments.
        """

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by(
            "-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Allow for submission of a comment.
        """

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by(
            "-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class RecipeLike(View):
    """
    Allow the user to like a recipe.
    """

    def post(self, request, slug, *args, **kwargs):
        """
        Action when user clicks on like button.
        """
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class RecipePost(View):
    def get(self, request, *args, **kwargs):
        """
        Get the post recipe form
        """

        return render(
            request,
            "new_post.html",
            {
                "recipe_form": RecipeForm()
            },
        )

    def post(self, request, *args, **kwargs):
        """
        Allow for submission of a recipe.
        """
        recipe_form = RecipeForm(data=request.POST)
        if recipe_form.is_valid():
            recipe_form.instance.author = request.user
            recipe = recipe_form.save(commit=False)
            recipe.save()
        else:
            recipe_form = RecipeForm()

        return render(
            request,
            "index.html",
            {
                "recipe_form": recipe_form,
            },
        )


class RecipeEdit(View):
    def get(self, request, slug, *args, **kwargs):
        """
        Get the post recipe form
        """
        # Some guidance from https://stackoverflow.com/questions/53075940/how-to-pre-populate-django-modelform-fields
        # get_title = request.session.get(Recipe.title)
        recipe = get_object_or_404(Recipe, slug=slug)
        get_title = "Sample title"
        get_slug = Recipe.slug
        get_content = recipe.content

        return render(
            request,
            "edit_post.html",
            {
                "recipe_form": RecipeForm(
                    initial={
                        'title': get_title,
                        'slug': get_slug,
                        'content': get_content,
                    }
                )
            },
        )

    def post(self, request, *args, **kwargs):
        """
        Allow for submission of a recipe.
        """
        recipe_form = RecipeForm(data=request.POST)
        if recipe_form.is_valid():
            recipe_form.instance.author = request.user
            recipe = recipe_form.save(commit=False)
            recipe.save()
        else:
            recipe_form = RecipeForm()

        return render(
            request,
            "index.html",
            {
                "recipe_form": recipe_form,
            },
        )
