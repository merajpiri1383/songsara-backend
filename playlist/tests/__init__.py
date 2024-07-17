from rest_framework.test import APITestCase
from mood.models import Mood
from genre.models import Genre
from playlist.models import Playlist
from pathlib import Path
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.urls import reverse

class PlaylistTestCase(APITestCase) : 

    image_path = Path(__file__).parent.parent.parent / "static/test.jpg"

    @classmethod
    def setUpTestData(self) : 

        self.staff_user = get_user_model().objects.create(
            email = "staff_user@gmail.com",
            username = "staff-user",
            is_staff = True,
            is_active = True
        )

        self.normal_user = get_user_model().objects.create(
            email = "noramal_user@gmail.com",
            username = "normal-user",
            is_active = True
        )

        self.mood = Mood.objects.create(
            name = "mood 1"
        )
        self.genre = Genre.objects.create(
            name = "genre 1",
            text = "text 1"
        )

        self.data = {
            "name" : "playlist 2",
            "slug" : "playlist-2",
            "image" : SimpleUploadedFile(
                content = open(self.image_path,"rb").read(),
                content_type = "image/jpg",
                name = "playlist1.jpg"
            ) ,
            "moods" : self.mood.id,
            "genre" : self.genre.id
        }

        self.playlist = Playlist.objects.create(
            name = "playlist",
            genre = self.genre,
            image = SimpleUploadedFile(
                content = open(self.image_path,"rb").read(),
                content_type = "image/jpg",
                name = "playlist2.jpg"
            )
        )
        self.playlist.moods.add(self.mood)
        self.playlist.save()

        self.list_url = "/playlist/"
        self.detail_url = reverse("playlist-detail",args=[self.playlist.slug])

        return super().setUpTestData()