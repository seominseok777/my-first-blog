from django import forms
from django.db import models
from django.utils import timezone
# Create your models here.


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력하세요.')

class Post(models.Model):
    title = models.CharField(max_length=200, validators=[min_length_3_validator])
    author = models.CharField(max_length=20, blank=True)
    user_agent = models.TextField(max_length=200)
    content = models.TextField(max_length=1000)
    tags = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)
    test_field = models.IntegerField(default=10)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

#class Hitcount(models.Model):
