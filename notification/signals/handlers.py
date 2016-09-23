'''
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from .models import answer


@receiver(post_save, sender=answer)
def add_ans_count(instance, created, **kwargs):
    if created:
        instance.question.answer +=1
        instance.question.save()


@receiver(post_delete, sender=answser)
def delete_ans_count(instance, **kwargs):
    instance.question.answer -=1
    instance.question.save()
'''
