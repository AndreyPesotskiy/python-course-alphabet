from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.title

