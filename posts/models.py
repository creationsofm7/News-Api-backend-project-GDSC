from django.db import models
from django.conf import settings

# Create your models here.
class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='news_covers/', null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trending_type = models.CharField(max_length=1, choices=[('N', 'New'), ('T', 'Top'), ('B', 'Best Story')], default='N')
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    bookmarked_by = models.ManyToManyField('accounts.CustomUser', related_name='bookmarked_posts')


    def __str__(self):
        return self.title

    @classmethod
    def search(cls, term):
        return cls.objects.filter(title__icontains=term)


class Comment(models.Model):
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
    @classmethod
    def search(cls, term):
        return cls.objects.filter(content__icontains=term)