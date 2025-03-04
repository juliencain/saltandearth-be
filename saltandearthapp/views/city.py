from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from saltandearthapp.models import City


class CityView(ViewSet):
    def retrieve(self, request, pk):
        
        try:
            city = City.objects.get(pk=pk)
            serializer = SingleCitySerializer(city)
            return Response(serializer.data)
        except City.DoesNotExist:
            return Response({'message': 'City not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self,request):
        
        cities = City.objects.all()
        
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        
        try:
            
            
            city = City.objects.create(
                name=request.data["name"],
                image=request.data["image"]
            )
            serializer = CitySerializer(city)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        
        try:
            city = City.objects.get(pk=pk)
            
            city.name = request.data["name"]
            city.image = request.data["image"]
            
            city.save()
            serializer = CitySerializer(city)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except City.DoesNotExist:
            return Response({'message': 'City not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, pk):
        """Handle DELETE requests to delete a city"""
        try:
            city = City.objects.get(pk=pk)
            city.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except City.DoesNotExist:
            return Response({'message': 'City not found'}, status=status.HTTP_404_NOT_FOUND)    
        
        
        
        
# Serializers
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'image')

class SingleCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'image')
