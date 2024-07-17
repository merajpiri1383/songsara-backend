from rest_framework import serializers
from track.models import Track
from rest_framework.exceptions import ValidationError

class TrackSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Track
        fields = ["id","name","slug","file","image","playlist","artist","album","created"]

    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True
        return super().__init__(instance,**kwargs)
    
    def validate(self,attrs) : 
        if not attrs.get("image") and not attrs.get("playlist") and not attrs.get("album") and not self.instance : 
            raise ValidationError({"image/album/playlist" : "at least one of them is required ."})
        if attrs.get("file") and attrs.get("file").size > 20000000 and  self.instance : 
            raise ValidationError({"file" : "file size must be less than 20Mb ."})
        if attrs.get("file") and not attrs.get("file").content_type in ["audio/mpeg"] and self.instance : 
            raise ValidationError({"file":"invlid type , format file must be audio/mpeg ."})
        return super().validate(attrs)
