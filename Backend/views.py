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

logger = logging.getLogger(__name__)

class ImageSearch(APIView) :
    def get(self, request, format=None):
        #todos = Todo.objects.all()
        logger.error(request)
        #Récuperer le résultat de l'algo CNN
        serializer = Serializer(data=request.data, many=True)
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

    @csrf_exempt
    @require_POST
    def reception_image(request):
        #request.POST.get()
        emplacement_image = "local"
        return JsonResponse({"Success":True},{"Location":emplacement_image})

