from utils.tests import TestBase
from django.urls import reverse
from track.models import Track
from artist.models import Artist


class TrackTestBase(TestBase) : 

    @classmethod
    def setUpTestData(self) -> None : 
        super().setUpTestData()
        self.artist = Artist.objects.create(
            name = "artist 1",
            image = self.image_1
        )

        self.data = {
            "name" : "track 1",
            "slug" : "track-1",
            "file" : self.file_1 ,
            "image" : self.image_2,
            "artist" : self.artist.id
        }

        self.track = Track.objects.create(
            name = "track 2",
            file = self.file_2,
            image = self.image_1,
            artist = self.artist
        )
        self.list_url = '/track/'
        self.detail_url = reverse("track-detail",args=[self.track.slug])