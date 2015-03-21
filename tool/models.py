from django.db import models
from django.utils import timezone

class Item(models.Model):
	query = models.TextField(default='')
	created_date = models.DateTimeField(default=timezone.now)

	def update(self):
		self.created_date = timezone.now()

	def __str__(self):
		return self.query

class Paper(models.Model):
	query = models.TextField(default='')
	title = models.TextField()
	abstract = models.TextField()

	def __str__(self):
		return self.title
