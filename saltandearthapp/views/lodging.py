from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from saltandearthapp.models import City, Lodging, User

class LodgingView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for a single lodging"""
        try:
            lodging = Lodging.objects.get(pk=pk)
            serializer = SingleLodgingSerializer(lodging)
            return Response(serializer.data)
        except Lodging.DoesNotExist:
            return Response({'message': 'Lodging not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for all lodgings"""
        city_id = request.query_params.get('city', None)
        uid = request.query_params.get('uid', None) 
        lodging = Lodging.objects.all()
        
        if city_id:
            lodging = lodging.filter(city_id=city_id)
            
        if uid:
            lodging = lodging.filter(uid=uid)
            
        serializer = LodgingSerializer(lodging, many=True)
        return Response(serializer.data)    

    def create(self, request):
        """Handle POST requests to create a new lodging"""
        try:
            # Fetch related models
            user = User.objects.get(pk=request.data["user_id"])
            city = City.objects.get(pk=request.data["city_id"])

            # Create the Lodging instance
            lodging = Lodging.objects.create(  # Corrected to Lodging.objects.create
                uid=request.data["uid"],
                user_id=user,
                city_id=city,
                name=request.data["name"],
                address=request.data["address"],
                description=request.data["description"],
                image=request.data["image"],
                link=request.data["link"],
            )
            
            # Serialize the created lodging instance and return the response
            serializer = LodgingSerializer(lodging)
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
        """Handle PUT requests to update an existing lodging"""
        try:
            lodging = Lodging.objects.get(pk=pk)
            city = City.objects.get(pk=request.data["city_id"])

            # Update fields
            lodging.uid = request.data["uid"]
            lodging.city = city
            lodging.name = request.data["name"]
            lodging.address = request.data["address"]
            lodging.description = request.data["description"]
            lodging.image = request.data["image"]
            lodging.link = request.data["link"]
            
            lodging.save()
            serializer = LodgingSerializer(lodging)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Lodging.DoesNotExist:
            return Response({'message': 'Lodging not found'}, status=status.HTTP_404_NOT_FOUND)
        except City.DoesNotExist:
            return Response({'message': 'City not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        """Handle DELETE requests to delete a lodging"""
        try:
            lodging = Lodging.objects.get(pk=pk)
            lodging.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Lodging.DoesNotExist:
            return Response({'message': 'Lodging not found'}, status=status.HTTP_404_NOT_FOUND)


# Serializers

class LodgingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lodging
        fields = ('id', 'uid', 'user_id', 'city_id', 'name', 'address', 'description', 'image', 'link')


class SingleLodgingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lodging
        fields = ('id', 'uid', 'user_id', 'city_id', 'name', 'address', 'description', 'image', 'link')
