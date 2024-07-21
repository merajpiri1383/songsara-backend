from django.db import models
from django.utils.text import slugify

class Genre(models.Model) : 
    name = models.CharField(max_length=300,unique=True)
    slug = models.SlugField(null=True,blank=True,max_length=300,unique=True)
    text = models.TextField(null=True,blank=True)

    def __str__(self) : 
        return f"{self.name} ( {self.slug} )"
    
    def save(self,**kwargs) : 
        if not self.slug : 
            self.slug = slugify(self.name,allow_unicode=True)
        return super().save(**kwargs)