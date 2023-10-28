from django.db import models
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

# class PersonManagerInactive(models.Manager):
#     def get_queryset(self):
#         return super(PersonManagerInactive, self).get_queryset().filter(is_active=False)
    
# class PersonManagerActive(models.Manager):
#     def get_queryset(self):
#         return super(PersonManagerActive, self).get_queryset().filter(is_active=True)


# class Person(User):

#     inactive = PersonManagerInactive()  # Usage : Person.inactive.all()
#     active = PersonManagerActive()

#     @classmethod
#     def count_all(cls, status=None):             # Usage: Person.count_all()
#         return cls.objects.filter(is_active=True).count()

#     def check_active(self):
#         if self.is_active == True:     # Usage: x.check_active()
#             print("You are active")
#         else:
#             print("You are not active")


#     class Meta:
#         proxy = True
#         ordering = ('first_name',)

#     def __str__(self):
#         return self.first_name
# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         get_user_model(), related_name='profile', on_delete=models.CASCADE
#     )
#     age = models.PositiveIntegerField(null=True, blank=True)
#     nickname = models.CharField(max_length=10, null=True, blank=True)


# @receiver(post_save, sender=get_user_model())
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

class NewUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=10, null=True, blank=True)