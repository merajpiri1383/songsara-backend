from rest_framework import serializers 
from playlist.models import Playlist

class PlaylistSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Playlist
        fields = ["id","name","slug","image","genre","moods","created"]
    
    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True
        return super().__init__(instance,**kwargs)