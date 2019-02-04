from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.views import APIView

class ImageSearche(APIView) :
    def get(self):
        print("OK")
        return 1

    def post(self):
        print("KO")
        return 1

    @csrf_exempt
    @require_POST
    def reception_image(request):
        #request.POST.get()
        emplacement_image = "local"
        return JsonResponse({"Success":True},{"Location":emplacement_image})

