from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Status options when creating a recipe post.
STATUS = ((0, "Draft"), (1, "Published"))


# Recipe class modified from I Think Therefore I Blog tutorial.
class Recipe(models.Model):
    """
    Class for the main recipe posts.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_post"
        )
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="recipe_likes", blank=True
        )

    class Meta:
        """
        Sort in revese date order.
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """
        Return number of likes.
        """
        return self.likes.count()


# Comment class modified from I Think Therefore I Blog tutorial.
class Comment(models.Model):
    """
    Class for comments on each particular recipe.
    """
    post = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
        )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Sort in date order.
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}."


class RecipeTag(models.Model):
    """
    Class for tags that can be applied to many recipies.
    """
    tag_name = models.CharField(
        max_length=100,
        unique=True
        )
    recipes = models.ManyToManyField(
        Recipe
        )

    def __str__(self):
        return self.tag_name
