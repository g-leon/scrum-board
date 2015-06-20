from rest_framework import serializers

from .models import Sprint, Task


class SprintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sprint
        fields = ('id', 'name', 'description', 'end',)


class TaskSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField('get_status_display')

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'sprint',
                  'status', 'status_display', 'order',
                  'assigned', 'started', 'due', 'completed',)

    def get_status_display(self, obj):
        return obj.get_status_display()
