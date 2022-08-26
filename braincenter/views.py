from email.policy import default
from django.http import HttpResponse, JsonResponse
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
from .serializers import SeriesTypeSerializer, SeriesSerializer

"""
2. All the models should have a Seriealizer and ViewSet based functiionalities
"""

"""
i) ViewSet based functiionalities
"""


class CreateOrUpdateSeriesView(APIView):

    def get(self, request, format=None):
        series = Series.objects.all()
        serializer = SeriesSerializer(series, many=True)
        content = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    """
    3a). POST method, with parameters of (Name, Series_type)   
    """

    def create(self, request):
        answer, created = Series.objects.update_or_create(
            name=request.data['name'], series_type=request.data['series_type'])
        default = {"name": request.data['name']}

        """
            i). If the posted record is not found on the exisiting records, insert the record
	        ii). If the posted record not on the database, create a new record 
        
        """
        if created:
            return Response(answer, status=status.HTTP_201_CREATED)

        return Response('Row already exist in data base', status=status.HTTP_208_ALREADY_REPORTED)


"""
4. Write a REST call to  get the following details:
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
4. Write a REST call to get  the following details:
	a). Series.id, Series.Name, Series_type.Name, Series_type.Mnemonic
"""


class GetSeriesDetailsView(APIView):

    def get_object(self, pk):
        try:
            return Series.objects.get(pk=pk)
        except Series.DoesNotExist:
            raise Http404

    def get(self, request):
        series = Series.objects.all()
        series_type = SeriesType.objects.all()
        series_serielizer = SeriesSerializer(series, many=True)
        series_type_serielizer = SeriesTypeSerializer(series_type, many=True)
        print(series_serielizer,series_type_serielizer )
        return Response({"data1": series_serielizer.data, "data2": series_type_serielizer.data})
        


"""
5. Write a REST call for get the following details:
    a). Count of unique Series_type from Series table, and list of series names for each Series_set
    b). parameters: Series_set.id
"""


class GetSeriesCountView(APIView):

    def get_object(self, pk):
        try:
            return Series.objects.get(pk=pk)
        except Series.DoesNotExist:
            raise Http404

    def get(self, request):
        query1 = Series.objects.filter(series_type=1)
        query2 = Series.objects.filter(series_type=2)
        query3 = Series.objects.filter(series_type=3)
        print("query==>", query1.values())
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
        print('serielizers of q1 ===> ', q1)

        return Response([{"serieses_count": len(query1), "series": arr1},
                         {"serieses_count": len(query2), "series": arr2},
                         {"serieses_count": len(query3), "series": arr3}
                         ])
