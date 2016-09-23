from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Notification(models.Model):
    title = models.CharField(max_length=256)
    message = models.TextField()
    attach = models.FileField(upload_to = "notifications_files/%Y.%m.%d", blank = True,null = True)
    viewed = models.BooleanField(default=False)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def created_welcome_message(sender, **kwargs):
    if kwargs.get('created', False):

        Notification.objects.create(user=kwargs.get('instance'),
                      title = "welcome to your new world",
                        message = "Thanks for registring")








