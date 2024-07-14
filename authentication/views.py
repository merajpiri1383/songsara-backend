from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from authentication.serializers import RegisterSerializer


class RegisterAPIView(APIView) : 
    serializer_class = RegisterSerializer
    
    def post(self,request) : 
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else : 
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)