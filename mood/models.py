from django.db import models
from django.utils.text import slugify

class Mood(models.Model) : 
    name = models.CharField(max_length=300,unique=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    hex_color = models.SlugField(max_length=15)
    
    
    def __str__(self) : 
        return f"Mood {self.name}"
    
    def save(self,**kwargs) : 
        if not self.slug : 
            self.slug = slugify(self.name,allow_unicode=True)
        return super().save(**kwargs)