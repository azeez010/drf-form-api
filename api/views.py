from django.shortcuts import render
from rest_framework.response  import Response
from rest_framework.views  import APIView
from rest_framework import status 
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import FormSerializer

# Create your views here.
class Test(APIView):
    parser_classes = (MultiPartParser,  FormParser )
    
    def post(self, request, *args, **kwargs):
        serializer = FormSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        print(serializer.errors)
        
        data = {
            "error": f'{serializer.errors}',
            "status": 400
        }
        return Response(data)