from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    bio = models.TextField(default='here is my bio')
    picture = models.ImageField(upload_to = 'users_prof_img/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs.get('created', False):
        UserProfile.objects.get_or_create(user=kwargs.get('instance'))




class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length = 60)
    stat_province = models.CharField(max_length = 30)
    country = models.CharField(max_length=50)
    web_site = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    sex = models.CharField(max_length=1, choices=(('M','male'),('F','female')),default='F')
    email = models.EmailField(blank=True, verbose_name='e-mail')
    def __str__(self):
        return u'%s %s' %(self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=50)
    descrp = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publicatin_date = models.DateField(blank=True, null=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title


    def get_absolute_url(self):

        return reverse("books:detail", kwargs={"id": self.id})
        # documentation return reverse('books.views.book_detail', args=[str(self.id)])


class likes(models.Model):
    likes_num = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    liked_on = models.DateTimeField(auto_now_add=True)
    



