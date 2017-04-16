from __future__ import unicode_literals
from singup.models import users
from django.db import models

class post(models.Model):
	title = models.CharField(max_length=20)
	username = models.ForeignKey(users, on_delete=models.CASCADE)
	aboutnow = models.CharField(max_length=200)
	post_date = models.DateTimeField('date published', auto_now_add=True, auto_now=False)
	def __str__(self):
		return self.title

class cheekin(models.Model):
	username = models.ForeignKey(users, on_delete=models.CASCADE)
	x = models.DecimalField(max_digits=20, decimal_places=16)
	y = models.DecimalField(max_digits=20, decimal_places=16)
	cheek_date = models.DateTimeField('date cheek', auto_now_add=True, auto_now=False)
	def __str__(self):
		return str(self.username)