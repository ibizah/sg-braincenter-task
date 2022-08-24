from .models import Series, SeriesType, SeriesSet
from rest_framework import serializers 

"""
2. All the models should have a Seriealizer and ViewSet based functiionalities

Seriealizers are as below for corresponding viewset:
"""

class SeriesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesType
        fields = ['id', 'name', 'mnemonic']
        
        
    # def create(self, validated_data):
    #     answer, created = Series.objects.update_or_create(
    #     name=validated_data.get('name', None),
    #     defaults={'answer': validated_data.get('answer', None)})
    #     return answer

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['id', 'name', 'series_type']
        
    # def create(self, validated_data):
    #     answer, created = Series.objects.update_or_create(
    #     name = validated_data.get('name', None),
    #     series_type = validated_data.get('series_type', None),
    #     defaults = {'name': validated_data.get('series_type', None),'series_type': validated_data.get('series_type', None) })
    #     return answer
        
class SeriesSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesSet
        fields = ['id', 'name', 'series']
        

class TaskFiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesSet
        fields = ['serieses_count', 'series']
    
    