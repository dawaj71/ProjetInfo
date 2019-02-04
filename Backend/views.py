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
            serializer.save()
            image = base64.standard_b64decode(request.data['img64'])
            #logger.error(image)
            #Il faudrait lancer l'algo de CNN
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            #logger.error(serializer.data)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageDetail(APIView) :
    def get(self, request, pk, format=None):
        Image = self.get_object(pk)
        serializer = Serializer(Image)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesnotExist:
            raise Http404
