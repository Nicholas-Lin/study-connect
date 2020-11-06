from django.db import models
from django.contrib.auth.models import User
# from PIL import Image

# Create your models here.
class Profile(models.Model):

    YEAR_IN_SCHOOL_CHOICES = [
        ('1st', 'First-Year'),
        ('2nd', 'Second-Year'),
        ('3rd', 'Third-Year'),
        ('4th', 'Fourth-Year'),
        ('Other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major = models.CharField(max_length=50, blank = True)
    year_in_school = models.CharField(
        max_length=5,
        choices=YEAR_IN_SCHOOL_CHOICES,
        blank = True,
    )
    bio = models.TextField(max_length=150, blank = True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # CODE FOR PROFILE PICTURE
    # image = models.ImageField(default='default.png', upload_to='profile_pics')
    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size=(300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    