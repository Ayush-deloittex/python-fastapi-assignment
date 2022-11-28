from django.conf import settings
from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title


class Issues(models.Model):
    class IssueType(models.TextChoices):
        BUG = 'BUG'
        TASK = 'TASK'
        STORY = 'STORY'
        EPIC = 'EPIC'

    class StatusType(models.TextChoices):
        OPEN = 'OPEN'
        IN_PROGRESS = 'IN PROGRESS'
        IN_REVIEW = 'IN REVIEW'
        CODE_COMPLETE = 'CODE COMPLETE'
        DONE = 'DONE'
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_id')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    issuetype = models.CharField(choices=IssueType.choices, default=IssueType.BUG, max_length=200)
    status = models.CharField(choices=StatusType.choices, default=StatusType.OPEN, max_length=200)

    


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id)+") "+self.title+"\n "


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    def __str__(self):
        return str(self.id)+") "+self.title+"\n "


class Sprint(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
