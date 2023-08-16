# from users.models import UserAccount
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Customer


# @receiver(post_save, sender=UserAccount)
# def create_customer_for_new_user(sender, **kwargs):
#     if kwargs['created']:
#         Customer.objects.create(user=kwargs['instance'])
        
        
from users.models import UserAccount
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer

@receiver(post_save, sender=UserAccount)
def create_customer_for_new_user(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
        instance.save()
