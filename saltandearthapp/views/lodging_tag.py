from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from saltandearthapp.models import (
    LodgingTag,
    Lodging,
    Tag
)


class LodgingTagView(ViewSet):

    def retrieve(self, request, pk):
        lodging_tag = LodgingTag.objects.get(pk=pk)
        serializer = LodgingTagSerializer(lodging_tag)
        return Response(serializer.data)

    def list(self, request):
        lodging_tag = LodgingTag.objects.all()
        serializer = LodgingTagSerializer(lodging_tag, many=True)
        return Response(serializer.data)

    def create(self, request):
        lodging = Lodging.objects.get(pk=request.data["lodging"])
        tag = Tag.objects.get(pk=request.data["tag"])

        lodging_tag = LodgingTag.objects.create(
            lodging=lodging,
            tag=tag
        )

        serializer = LodgingTagSerializer(lodging_tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        lodging_tag = LodgingTag.objects.get(pk=pk)

        lodging = Lodging.objects.get(pk=request.data["lodging"])
        tag = Tag.objects.get(pk=request.data["tag"])

        lodging_tag.lodging = lodging
        lodging_tag.tag = tag
        lodging_tag.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        lodging_tag = LodgingTag.objects.get(pk=pk)
        lodging_tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class LodgingTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = LodgingTag
        fields = (
            'lodging',
            'tag'
        )
        depth = 1