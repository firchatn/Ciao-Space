from __future__ import unicode_literals
from singup.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=20)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    aboutnow = models.CharField(max_length=200)
    post_date = models.DateTimeField(
        'date published', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title


class Checkin(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    x = models.DecimalField(max_digits=20, decimal_places=16)
    y = models.DecimalField(max_digits=20, decimal_places=16)
    cheek_date = models.DateTimeField(
        'date cheek', auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.username)


class Message(models.Model):
    toUser = models.ForeignKey(User, on_delete=models.CASCADE)
    fromUser = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    msg_date = models.DateTimeField(
        'date cheek', auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.toUser)
