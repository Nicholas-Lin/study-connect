from django.test import TestCase
from users.models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def test_profile_created(self):
        new_user = User.objects.create_user(username="New_user", email="New_user@user.com")
        self.assertEqual(new_user.username, "New_user")
        self.assertEqual(new_user.email, "New_user@user.com")
        self.assertTrue(isinstance(new_user.profile, Profile))
    
