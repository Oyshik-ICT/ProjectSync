from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"users", views.UserViewset, basename="users")
router.register(r"projects", views.ProjectViewset, basename="projects")

urlpatterns = [
    path("", include(router.urls)),
    path("projects/<int:project_pk>/tasks/", views.TaskViewset.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path("projects/<int:project_pk>/tasks/<int:pk>/", views.TaskViewset.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path("tasks/<int:task_pk>/comments/", views.CommentViewset.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path("tasks/<int:task_pk>/comments/<int:pk>/", views.CommentViewset.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]