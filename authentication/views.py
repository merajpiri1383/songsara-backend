from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from authentication.serializers import RegisterSerializer
from authentication.tasks import send_otp_to_user
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema,OpenApiParameter
from drf_spectacular.types import OpenApiTypes




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

    serializer_class = UserSerializer

    @extend_schema(
            responses={200 : UserSerializer},
            parameters= [
                OpenApiParameter(
                    name = "id",
                    required= True,
                    type= OpenApiTypes.UUID,
                ),
                OpenApiParameter(
                    name = "otp",
                    required= True,
                    type= OpenApiTypes.INT
                )
            ]
    )
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
    



class LoginAPIView(APIView) : 
    serializer_class = UserSerializer

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
        if not request.data.get("email") and not request.data.get("username")  :
            return Response({"detail":"email or user name is required"},status.HTTP_400_BAD_REQUEST)
        if not request.data.get("password"): 
            return Response({"detail":"password is required"},status.HTTP_400_BAD_REQUEST)
        
        try : 
            if request.data.get("email") : 
                user = get_user_model().objects.get(email=request.data.get("email"))
            else : 
                user = get_user_model().objects.get(username=request.data.get("username"))
        except : 
            return Response({"detail":"user with this username / email does not exist ."},
                    status.HTTP_400_BAD_REQUEST)
        
        if not user.is_active : 
            return Response({"detail":"user is not active ."},status.HTTP_400_BAD_REQUEST)
        
        if not user.check_password(request.data.get("password")) : 
            return Response({"detail":"incorrect password ."},status.HTTP_400_BAD_REQUEST)
        
        refresh_token = RefreshToken.for_user(user)
        data = UserSerializer(user).data
        data["refresh_token"] = str(refresh_token)
        data["access_token"] = str(refresh_token.access_token)
        return Response(data)