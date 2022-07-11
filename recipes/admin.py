from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment, RecipeTag


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Modifications to the recipes admin panel.
    """

    # Prepopulate the slug field.
    prepopulated_fields = {'slug': ('title',)}

    # Create admin post filters.
    list_filter = ('created_on', 'author')

    # Add details to the list display.
    list_display = ('title', 'slug', 'author', 'status', 'created_on')

    # Add a search field.
    search_fields = ['title', 'content']

    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Modifications to the comments admin panel.
    """
    list_display = ('name', 'body', 'post', 'approved', 'created_on')
    list_filter = ('created_on', 'approved')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Allows admin to approve comments in admin panel.
        """
        queryset.update(approved=True)


admin.site.register(RecipeTag)
