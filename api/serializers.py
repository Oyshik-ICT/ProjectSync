from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    class Meta:
        model = Project
        fields = (
            'name',
            'description',
            'owner',
            'created_at',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'date_joined',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance is not None:
            self.fields['password'].required = False

class TaskSerializer(serializers.ModelSerializer):
    assign_to = serializers.StringRelatedField()
    project= serializers.StringRelatedField()
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'status',
            'priority',
            'assign_to',
            'project',
            'created_at',
            'due_date'
        )