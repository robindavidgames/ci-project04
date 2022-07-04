from django import forms
from .models import Comment, Recipe

# Modified from I Think Therefore I Blog

class CommentForm(forms.ModelForm):
    """
    Form for leaving comments on recipes.
    """
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Form for creating a recipe post.
    """
    class Meta:
        model = Recipe
        fields = ('title', 'slug', 'content', 'featured_image', 'excerpt',)


# class RecipeUpdate(forms.ModelForm):
#     """
#     Form for editing a recipe post. (currently the same, but may remove slug)
#     """
#     class Meta:
#         model = Recipe
#         fields = ('title', 'slug', 'content', 'featured_image', 'excerpt',)
