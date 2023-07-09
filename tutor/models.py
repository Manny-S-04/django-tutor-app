from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Review(models.Model):
    objects = models.Manager()
    firstname = models.CharField(max_length=50, blank=False, null=False)
    lastname = models.CharField(max_length=50, blank=False, null=False)
    stars = models.PositiveSmallIntegerField(blank=False, null=False)
    description = models.TextField(blank=True)


class CallBack(models.Model):
    objects = models.Manager()
    email = models.CharField(max_length=50, unique=True, null=False, blank=False)
    number = PhoneNumberField(unique=True, null=False, blank=False)
    message = models.TextField()