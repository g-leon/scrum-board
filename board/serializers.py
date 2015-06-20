from rest_framework import serializers

from .models import Sprint, Task


class SprintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sprint
        fields = ('id', 'name', 'description', 'end',)


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'sprint', 'status', 'order',
                  'assigned', 'started', 'due', 'completed',)
