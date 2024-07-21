from utils.tests import TestBase
from django.urls import reverse
from genre.models import Genre
from artist.models import Artist
from album.models import Album


class AlbumTest(TestBase) : 
    @classmethod
    def setUpTestData(self) -> None : 
        super().setUpTestData()
        self.genre = Genre.objects.create(name = "genre 1")
        self.artist = Artist.objects.create(name="artist 1",image=self.image_1)
        self.album = Album.objects.create(
            name = "album 1",
            image = self.image_1,
            genre = self.genre,
            artist = self.artist
        )
        self.data = {
            "name" : "album 2",
            "image" : self.image_2,
            "genre" :  self.genre.id ,
            "artist" : self.artist.id ,
            "slug" :"album-2"
        }
        self.list_url = reverse("album-list")
        self.detail_url = reverse("album-detail",args=[self.album.slug])