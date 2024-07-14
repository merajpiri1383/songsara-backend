from rest_framework import serializers 
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
import re 

regex_password = re.compile("(?=.*[a-zA-Z])(?=.*[0-9]).{8,16}")

class RegisterSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = get_user_model()
        fields = ["id","email","username","password"]
        
    def validate(self,data) :
        if not regex_password.findall(data.get("password")) : 
            raise ValidationError({"detail":"password must contains of number and character and must be at leadt 8 character."})
        return super().validate(data)
    
    def create(self,vd) : 
        user = get_user_model().objects.create(email=vd.get("email"),username=vd.get("username"))
        user.set_password(vd.get("password"))
        user.save()
        return user
