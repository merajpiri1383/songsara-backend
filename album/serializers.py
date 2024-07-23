from rest_framework import serializers 
from album.models import Album
from track.serializers import TrackSerializer 

class AlbumSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Album
        fields = ["id","name","slug","genre","image","moods","artist"]

    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True 
        return super().__init__(instance,**kwargs)
    
    def to_representation(self,instance) : 
        moods = []
        for mood in instance.moods.all() : 
            moods.append({"name" : mood.name, "id" : mood.id})
        context = super().to_representation(instance)
        context["genre"] = {
            "id" : instance.genre.id,
            "name" : instance.genre.name
        }
        context["artist"] = {
            "id" : instance.artist.id , 
            "name" : instance.artist.name
        }
        context["tracks"] = TrackSerializer(instance.tracks.all(),many=True,context=self.context).data
        context["moods"] = moods
        context["created_date"] = instance.created.strftime("%Y-%M-%d")
        return context