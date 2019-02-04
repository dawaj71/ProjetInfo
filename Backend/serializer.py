from rest_framework import serializers
from Backend.models import Image


class Serializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        #fields = ('id', 'description', 'deadline', 'done', 'priority', 'tags')
        fields = ('id','name','img64')