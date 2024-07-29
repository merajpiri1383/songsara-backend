from rest_framework import serializers 
from mood.models import Mood
from album.serializers import AlbumSerializer,Album
from playlist.serializers import PlaylistSerializer,Playlist
from track.serializers import TrackSerializer,Track

class TotalSerializer(serializers.Serializer) : 

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context["track"] = TrackSerializer(instance,context=self.context).data if isinstance(instance,Track) else None 
        context["playlist"] = PlaylistSerializer(instance,context=self.context).data if isinstance(instance,Playlist) else None
        context["album"] = AlbumSerializer(instance,context=self.context).data if isinstance(instance,Album) else None
        return context

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