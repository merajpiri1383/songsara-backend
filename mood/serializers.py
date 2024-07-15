from rest_framework import serializers 
from mood.models import Mood

class MoodSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Mood
        fields = ["id","name","slug"]

    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True
        return super().__init__(instance,**kwargs)