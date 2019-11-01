from rest_framework import serializers
from .models import *


class VoteSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Vote
        fields= "__all__"



class ChoiceSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='question_text', read_only=True)
    votes = VoteSerializer(many=True,read_only=True)
    class Meta:
        model=Choice
        fields = "__all__" 


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True,read_only=True)
    class Meta:
        model=Question
        fields = "__all__"

