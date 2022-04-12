from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Creating classes taken from I Think Therefore I Blog tutorial videos.


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
