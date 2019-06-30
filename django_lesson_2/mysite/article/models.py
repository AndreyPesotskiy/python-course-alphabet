from django.db import models
from account.models import Profile


class Article(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.title

