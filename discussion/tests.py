from django.test import TestCase
from discussion.models import Post
from users.models import Profile
from social_app.models import StudentCourse
from django.contrib.auth.models import User

# Create your tests here.
class DiscussionTestCase(TestCase):
    def setUp(self):
        new_user = User.objects.create_user(username="New_user", email="New_user@user.com")
        new_post = Post.objects.create(title="the title", content="This is my first post right here", author=new_user)

    def test_post_created(self):
        new_user2 = User.objects.create_user(username="New_user2", email="New_user2@user.com")
        new_post = Post.objects.create(title="the title", content="This is my first post right here", author=new_user2)
        self.assertEqual(new_post.title, "the title")
        self.assertEqual(new_post.content, "This is my first post right here")

    def test_change_Post_title(self):
        john_green = User.objects.create_user(username="johngreen", email="johngreen@gmail.com")
        new_post = Post.objects.create(title="the title", content="This is my first post right here", author=john_green)
        new_post.title = "Changed Title"
        self.assertEqual(new_post.title, "Changed Title")

    def test_change_Post_content(self):
        john_green = User.objects.create_user(username="johngreen", email="johngreen@gmail.com")
        new_post = Post.objects.create(title="the title", content="This is my first post right here", author=john_green)
        new_post.content = "new Content here"
        self.assertEqual(new_post.content, "new Content here")

    def test_add_course(self):
        john_green = User.objects.create_user(username = "johngreen", email = "johngreen@gmail.com")
        newCourse = StudentCourse.objects.create(subject="CS", catalog_number = "2150" , difficulty = 3, profile = john_green.profile)
        new_post = Post.objects.create(title="the title", content="This is my first post right here", author=john_green)
        new_post.course = newCourse
        self.assertEqual(new_post.course, newCourse)

    def test_change_author(self):
        john_green = User.objects.create_user(username="johngreen", email="johngreen@gmail.com")
        new_user2 = User.objects.create_user(username="New_user2", email="New_user2@user.com")
        new_post = Post.objects.create(title="the title", content="This is my first post right here", author=john_green)
        new_post.author = john_green
        self.assertEqual(new_post.author, john_green)