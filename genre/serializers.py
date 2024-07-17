from rest_framework import serializers
from genre.models import Genre

class GenreSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Genre
        fields = ["id","name","slug","text"]
    
    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True
        return super().__init__(instance,**kwargs)
