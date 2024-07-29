from rest_framework import serializers
from .models import DynamicModel

class DynamicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicModel
        fields = '__all__'
