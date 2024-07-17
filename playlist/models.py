from django.db import models
from mood.models import Mood
from genre.models import Genre
from django.utils.text import slugify

class Playlist (models.Model) : 
    
    name = models.CharField(max_length=300 , unique=True)
    slug = models.SlugField(max_length=300 , unique= True,null=True,blank=True)
    image = models.ImageField(upload_to="playlist/images")
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE,related_name="playlists")
    moods = models.ManyToManyField(Mood,related_name="playlists")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) : 
        return f"{self.name} ({self.genre})"
    
    def save(self,**kwargs) : 
        if not self.slug : 
            self.slug = slugify(self.name,allow_unicode=True)
        return super().save(**kwargs)