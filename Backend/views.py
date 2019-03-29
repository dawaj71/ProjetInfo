from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.views import APIView
from Backend.serializer import Serializer
from Backend.serializer import ResultSerializer
from rest_framework.response import Response
from rest_framework import status
import logging
import base64
from django.http import JsonResponse
from Backend.models import Image
from Backend.models import Result
from cnn.query_online import analyse_image


logger = logging.getLogger(__name__)

class ImageSearch(APIView) :
    def get(self, request, format=None):
        logger.error(request)
        image = Image.objects.all()
        serializer = Serializer(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = Serializer(data=request.data)
        if serializer.is_valid():
            image = base64.b64decode(request.data['img64'])
            analyseresult = analyse_image(image)
            img1 = analyseresult[0]
            score1 = analyseresult[1]
            img2 = analyseresult[2]
            score2 = analyseresult[3]
            img3 = analyseresult[4]
            score3 = analyseresult[5]
            print(img1, score1, img2, score2, img3, score3)
            Image = open("./dataset-retr/train"+"/"+img1, "rb")
            imageContent = Image.read()
            Image.close()
            img1b64 = base64.b64encode(imageContent)
            Image = open("./dataset-retr/train"+"/"+img2, "rb")
            imageContent = Image.read()
            Image.close()
            img2b64 = base64.b64encode(imageContent)
            Image = open("./dataset-retr/train"+"/"+img3, "rb")
            imageContent = Image.read()
            Image.close()
            img3b64 = base64.b64encode(imageContent)

            model = Result(score1=score1, score2=score2, score3=score3, img1b64=img1b64, img2b64=img2b64, img3b64=img3b64)
            model.save()
            MyResponse = JsonResponse({"Success": True, "Key": model.id}, status=status.HTTP_201_CREATED)
            #logger.error(serializer.data)
            return MyResponse
        return JsonResponse({"Success": False})

class ImageDetail(APIView) :
    def get(self, request, pk, format=None):
        try:
            image = Result.objects.get(pk=pk)

            #serializerscore1 = ResultSerializer(image.score1)
            #serializerscore2 = ResultSerializer(image.score2)
            #serializerscore3 = ResultSerializer(image.score3)
            #serializerb641 = ResultSerializer(image.img1b64)
            #serializerb642 = ResultSerializer(image.img2b64)
            #serializerb643 = ResultSerializer(image.img3b64)
            return JsonResponse({"Success": True, "Score1": image.score1, "Score2": image.score2, "Score3": image.score3, "img1b64": image.img1b64, "img2b64": image.img2b64, "img3b64": image.img3b64})
        except Image.DoesNotExist:
            return JsonResponse({"Success": False}, status=status.HTTP_400_BAD_REQUEST)
