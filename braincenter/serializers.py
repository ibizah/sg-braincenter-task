from .models import Series, SeriesType, SeriesSet, GetSeriesDetailsModel
from rest_framework import serializers

"""
2. All the models should have a Seriealizer and ViewSet based functiionalities

Seriealizers are as below for corresponding Models:
"""


class SeriesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesType
        fields = ['id', 'name', 'mnemonic']


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['id', 'name', 'series_type']


class SeriesSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesSet
        fields = ['id', 'name', 'series']


class GetSeriesDetailsSerielizer(serializers.ModelSerializer):
    class Meta:
        model = GetSeriesDetailsModel
        fields = ['series_id', 'series_name', 'series_type_name', 'series_type_mnemonic']
