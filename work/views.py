from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def home(request):
    man = {
        "name": "mehedi",
        "phone": "40920923",
        "mariied_stutus": False
    }

    return Response(man)