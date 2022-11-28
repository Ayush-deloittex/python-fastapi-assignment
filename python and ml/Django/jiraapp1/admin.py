from django.contrib import admin
from .models import Project, Issues, Comment, Sprint

admin.site.register(Project)
admin.site.register(Issues)
admin.site.register(Comment)
admin.site.register(Sprint)
