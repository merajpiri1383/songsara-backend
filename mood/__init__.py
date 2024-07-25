from rest_framework import serializers

class MiniMoodSerializer (serializers.Serializer) : 
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only = True)
    slug = serializers.SlugField(read_only=True)