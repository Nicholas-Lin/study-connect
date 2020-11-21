from django.test import TestCase
from users.models import Profile
from django.contrib.auth.models import User
from groups.models import Group
from social_app.models import StudentCourse
# Create your tests here.
class groupsTestCase(TestCase):
    def test_group_creation(self):
        new_user = User.objects.create_user(username="New_user", email="New_user@user.com")
        test_course = StudentCourse.objects.create(subject = "CS", catalog_number = "2150", difficulty = 2, profile = new_user.profile)
        group1 = Group.objects.create(name = "CS 2150 group", course = test_course, owner = new_user)
        self.assertIn(group1, Group.objects.all())

    def test_member_addition_and_leave(self):
        new_user = User.objects.create_user(username="New_user", email="New_user@user.com")
        test_course = StudentCourse.objects.create(subject = "CS", catalog_number = "2150", difficulty = 2, profile = new_user.profile)
        group1 = Group.objects.create(name = "CS 2150 group", course = test_course, owner = new_user)
        new_user2 = User.objects.create_user(username="New_user2", email="New_user2@user.com")
        group1.members.add(new_user2.profile)
        self.assertIn(new_user2.profile, group1.members.all())
        group1.members.remove(new_user2.profile)
        self.assertNotIn(new_user2.profile, group1.members.all())

    def test_update_description(self):
        new_user = User.objects.create_user(username="New_user", email="New_user@user.com")
        test_course = StudentCourse.objects.create(subject="CS", catalog_number="2150", difficulty=2,
                                                   profile=new_user.profile)
        group1 = Group.objects.create(name="CS 2150 group", course=test_course, owner=new_user, private = True, description = "none")
        self.assertEqual(group1.description, "none")
        group1.description = "this is the update"
        self.assertEqual(group1.description, "this is the update")

    def test_filter_for_groups(self):
        new_user = User.objects.create_user(username="New_user", email="New_user@user.com")
        test_course = StudentCourse.objects.create(subject="CS", catalog_number="2150", difficulty=2,
                                                   profile=new_user.profile)
        group1 = Group.objects.create(name="CS 2150 group", course=test_course, owner=new_user, private = True)
        filtered_group = Group.objects.filter(course = test_course)
        filtered_group2 = Group.objects.filter(private = False)
        self.assertIn(group1, filtered_group)
        self.assertNotIn(group1, filtered_group2)

    def test_edit_course(self):
        new_user = User.objects.create_user(username="New_user", email="New_user@user.com")
        test_course = StudentCourse.objects.create(subject="CS", catalog_number="2150", difficulty=2,
                                                   profile=new_user.profile)
        test_course2 = StudentCourse.objects.create(subject = "CS", catalog_number = "4102", difficulty=2000,
                                                   profile=new_user.profile)
        group1 = Group.objects.create(name="CS 2150 group", course=test_course, owner=new_user, private = True)
        group1.course = test_course2
        self.assertTrue( group1.course == test_course2)

    def test_no_parameters(self):
        new_user = User.objects.create_user(username="New_user", email="New_user@user.com")
        group1 = Group.objects.create(
            owner=new_user)
        self.assertIn(group1, Group.objects.all())

    def test_owner_change(self):
        new_user = User.objects.create_user(username="New_user", email="New_user@user.com")
        test_course = StudentCourse.objects.create(subject="CS", catalog_number="2150", difficulty=2,
                                                   profile=new_user.profile)
        new_user2 = User.objects.create_user(username="New_user2", email="New_user2@user.com")
        group1 = Group.objects.create(name="CS 2150 group", course=test_course, owner=new_user)
        group1.owner = new_user2
        self.assertEqual(group1.owner, new_user2)

    def test_large_group(self):
        new_user = User.objects.create_user(username="New_user", email="New_user@user.com")
        new_user2 = User.objects.create_user(username="New_user2", email="New_user2@user.com")
        new_user3 = User.objects.create_user(username="New_user3", email="New_user3@user.com")
        new_user4 = User.objects.create_user(username="New_user4", email="New_user4@user.com")
        new_user5 = User.objects.create_user(username="New_user5", email="New_user5@user.com")
        new_user6 = User.objects.create_user(username="New_user6", email="New_user6@user.com")
        new_user7 = User.objects.create_user(username="New_user7", email="New_user7@user.com")
        test_course = StudentCourse.objects.create(subject="CS", catalog_number="2150", difficulty=2,
                                                   profile=new_user.profile)
        group1 = Group.objects.create(name="CS 2150 group", course=test_course, owner=new_user)

        group1.members.add(new_user2.profile, new_user3.profile, new_user4.profile,
                           new_user5.profile, new_user6.profile, new_user7.profile)
        self.assertIn(new_user2.profile, group1.members.all())
        self.assertIn(new_user3.profile, group1.members.all())
        self.assertIn(new_user4.profile, group1.members.all())
        self.assertIn(new_user5.profile, group1.members.all())
        self.assertIn(new_user6.profile, group1.members.all())
        self.assertIn(new_user7.profile, group1.members.all())


    def test_change_name(self):
        new_user = User.objects.create_user(username="New_user", email="New_user@user.com")
        test_course = StudentCourse.objects.create(subject="CS", catalog_number="2150", difficulty=2,
                                                   profile=new_user.profile)
        group1 = Group.objects.create(name="CS 2150 group", course=test_course, owner=new_user)
        group1.name = "testName"
        self.assertEqual(group1.name, "testName")


    def test_group_deletion(self):
        new_user = User.objects.create_user(username="New_user", email="New_user@user.com")
        test_course = StudentCourse.objects.create(subject="CS", catalog_number="2150", difficulty=2,
                                                   profile=new_user.profile)
        group1 = Group.objects.create(name="CS 2150 group", course=test_course, owner=new_user, private = True)
        self.assertIn(group1, Group.objects.all())
        group1.delete()
        self.assertNotIn(group1, Group.objects.all())







