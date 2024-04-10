from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

    

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100)
    is_journalist = models.BooleanField(default=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    karma = models.IntegerField(default=0)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    bookmarks = models.ManyToManyField('posts.NewsPost', related_name='user_bookmarks', blank=True)

    def clean(self):
            # Add your custom validation here
        if not self.first_name:
            raise ValidationError('First name is required')
        if not self.email:
            raise ValidationError('Email is required')
        if self.age and self.age < 18:
            raise ValidationError('Age must be at least 18')
        super().clean()

    def __str__(self):
        return self.email