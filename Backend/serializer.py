from rest_framework import serializers
from Backend.models import Image
from Backend.models import Result


class Serializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        #fields = ('id', 'description', 'deadline', 'done', 'priority', 'tags')

        fields = ('id', 'name', 'img64')

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'score1', 'score2', 'score3', 'img1b64', 'img2b64', 'img3b64')