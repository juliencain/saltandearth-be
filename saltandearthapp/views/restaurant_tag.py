from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from saltandearthapp.models import RestaurantTag, Restaurant, Tag
from django.shortcuts import get_object_or_404

class RestaurantTagView(ViewSet):

    def retrieve(self, request, pk):
        restaurant_tag = get_object_or_404(RestaurantTag, pk=pk)
        serializer = RestaurantTagSerializer(restaurant_tag)
        return Response(serializer.data)

    def list(self, request):
        restaurant_tags = RestaurantTag.objects.all()
        serializer = RestaurantTagSerializer(restaurant_tags, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            restaurant = Restaurant.objects.get(pk=request.data["restaurant"])
            tag = Tag.objects.get(pk=request.data["tag"])
        except Restaurant.DoesNotExist:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Tag.DoesNotExist:
            return Response({"error": "Tag not found"}, status=status.HTTP_400_BAD_REQUEST)

        restaurant_tag = RestaurantTag.objects.create(
            restaurant=restaurant,
            tag=tag
        )

        serializer = RestaurantTagSerializer(restaurant_tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        restaurant_tag = get_object_or_404(RestaurantTag, pk=pk)

        try:
            restaurant = Restaurant.objects.get(pk=request.data["restaurant"])
            tag = Tag.objects.get(pk=request.data["tag"])
        except Restaurant.DoesNotExist:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Tag.DoesNotExist:
            return Response({"error": "Tag not found"}, status=status.HTTP_400_BAD_REQUEST)

        restaurant_tag.restaurant = restaurant
        restaurant_tag.tag = tag
        restaurant_tag.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        restaurant_tag = get_object_or_404(RestaurantTag, pk=pk)
        restaurant_tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class RestaurantTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTag
        fields = ('restaurant', 'tag')
        depth = 1 
