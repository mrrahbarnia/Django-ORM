from django.dispatch import receiver
from django.db.models.signals import post_save
from ecommerce.inventory.models import Brand

@receiver(post_save, sender=Brand)
def hello_world(sender, instance, created, **kwargs):
    print(instance)
    print(created)