from django.db import models
from artist.models import Artist
from playlist.models import Playlist
from album.models import Album
from mood.models import Mood
from django.utils.text import slugify

class Track(models.Model) : 
    name = models.CharField(max_length = 300,unique=True)
    slug = models.SlugField(max_length = 300,unique=True,null=True,blank=True)
    image = models.ImageField(upload_to ="track/images",null=True,blank=True)
    album = models.ForeignKey(Album,on_delete=models.SET_NULL,related_name="tracks",null=True,blank=True)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE,related_name="tracks")
    playlist = models.ForeignKey(Playlist,on_delete=models.SET_NULL,related_name="tracks",null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    moods = models.ManyToManyField(Mood,related_name="tracks",blank=True)
    file = models.FileField(upload_to="track/files")

    def __str__(self) : 
        return f"{self.name} ({self.artist})"
    
    def save(self,**kwargs) : 
        if not self.slug : 
            self.slug = slugify(self.name,allow_unicode=True)
        return super().save(**kwargs)