from rest_framework import serializers 
from playlist.models import Playlist
from mood import MiniMoodSerializer
from track.serializers import TrackSerializer

class PlaylistSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Playlist
        fields = ["id","name","slug","image","genre","moods"]
    
    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True
        return super().__init__(instance,**kwargs)
    
    def to_representation(self,instance) : 
        context = super().to_representation(instance)
        context["genre"] = {"id" : instance.genre.id , "name" : instance.genre.name}
        context["moods"] = MiniMoodSerializer(instance.moods.all(),many=True).data
        context["created_date"] = instance.created.strftime("%Y-%M-%d")
        context["tracks"] = TrackSerializer(instance.tracks.all(),many=True,context=self.context).data
        return context