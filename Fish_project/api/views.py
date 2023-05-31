from random import choice
from django.db.models import ManyToManyRel
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.response import Response
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
        player = self.request.query_params.get('player_id')
        rel_tasks = models.Task.objects.filter(category=category).exclude(players__player_id=player).values_list('id')
        random_task = choice(rel_tasks)
        return models.Task.objects.filter(id__in=random_task)


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('player_id',)

    def partial_update(self, request, *args, **kwargs):
        player: models.Player = self.get_object()
        data: dict = request.data
        if data.get('score'):
            player.score += data.get('score')
        if data.get('solved_tasks'):
            player.solved_tasks.add(data.get('solved_tasks')[0])
        player.save()
        serializer = serializers.PlayerSerializer(player, data=request.data, partial=True)
        serializer.is_valid()
        return Response(serializer.data)