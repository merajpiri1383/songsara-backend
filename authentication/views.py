from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from authentication.serializers import (RegisterSerializer,ActivateAcountSerializer,
                    LoginSerializer,ForgetPasswordSerializer,ResetPasswordSerializer)
from authentication.tasks import send_otp_to_user
from user.serializers import UserSerializer
from drf_spectacular.utils import extend_schema,OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from utils.permissions import IsOwnOrNot




class RegisterAPIView(APIView) : 
    serializer_class = RegisterSerializer


    @extend_schema(
            responses= {201 : RegisterSerializer},
            parameters=[
                OpenApiParameter(
                    name = "email",
                    required = True,
                    type= OpenApiTypes.EMAIL
                ),
                OpenApiParameter(
                    name = "username" ,
                    required = True , 
                    type= OpenApiTypes.STR , 
                ),
                OpenApiParameter(
                    name = "password" , 
                    required= True ,
                    type= OpenApiTypes.PASSWORD
                )
            ]
    )
    def post(self,request) : 
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid() :
            user = serializer.save()
            send_otp_to_user.apply_async(args=[user.id])
            return Response(serializer.data,status.HTTP_201_CREATED)
        else : 
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
        



class ActivateEmailAPIView(APIView) : 

    serializer_class = ActivateAcountSerializer

    @extend_schema(
            responses={200 : UserSerializer},
            parameters= [
                OpenApiParameter(
                    name = "email",
                    required= True,
                    type= OpenApiTypes.EMAIL,
                ),
                OpenApiParameter(
                    name = "otp",
                    required= True,
                    type= OpenApiTypes.INT
                )
            ]
    )
    def post(self,request) :
        serializer = ActivateAcountSerializer(data=request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    



class LoginAPIView(APIView) : 
    serializer_class = LoginSerializer

    @extend_schema(
            description= "username and email , one of them is required .",
            parameters=[
                OpenApiParameter(
                    name = "email",
                    required= True,
                    type= OpenApiTypes.EMAIL
                ),
                OpenApiParameter(
                    name = "username" , 
                    required = True , 
                    type = OpenApiTypes.STR , 
                ),
                OpenApiParameter(
                    name = "password",
                    required= True ,
                    type= OpenApiTypes.PASSWORD
                )
            ]
    )
    def post(self,request) :
        serialzier = LoginSerializer(data=request.data)
        if serialzier.is_valid() : 
            return Response(serialzier.data)
        else : 
            return Response(serialzier.errors,status.HTTP_400_BAD_REQUEST)

class ForgetPasswordAPIView(APIView) : 
    serializer_class = ForgetPasswordSerializer

    @extend_schema(
            parameters=[
                OpenApiParameter(
                    name="email",
                    required=True,
                    type=OpenApiTypes.EMAIL,
                ),
                OpenApiParameter(
                    name = "otp",
                    required= True,
                    type= OpenApiTypes.INT
                )
            ]
    )
    def post(self,request) : 
        serializer = ForgetPasswordSerializer(data=request.data)
        if serializer.is_valid() :
            return Response({"detail" : "email is sent ."})
        else :
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(APIView) : 
    permission_classes = [IsOwnOrNot]
    serializer_class = ResetPasswordSerializer
    
    @extend_schema(
            parameters= [
                OpenApiParameter(
                name = "email",
                required=True,
                type=OpenApiTypes.EMAIL
            ),
            OpenApiParameter(
                name="new_password",
                required=True,
                type=OpenApiTypes.PASSWORD,
            )
            ]
    )
    def post(self,request) : 
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid() : 
            user = serializer.save()
            self.check_object_permissions(request,user)
            return Response(serializer.data)
        else : 
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)