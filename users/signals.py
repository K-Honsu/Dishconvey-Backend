from .models import UserAccount
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=UserAccount)
def activate_user(sender, instance, created, **kwargs):
    if created:
        instance.is_active = True
        instance.save()