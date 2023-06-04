from random import choice
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

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
        if len(rel_tasks) == 0:
            return rel_tasks
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

    def destroy(self, request, *args, **kwargs):
        player_id: models.Player = self.get_object().id
        category = request.query_params.get('category')
        if not category:
            return Response(status=status.HTTP_418_IM_A_TEAPOT, data="No category provided") 
        tasks_to_delete = models.Player.solved_tasks.through.objects.filter(player_id=player_id, task__category=category)
        count = tasks_to_delete.count()
        tasks_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data=f'Deleted results: {count}')



    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance: models.Player = self.get_object()
    #     data: dict = request.data
    #     if getattr(instance, 'score', None):
    #         data['score'] = instance.score + data['score']
    #     if getattr(instance, 'solved_tasks', None):
    #         instance.solved_tasks.add(data.get('solved_tasks')[0])
    #         instance.save()
    #     # if request.data.get('score'):
    #     #     instance.score == request.data.get('score')
    #     # if request.data.get('solved_tasks'):
    #     #     instance.solved_tasks.add(request.data)

    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)

    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}

    #     return Response(serializer.data)