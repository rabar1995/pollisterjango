from rest_framework import serializers
from .models import *



class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Question
        fields = "__all__"



class ChoiceSerializer(serializers.ModelSerializer):
    quistion = serializers.StringRelatedField(many=True)
    class Meta:
        model=Choice
        fields = "__all__" 

