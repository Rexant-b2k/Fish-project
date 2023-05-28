from random import choice
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination

from api import serializers
from quizzles import models


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category',)

    def perform_create(self, serializer):
        category_id = self.request.data.get('category')
        category = get_object_or_404(models.Category, id=category_id)
        serializer.save(category=category)


class HintViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HintSerializer

    def get_queryset(self):
        task = get_object_or_404(
            models.Task,
            id=self.kwargs.get('task_id')
        )
        return task.hints


class RandomTaskViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        rel_tasks = models.Task.objects.filter(category=category).values_list('id')
        random_task = choice(rel_tasks)
        return models.Task.objects.filter(id__in=random_task)


