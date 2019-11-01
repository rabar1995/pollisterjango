from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Poll
from .serializers import *
    

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

