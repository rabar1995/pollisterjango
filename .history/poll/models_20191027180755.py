from django.db import models
from django.contrib.auth.models import User

class Vote(models.Model):
    votes = models.IntegerField(default=0)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes=models.ManyToManyField(Vote)
    

    def __str__(self):
        return self.choice_text


        