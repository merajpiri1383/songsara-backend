from rest_framework import serializers 
from artist.models import Artist

class ArtistSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Artist
        fields = ["id","name","slug","image","topic","description"]
    
    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True 
        return super().__init__(instance,**kwargs)