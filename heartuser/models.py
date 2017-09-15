from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.
class HeartUser(models.Model):
    heartuser = models.OneToOneField(User)
    profile = models.OneToOneField("Profile")

    def __str__(self):
        return self.heartuser.username

class Profile(models.Model):
    RELIGIONS = (
        ('1', "Christianity"),
        ('2', "Islam"),
        ('3', "Judaism")
    )

    ETHNICITY = (
        ('1', "White"),
        ('2', "Black"),
        ('3', "Asian")
    )

    PETS = (
        ('1', "Dog"),
        ('2', "Cat"),
        ('3', "Guinea Pig")
    )
    profile_photo = models.ImageField(upload_to="profilephotos")
    profile_message = models.TextField()
    age = models.IntegerField()
    ethnicity = models.CharField(max_length=30, choices=ETHNICITY)
    religion = models.CharField(max_length=30, choices=RELIGIONS)
    location = models.CharField(max_length=30)
    pets = models.CharField(max_length=30, choices=PETS)
    kids = models.CharField(max_length=30)
    willingtorelocate = models.BooleanField()
    willingtotravel = models.BooleanField()
    opentodistrelationship = models.BooleanField()

    def __str__(self):
        return str(self.age)


class RestTest(models.Model):
    user = models.OneToOneField(User)
    file = models.FileField(upload_to='profile')