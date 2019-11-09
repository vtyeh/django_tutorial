"""
A model is the single, definitive source of truth about your data. It contains the essential 
fields and behaviors of the data you’re storing. Django follows the DRY Principle. 
The goal is to define your data model in one place and automatically derive things from it.

This includes the migrations - unlike in Ruby On Rails, for example, migrations are entirely 
derived from your models file, and are essentially just a history that Django can roll through 
to update your database schema to match your current models.

In our simple poll app, we’ll create two models: Question and Choice. A Question has a 
question and a publication date. A Choice has two fields: the text of the choice and a vote 
tally. Each Choice is associated with a Question.

This small bit of model code gives Django a lot of information. With it, Django is able to:

- Create a database schema (CREATE TABLE statements) for this app.
- Create a Python database-access API for accessing Question and Choice objects.

After adding 'polls.apps.PollsConfig' to INSTALLED_APPS:
Run >>>python manage.py makemigrations polls
This tells Django you've made some changes to your models and you'd like the changes to be 
stored as migrations.

Run >>>python manage.py sqlmigrate polls 001
This gives you a preview of what SQL Django thinks is required and what it will do.
Alternatively, you can run python manage.py check

Run >>> python manage.py migrate
This synchronizes the changes you made to your models with the schema in the database.

Migration is powerful because it lets you change your models and develop without having
to delete your database or tables and make new ones.
"""
from django.db import models
from django.utils import timezone

import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # It’s important to add __str__() methods to your models, not only for your own convenience 
    # when dealing with the interactive prompt, but also because objects’ representations are used 
    # throughout Django’s automatically-generated admin.
    def __str__(self):
        return self.question_text

    # Custom method. Checks if published date is no later than a day ago
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # ForeignKey tells Django each Choice is related to a single Question
    # Django supports many-to-one, many-to-many, and one-to-one relationships
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # default option is optional
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

