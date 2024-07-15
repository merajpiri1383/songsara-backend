from rest_framework import serializers 
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
import re 

regex_password = re.compile("(?=.*[a-zA-Z])(?=.*[0-9]).{8,16}")

class RegisterSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = get_user_model()
        fields = ["id","email","username","password"]
        
    def validate(self,data) :
        if not regex_password.findall(data.get("password")) : 
            raise ValidationError({"detail":"""
            password must contains of number and character and must be at leadt 8 character.
        """})
        return super().validate(data)
    
    def create(self,vd) : 
        user = get_user_model().objects.create(email=vd.get("email"),username=vd.get("username"))
        user.set_password(vd.get("password"))
        user.save()
        return user
    
class ActivateAcountSerializer(serializers.Serializer) : 
    id = serializers.UUIDField(required=True)
    otp = serializers.SlugField(required=True)

    def validate(self,data) : 
        try : 
            self.user = get_user_model().objects.get(id=data.get("id"))
        except : 
            raise ValidationError({"id" : "user with this id does not exist ."})
        return data
    
    def create(self,validated_data) : 
        print('create')
        if validated_data.get("otp") == self.user.otp : 
            self.user.is_active = True
            self.user.save()
            return self.user
        else : 
            raise ValidationError({"otp" : "otp code is incorrect ."})
    
    def to_representation(self,instance) : 
        context = super().to_representation(instance)
        del context["otp"]
        refresh_token = RefreshToken.for_user(instance)
        context["access_token"] = str(refresh_token.access_token)
        context["refresh_token"] = str(refresh_token)
        return context
    

class LoginSerializer(serializers.Serializer) :
    email = serializers.EmailField(required=False)
    username = serializers.SlugField(required=False)
    password = serializers.SlugField(required=True)

    def validate(self,data) : 
        if not data.get("email") and not data.get("username") : 
            raise ValidationError({"email/username" : "one of them is required ."})
        try : 
            if data.get("email") : 
                self.user = get_user_model().objects.get(email=data.get("email"))
            else : 
                self.user = get_user_model().objects.get(username=data.get("username"))
        except : 
            raise ValidationError({"email/username" : "user does not exist ."})
        if not self.user.check_password(data.get("password")) : 
            raise ValidationError({"password" : "password is incorrect ."})
        return data
    
    def to_representation(self,instance) : 
        context = super().to_representation(instance)
        refresh_token = RefreshToken.for_user(self.user)
        context["refresh_token"] = str(refresh_token)
        context["access_token"] = str(refresh_token.access_token)
        return context