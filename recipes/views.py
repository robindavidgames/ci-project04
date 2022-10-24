from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Recipe, User, RecipeTag
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
        # This line and understanding of many-to-many relationships with
        # guidance from Tutor Support.
        tags = recipe.recipetag_set.all()
        print(tags)

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "tags": tags
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
            if recipe_form.instance.status == 1:
                messages.success(
                    request,
                    'Your recipe post was successfully published!')
            else:
                messages.success(
                    request,
                    'Your recipe post was successfully saved as a draft.')
        else:
            recipe_form = RecipeForm()
            messages.warning(request, 'Form error - the post was not created.')

        return render(
            request,
            "index.html",
            {
                "recipe_form": recipe_form,
            },
        )


# Created with help from Tutor Support.
class EditRecipe(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'edit_post.html'
    success_url = '/'


class RecipeDelete(DeleteView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'delete_post.html'
    success_url = '/'
