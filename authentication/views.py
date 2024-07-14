from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from authentication.serializers import RegisterSerializer
from authentication.tasks import send_otp_to_user
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer

class RegisterAPIView(APIView) : 
    serializer_class = RegisterSerializer
    
    def post(self,request) : 
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid() :
            user = serializer.save()
            send_otp_to_user.apply_async(args=[user.id])
            return Response(serializer.data,status.HTTP_201_CREATED)
        else : 
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class ActivateEmailAPIView(APIView) : 
    def post(self,request) :
        if not request.data.get("id") : 
            return Response({"detail":"id field is required ."},status.HTTP_400_BAD_REQUEST)
        if not request.data.get("otp") : 
            return Response({"detail":"otp field is required ."},status.HTTP_400_BAD_REQUEST)
        try : 
            user = get_user_model().objects.get(id = request.data.get("id"))
        except : 
            return Response({"detail" : "user with this id does not exist"},status.HTTP_400_BAD_REQUEST)
        if user.otp == request.data.get("otp") : 
            user.is_active = True 
            user.save()
            serializer = UserSerializer(instance=user)
            return Response(serializer.data)
        return Response({"detail":"otp code is incorrect ."},status.HTTP_400_BAD_REQUEST)