import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published') #('date published') macht aus 'pub_date' 'date published'
	
	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date' # macht pub_date sortierbar
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'


class Choicex(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

"""
The code is straightforward. 
Each model is represented by a class that subclasses django.db.models.Model. 
Each model has a number of class variables, 
each of which represents a database field in the model.

Question ist der classname. Sousagen der Name einer Tabelle.
question_text ist der fieldname. Sozusagen der Name einer Spalte.

Wait a minute. <Question: Question object> is, utterly, an unhelpful representation of this object. Let’s fix that by editing the Question model (in the polls/models.py file) and adding a __str__() method to both Question and Choice:


"""