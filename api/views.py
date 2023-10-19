from django.shortcuts import render
from apps.airlane.models import *
from apps.flight.models import *
from apps.plane.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from .serializer import *

class AirlaneAPIView(APIView):
    def get(self, request):
        airlane = Airlane.objects.all()
        serializer = AirlaneSerializers(airlane, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = AirlaneSerializers(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class AirlaneDetailAPiView(APIView):
    def get(self, request, pk):
        airlane = Airlane.objects.get(pk=pk)
        serializer = AirlaneSerializers(airlane)
        return Response(serializer.data,status=HTTP_200_OK)
    
    def patch(self, request, pk):
        airlane = Airlane.objects.get(pk=pk)
        serializer = AirlaneSerializers(airlane, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        airlane = Airlane.objects.get(pk=pk)
        airlane.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class PlaneAPIView(APIView):
    def get(self, request):
        plane = Plane.objects.all()
        serializer = PlaneSerializers(plane, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = PlaneSerializers(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class PlaneDetailAPiView(APIView):
    def get(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        serializer = PlaneSerializers(plane)
        return Response(serializer.data,status=HTTP_200_OK)
    
    def patch(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        serializer = PlaneSerializers(plane, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        plane.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class FlightAPIView(APIView):
    def get(self, request):
        flight = Flight.objects.all()
        serializer = FlightSerializers(flight, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = FlightSerializers(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class FlightDetailAPiView(APIView):
    def get(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        serializer = FlightSerializers(flight)
        return Response(serializer.data,status=HTTP_200_OK)
    
    def patch(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        serializer = FlightSerializers(flight, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        flight.delete()
        return Response(status=HTTP_204_NO_CONTENT)



