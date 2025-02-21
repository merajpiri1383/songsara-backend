from django.db import models
from mood.models import Mood
from artist.models import Artist
from django.utils.text import slugify
from genre.models import Genre

class Album(models.Model) : 
    name = models.CharField(max_length=300,unique=True)
    slug = models.SlugField(null=True,blank=True,unique=True,max_length=300)
    image = models.ImageField(upload_to="artist/images")
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE,related_name="albums")
    moods = models.ManyToManyField(Mood,blank=True,related_name="albums")
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE,related_name="albums")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) : 
        return f'{self.name} {self.artist}'
    
    def save(self,**kwargs) : 
        if not self.slug : 
            self.slug = slugify(self.name,allow_unicode=True)
        return super().save(**kwargs)