from utils.permissions import IsOwnOrNot
from user.serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class UserAPIView(APIView) : 

    permission_classes = [IsAuthenticated,IsOwnOrNot]
    serializer_class = UserSerializer

    def get_object(self,request) : 
        self.result = None
        try : 
            self.user = get_user_model().objects.get(username=request.user.username)
        except : 
            self.result = Response({"detail":"user does not exist ."},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request) : 
        self.get_object(request)
        if self.result : return self.result
        self.check_object_permissions(request,self.user)
        serializer = UserSerializer(self.user)
        return Response(serializer.data)
    
    def patch(self,request) : 
        self.get_object(request)
        if self.result  : return self.result
        self.check_object_permissions(request,self.user)
        serializer = UserSerializer(data=request.data,instance=self.user)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data)
        else : 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)