from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from adaptor.model import CsvDbModel
import datetime

from django.db import models
from django.db.models import IntegerField, FloatField, CharField

@python_2_unicode_compatible
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	"""Next 3 lines add attributes to the admin representation of this method"""
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

datetime.timedelta(days=1)

@python_2_unicode_compatible
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

@python_2_unicode_compatible
class Major(models.Model):
	major_code = IntegerField(primary_key=True)
	major = CharField(max_length=100)
	major_category = CharField(max_length=100)
	total = IntegerField()
	employed = IntegerField()
	employed_full_time_year_round = IntegerField()
	unemployed = IntegerField()
	unemployment_rate = FloatField()
	median = IntegerField()
	p25th= IntegerField()
	p75th = IntegerField()
	def __str__(self):
		return self.major



