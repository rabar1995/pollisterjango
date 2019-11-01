from rest_framework import serializers
from .models import *



class ChoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Choice
        fields = "__all__" 


class QuestionSerializer(serializers.ModelSerializer):
    # choice_set = ChoiceSerializer(many=True,read_only=True)
    class Meta:
        model=Question
        fields = "__all__"
