from .models import Task
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import bleach

class TaskSerializer(serializers.ModelSerializer):
    
    def validate(self, attrs):
        
        attrs['name'] = bleach.clean(attrs['name'])
        attrs['description'] = bleach.clean(attrs['description'])
        return super().validate(attrs)
    
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date']
        extra_kwargs = {
     'name': {
     'validators': [
             UniqueValidator(
                 queryset=Task.objects.all()
             )
         ]
             }
         }