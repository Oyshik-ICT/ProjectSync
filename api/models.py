from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name="project")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Project_Member(models.Model):
    class RoleChoice(models.TextChoices):
        ADMIN = 'Admin', 'Admin'
        MEMBER = 'Member', 'Member'

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="ProjectMember")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ProjectMember")
    role = models.CharField(max_length=10, choices=RoleChoice.choices)

    def __str__(self):
        return f"{self.user.username} in project {self.project.name}"

class Task(models.Model):
    class StatusChoice(models.TextChoices):
        TODO = 'To Do', 'To Do'
        IN_PROGRESS = 'In Progress', 'In Progress'
        DONE = 'Done', 'Done'

    class PriorityChoice(models.TextChoices):
        LOW = 'Low', 'Low'
        MEDIUM = 'Medium', 'Medium'
        HIGH = 'High', 'High'

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=StatusChoice.choices)
    priority = models.CharField(max_length=15, choices=PriorityChoice.choices)
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task", null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="Task")
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} is assigned to {self.assign_to.username}"
    
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comment")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} comment in {self.task.title}"



