from django.shortcuts import render, redirect
from .models import Issues, Project, Comment, Sprint
from .forms import IssueCreate, ProjectCreate, CommentCreate, SprintCreate
from django.http import HttpResponse
from django.core import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

class Projectviewset (ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectCreate
    queryset = Project.objects.all()

class Commentviewset (ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentCreate
    def get_queryset(self):
        user = self.request.user
        queryset = Comment.objects.filter(author=user)
        return queryset

    def get_comments_by_issue(self, issue_id):
        data = Comment.objects.filter(issue_id = issue_id)
        # serializer = self.get_serializer(data, many=True)
        return HttpResponse(data)


class Issueviewset (ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = IssueCreate
    queryset = Issues.objects.all()
    def get_issues_by_project(self, project_id):
        data = Issues.objects.filter(project_id = project_id)
        # serializer = self.get_serializer(data, many=True)
        return HttpResponse(data)

class Sprintviewset (ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = SprintCreate
    queryset = Sprint.objects.all()

class Issuelist(generics.ListCreateAPIView):
    queryset = Issues.objects.all()
    serializer_class = IssueCreate
    filter_backends = (DjangoFilterBackend)
    filter_fields = ('project_id', 'author','type')

