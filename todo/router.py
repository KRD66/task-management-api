from rest_framework import routers
from .views import TaskViewSet, RegisterView
from django.urls import path

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = router.urls + [
    path('register/', RegisterView.as_view(), name='register')
]
