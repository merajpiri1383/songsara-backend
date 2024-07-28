from rest_framework import serializers
from track.models import Track
from rest_framework.exceptions import ValidationError
from mutagen.mp3 import MP3
import math

def getDurationFile (path) : 
    try : 
        audio =MP3(path).info.length
        audio_duration = f"{int(audio // 60)}:{"0" + str(math.floor(audio % 60)) if math.floor(audio % 60) < 10 else math.floor(audio) % 60}"
        return audio_duration
    except : 
        return None

class TrackSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Track
        fields = ["id","name","slug","file","image","genre","playlist","artist","album",] 

    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True
        return super().__init__(instance,**kwargs)
    
    def to_representation(self,instance) : 
        context = super().to_representation(instance)
        context["created_date"] = instance.created.strftime('%Y-%M-%d')
        context["genre"] = {
            "id" : instance.genre.id ,
            "name" : instance.genre.name
        }
        context["artist"] = {
            "id" : instance.artist.id , 
            "name" : instance.artist.name
        }
        context["duration"] = getDurationFile(instance.file)
        return context
    
    def validate(self,attrs) : 
        if not attrs.get("image") and not attrs.get("playlist") and not attrs.get("album") and not self.instance : 
            raise ValidationError({"image/album/playlist" : "at least one of them is required ."})
        if attrs.get("file") and attrs.get("file").size > 20000000 and  self.instance : 
            raise ValidationError({"file" : "file size must be less than 20Mb ."})
        if attrs.get("file") and not attrs.get("file").content_type in ["audio/mpeg"] and self.instance : 
            raise ValidationError({"file":"invlid type , format file must be audio/mpeg ."})
        return super().validate(attrs)
