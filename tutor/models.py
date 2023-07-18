from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Review(models.Model):
    objects = models.Manager()
    firstname = models.CharField(max_length=50, blank=False, null=False)
    lastname = models.CharField(max_length=50, blank=False, null=False)
    stars = models.PositiveSmallIntegerField(blank=False, null=False)
    description = models.TextField(blank=True)
    
    def as_json(self):
        return dict(
            review_id=self.id, review_firstname=self.firstname,
            review_lastname=self.lastname, 
            review_stars=self.stars,
            review_description=self.description)


class CallBack(models.Model):
    objects = models.Manager()
    email = models.CharField(max_length=50, unique=True, null=False, blank=False)
    number = PhoneNumberField(unique=True, null=False, blank=False)
    message = models.TextField()