from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.views import APIView
from Backend.serializer import Serializer
from rest_framework.response import Response
from rest_framework import status
import logging
import base64
from Backend.models import Image
from cnn.query_online import analyse_image
from cnn.index import index

logger = logging.getLogger(__name__)

class ImageSearch(APIView) :
    def get(self, request, format=None):
        logger.error(request)
        #Récuperer le résultat de l'algo CNNs
        image = Image.objects.all()
        serializer = Serializer(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = Serializer(data=request.data)
        if serializer.is_valid():
            image = base64.b64decode(request.data['img64'])#.replace("\n",'')
            analyse_image(image)
            #logger.error(image)
            #Il faudrait lancer l'algo de CNN
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            #logger.error(serializer.data)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageDetail(APIView) :
    def get(self, request, pk, format=None):
        try:
            image = Image.objects.get(pk=pk)
            serializer = Serializer(image)
            return Response(serializer.data)
        except Image.DoesnotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
