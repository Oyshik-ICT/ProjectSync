from django.contrib import admin
from .models import Project, Project_Member, Task

admin.site.register(Project)
admin.site.register(Project_Member)
admin.site.register(Task)

