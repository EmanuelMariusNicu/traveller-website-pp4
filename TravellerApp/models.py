from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from utils.constants import TAGS
from django.template.defaultfilters import slugify


STATUS = ((0, "Draft"), (1, "Published"))


class Trip(models.Model):
    """
    Model to store user-submitted trips
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    budget = models.PositiveIntegerField()
    route = models.TextField()
    accommodation = models.TextField()
    guide = models.TextField()
    additional_info = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(
        User, related_name='trip_like', blank=True)
    tags = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def list_of_tags(self):
        return self.tags.translate({ord(i): None for i in "]['"}).split(',')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Trip, self).save(*args, **kwargs)


class Comment(models.Model):
    """
    Model stores comments and links to trip via foreign key
    """
    post = models.ForeignKey(Trip, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
