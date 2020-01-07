from rest_framework import serializers
from .models import employees

class employeesSerializer(Serializers.ModelSerializer):

    class Meta:
        fields=('firstname','lastname')
        fields= '__all__'