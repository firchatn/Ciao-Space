from __future__ import unicode_literals
from singup.forms import usersForms
from django.db import models

class users(models.Model):
	name = models.CharField(max_length=10)
	lastname = models.CharField(max_length=10)
	username = models.CharField(max_length=10, unique=True)
	email = models.EmailField()
	password = models.CharField(max_length=10)
	selfi = models.ImageField(upload_to='upload/')
	def __str__(self):
		return self.username