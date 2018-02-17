from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PrecipEvent, Raingage


class IndexView(TemplateView):
    """ Landing page """

    template_name = 'appclimate/templates/index.html'

class PrecipEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecipEvent
        # fields = ('id', 'year', 'month', 'precip', 'raingage')
        fields = ('id', 'year', 'month', 'precip', 'raingage_id')


class RaingageSerializer(serializers.ModelSerializer):
    # precip_events = PrecipEventSerializer(many=True, read_only=True)

    class Meta:
        model = Raingage
        # fields = ('__all__')
        # fields = ['id', 'code', 'name', 'latitude', 'longitude', 'precip_events']
        fields = ['id', 'code', 'name', 'latitude', 'longitude', ]


class RaingageApiView(APIView):
    """ Handles the serializing and rendering of the raingage data """

    def get(self, request, *args, **kwargs):
        """
        Return a list of all raingages
        """
        raingages = []
        for i, item in enumerate(Raingage.objects.all()):
            raingages.append({'id': i, 'name': item.name, 'code': item.code, 'lng': item.longitude(), 'lat': item.latitude()})

        return Response({"raingages": raingages})

class PrecipEventApiView(APIView):
    """ Handles the serializing and rendering of the precipitation data. """

    def get(self, request, *args, **kwargs):
        if 'gid' in kwargs and 'year' not in kwargs:
            gid = kwargs['gid']
            objects = PrecipEvent.objects.filter(raingage_id=gid)
            serializer = PrecipEventSerializer(objects, many=True)
            return Response(serializer.data)
        elif 'gid' in kwargs and 'year' in kwargs:
            gid = kwargs['gid']
            year = kwargs['year']
            objects = PrecipEvent.objects.filter(raingage_id=gid, year=year)
            serializer = PrecipEventSerializer(objects, many=True)
            return Response(serializer.data)
        else:
            objects = PrecipEvent.objects.all()
            serializer = PrecipEventSerializer(objects, many=True)
    
        return Response(serializer.data)