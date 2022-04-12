from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    # Prepopulate the slug field.
    prepopulated_fields = {'slug': ('title',)}

    # Create admin post filters.
    list_filter = ('created_on', 'author')

    # Add details to the list display.
    list_display = ('title', 'slug', 'author', 'created_on')

    # Add a search field.
    search_fields = ['title', 'content']

    summernote_fields = ('content')