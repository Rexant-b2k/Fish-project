from django.urls import include, path
from rest_framework import routers

from api.views import CategoryViewSet, TaskViewSet, HintViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'tasks/(?P<task_id>\d+)/hints', HintViewSet, 'hints')
router.register(r'categories', CategoryViewSet, 'categories')
router.register(r'tasks', TaskViewSet, 'tasks')
# router.register(r'hints', HintViewSet, 'hints')

urlpatterns = [
    path('', include(router.urls)),
]