from email.policy import default
from urllib import request
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from .models import Series, SeriesSet, SeriesType
from .serializers import SeriesTypeSerializer, SeriesSerializer, TaskFiveSerializer

"""
2. All the models should have a Seriealizer and ViewSet based functiionalities
"""
class SeriesListView(APIView):

    def get(self, request, format=None):
        series = Series.objects.all()
        serializer = SeriesSerializer(series, many=True)
        content = JSONRenderer().render(serializer.data)
        return Response(serializer.data)
    
    """
    3a). POST method, with parameters of (Name, Series_type)   
    """
    def post(self, request ):
        answer, created = Series.objects.update_or_create(
        name  = request.data['name'], series_type  = request.data['series_type'])
        default = { "name" : request.data['name'] }
        
        #     i). If the posted record is not found on the exisiting records, insert the record
	    #     ii). If the posted record not on the database, create a new record 
     
        if created :
            return Response(answer, status=status.HTTP_201_CREATED)
        
        return Response('Row already exist in data base', status = status.HTTP_208_ALREADY_REPORTED)

"""
4. Write a REST call for allget the following details:
	a). Series.id, Series.Name, Series_type.Name, Series_type.Mnemonic
"""
class SeriesDetailView(APIView):

    def get_object(self, pk):
        try:
            return Series.objects.get(pk=pk)
        except Series.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        series = self.get_object(pk)
        serializer = SeriesSerializer(series)
        return Response(serializer.data)
    
"""
4. Write a REST call for allget the following details:
	a). Series.id, Series.Name, Series_type.Name, Series_type.Mnemonic
"""
class TaskFourListView(APIView):
    
    def get_object(self, pk):
        try:
            return Series.objects.get(pk=pk)
        except Series.DoesNotExist:
            raise Http404

    def get(self, request):
        series = Series.objects.all().values()
        series_type = SeriesType.objects.all().values()
        
        pubs = Series.objects.select_related('series_type')
        print("pubs  ====>", pubs)
        series = serializers.serialize("json", pubs)
        series_type = serializers.serialize("json", SeriesType.objects.all(), fields = ("name", "mnemonic"))
        # serielizers = [serializer1.data, serializer2.data]
        print("series  ====>", series)
        print("series_type  ====>", series_type)
        return Response(series)
    
"""
5. Write a REST call for get the following details:
    a). Count of unique Series_type from Series table, and list of series names for each Series_set
    b). parameters: Series_set.id
"""
class TaskFiveListView(APIView):
    
    def get_object(self, pk):
        try:
            return Series.objects.get(pk=pk)
        except Series.DoesNotExist:
            raise Http404

    def get(self, request):
        query1 = Series.objects.filter(series_type=1)
        query2 = Series.objects.filter(series_type=2)
        query3 = Series.objects.filter(series_type=3)
        print("query==>",query1.values())
        arr1 = []
        arr2 = []
        arr3 = []
        for i in query1.values():
            arr1.append(i["name"])
            
        for i in query2.values():
            arr2.append(i["name"])
            
        for i in query2.values():
            arr3.append(i["name"])   
              
        q1 = serializers.serialize("json", query1)
        q2 = serializers.serialize("json", query2)
        q3 = serializers.serialize("json", query3)
       
       
        return Response([{"serieses_count": len(query1), "series":arr1},
                         {"serieses_count": len(query2), "series":arr2},
                         {"serieses_count": len(query3), "series":arr3}
                         ])
