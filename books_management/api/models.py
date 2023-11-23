from django.db import models
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
	title = models.CharField(verbose_name = 'Название', max_length = 150)
	author = models.CharField(verbose_name = 'Автор', max_length = 50)

	# Было написано год, да именно год издания а не дата издания поэтому IntegerField а не DateField.
	published_year = models.IntegerField(verbose_name = 'Год издания') 
	ISBN = models.CharField(verbose_name = 'ISBN', max_length = 17)

class UserProfile(AbstractUser):
	email = models.EmailField(verbose_name = 'E-mail', unique = True)
	date_joined = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.username