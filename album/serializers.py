from rest_framework import serializers 
from album.models import Album

class AlbumSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Album
        fields = ["id","name","slug","genre","image","moods","artist","created"]

    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True 
        return super().__init__(instance,**kwargs)