from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100)
    is_journalist = models.BooleanField(default=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
   

    def __str__(self):
        return self.email