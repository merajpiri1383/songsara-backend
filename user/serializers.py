from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = get_user_model()
        fields = ["id","email","username","joind","is_active","is_staff"]
        read_only_fields = ["id","email","joind","is_active","is_staff"]
    
    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True
        return super().__init__(instance,**kwargs)