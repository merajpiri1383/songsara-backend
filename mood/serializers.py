from rest_framework import serializers 
from mood.models import Mood
from album.serializers import AlbumSerializer
from playlist.serializers import PlaylistSerializer
from track.serializers import TrackSerializer

class MoodSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Mood
        fields = ["id","name","slug","hex_color"]

    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True
        return super().__init__(instance,**kwargs)
    
    def to_representation(self,instance) : 
        context = super().to_representation(instance)
        context["albums"] = AlbumSerializer(instance.albums.all(),many=True,context=self.context).data
        context["playlists"] = PlaylistSerializer(instance.playlists.all(),many=True,context = self.context).data
        context["tracks"] = TrackSerializer(instance.tracks.all(),many=True,context=self.context).data
        return context