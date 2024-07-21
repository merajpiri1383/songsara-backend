from django.db import models
from django.utils.text import slugify

class Artist(models.Model) : 
    name = models.CharField(max_length=300,unique=True)
    slug = models.SlugField(null=True,blank=True,unique=True)
    image = models.ImageField(upload_to="artist/images")
    topic = models.CharField(max_length=300,blank=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self) : 
        return str(self.name)
    
    def save(self,**kwargs) : 
        if not self.slug : 
            self.slug = slugify(self.name,allow_unicode=True)
        return super().save(**kwargs)