from rest_framework.serializers import ModelSerializer
from django import forms
from .models import Project, Issues, Comment, Sprint

class ProjectCreate(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class IssueCreate(ModelSerializer):
    class Meta:
        model = Issues
        fields = '__all__'

class CommentCreate(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class SprintCreate(ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'