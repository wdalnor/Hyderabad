from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

#from django.utils.encoding import python_2_compatible



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pup_date = models.DateTimeField('date puplished')


    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)



class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    question = models.ForeignKey(Question)
    selected_choice = models.ForeignKey(Choice)
    user = models.ForeignKey(User)

    def __str__(self):

        return self.user.username

    class Meta:
        unique_together = (
            ('question', 'user'),
            )