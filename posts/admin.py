from django.contrib import admin

# Register your models here.
from .models import NewsPost, Comment

admin.site.register(NewsPost)
admin.site.register(Comment)
