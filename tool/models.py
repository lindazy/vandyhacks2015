from django.db import models

class Item(models.Model):
	query = models.TextField(default='')
