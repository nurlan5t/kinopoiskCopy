from django.db import models
from users.models import User


class Serial(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='serials/')
    duration = models.CharField(max_length=150)
    age_limit = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='serials')

    def get_absolute_url(self):
        return f'/'


class Cast(models.Model):
    serials = models.ManyToManyField(Serial, related_name='cast')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()


class Comment(models.Model):
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
