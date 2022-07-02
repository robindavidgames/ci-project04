from django import forms
from .models import Comment, Recipe

# Modified from I Think Therefore I Blog

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'slug', 'content', 'featured_image', 'excerpt',)

class RecipeUpdate(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'slug', 'content', 'featured_image', 'excerpt',)
