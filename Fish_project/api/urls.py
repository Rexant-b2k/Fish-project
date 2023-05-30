from django.urls import include, path
from rest_framework import routers

from api.views import CategoryViewSet, PlayerViewSet, RandomTaskViewSet, TaskViewSet, HintViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'tasks/(?P<task_id>\d+)/hints', HintViewSet, 'hints')
router.register(r'categories', CategoryViewSet, 'categories')
router.register(r'tasks', TaskViewSet, 'tasks')
router.register(r'randomtask', RandomTaskViewSet, 'randomtask')
router.register(r'player', PlayerViewSet, 'players')

urlpatterns = [
    path('', include(router.urls)),
]
