from django.db import models
from django.contrib.auth.models import User

class Flag(models.Model):
	country = models.CharField(max_length=100)

	def __str__(self):
		return self.country

class Color(models.Model):
	name = models.CharField(max_length=100)
	flags = models.ManyToManyField(Flag)

	def __str__(self):
		return self.name

class FavoriteFlag(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	flag = models.ForeignKey(Flag, on_delete=models.CASCADE)

class FavoriteColor(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	color = models.ForeignKey(Color, on_delete=models.CASCADE)
