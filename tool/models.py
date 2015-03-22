from django.db import models
from django.utils import timezone
import ast

class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

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
	mesh = ListField(default=[])

	def __str__(self):
		return self.title

class Mesh(models.Model):
	term = models.TextField()
	category = models.TextField()
