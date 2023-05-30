from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from quizzles import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ('id', 'text')


class TaskSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='text', read_only=True)

    class Meta:
        model = models.Task
        fields = ('id', 'header', 'text', 'image', 'category', 'topic', 'add_date', 'answer')


class HintSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Hint
        fields = ('id', 'task', 'level', 'text')


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Player
        fields = ('id', 'player_id', 'score', 'solved_tasks')
        read_only_fields = ('id', 'player_id')