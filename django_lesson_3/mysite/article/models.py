from django.db import models
from account.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150)
    description = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.title


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=Article)
def notify_author(sender, instance, **kwargs):
    subject = 'Article Created'
    body = 'Your article created successfully!'
    send_from = settings.DEFAULT_FROM_EMAIL
    send_to = 'albert.li.das@gmail.com'
    print('email sent')
    send_mail(subject, body, send_from, [send_to])