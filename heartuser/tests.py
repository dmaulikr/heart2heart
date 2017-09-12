from django.test import TestCase
from django.test import Client
from django.core.files import File
from .models import HeartUser, Profile
from django.contrib.auth.models import User
# Create your tests here.

class ClientTestCase(TestCase):
    def test_heert_user(self):
        user = User.objects.create_user(username="samson", email="samson@gmail.com", password="samsonthestrong")
        photo = File(open("heartuser/property2.jpg", 'rb'))
        profile = Profile.objects.create( profile_message="", age=2, ethnicity="White", religion="Christianity", location="", pets="Dog", kids="", willingtorelocate=True, willingtotravel=False, opentodistrelationship=False)
        profile.profile_photo.save(photo.name, photo)
        HeartUser.objects.create(heartuser=user, profile=profile)
        self.assertEqual(User.objects.get(username="samson").username, user.username, "The object is not equal to samson")