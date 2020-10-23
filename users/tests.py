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

    def test_change_username(self):
        john_green = User.objects.create_user(username="johngreen", email="johngreen@gmail.com")
        john_green.username = "john_green"
        self.assertEqual(john_green.username, "john_green")

    def test_change_email(self):
        john_green = User.objects.create_user(username = "johngreen", email = "johngreen@gmail.com")
        john_green.email = "john_green@gmail.com"
        self.assertEqual(john_green.email, "john_green@gmail.com")

    def test_choose_classes(self):
        john_green = User.objects.create_user(username="johngreen", email="johngreen@gmail.com")
        john_green.profile.course_1 = "CS2150"
        john_green.profile.course_2 = "EVSC1450"
        john_green.profile.course_3 = "ABCD1234"
        self.assertEqual(john_green.profile.course_1, "CS2150")
        self.assertEqual(john_green.profile.course_2, "EVSC1450")
        self.assertEqual(john_green.profile.course_3, "ABCD1234")

    def test_change_and_delete_classes(self):
        john_green = User.objects.create_user(username="johngreen", email="johngreen@gmail.com")
        john_green.profile.course_1 = "CS2150"
        john_green.profile.course_2 = "EVSC1450"
        john_green.profile.course_3 = "ABCD1234"
        john_green.profile.course_3 = ""
        john_green.profile.course_2 = "CS3240"
        self.assertEqual(john_green.profile.course_1, "CS2150")
        self.assertEqual(john_green.profile.course_3, "")
        self.assertEqual(john_green.profile.course_2, "CS3240")

    def test_change_year(self):
        john_green = User.objects.create_user(username="johngreen", email="johngreen@gmail.com")
        john_green.profile.year_in_school = "1st"
        john_green.profile.year_in_school = "2nd"
        self.assertEqual(john_green.profile.year_in_school, "2nd")