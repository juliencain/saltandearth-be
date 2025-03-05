from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from saltandearthapp.models import City, Restaurant, User

class RestaurantView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for a single restaurant"""
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            serializer = SingleRestaurantSerializer(restaurant)
            return Response(serializer.data)
        except Restaurant.DoesNotExist:
            return Response({'message': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for all restaurants"""
        city_id = request.query_params.get('city', None)
        uid = request.query_params.get('uid', None)
        restaurant = Restaurant.objects.all()
        
        if city_id:
            restaurant = restaurant.filter(city_id=city_id)
            
        if uid:
            restaurant = restaurant.filter(uid=uid)
            
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests to create a new restaurant"""
        try:
            # Fetch related models
            user = User.objects.get(pk=request.data["user_id"])
            city = City.objects.get(pk=request.data["city_id"])

            # Create the Restaurant instance
            restaurant = Restaurant.objects.create(
                uid=request.data["uid"],
                user_id=user,
                city_id=city,
                name=request.data["name"],
                address=request.data["address"],
                description=request.data["description"],
                image=request.data["image"],
                link=request.data["link"],
            )
            
            # Serialize the created restaurant instance and return the response
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except City.DoesNotExist:
            return Response({"error": "City not found"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError as e:
            return Response({"error": f"Missing field: {e.args[0]}"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """Handle PUT requests to update an existing restaurant"""
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            city = City.objects.get(pk=request.data["city_id"])

            # Update fields
            restaurant.uid = request.data["uid"]
            restaurant.city = city
            restaurant.name = request.data["name"]
            restaurant.address = request.data["address"]
            restaurant.description = request.data["description"]
            restaurant.image = request.data["image"]
            restaurant.link = request.data["link"]
            
            restaurant.save()
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Restaurant.DoesNotExist:
            return Response({'message': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
        except City.DoesNotExist:
            return Response({'message': 'City not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        """Handle DELETE requests to delete a restaurant"""
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            restaurant.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Restaurant.DoesNotExist:
            return Response({'message': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)


# Serializers

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'uid', 'user_id', 'city_id', 'name', 'address', 'description', 'image', 'link')


class SingleRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'uid', 'user_id', 'city_id', 'name', 'address', 'description', 'image', 'link')
