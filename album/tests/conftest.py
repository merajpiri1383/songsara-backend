from django.urls import reverse
import pytest
from rest_framework.test import APIClient
from album.models import Album
from artist.models import Artist
from mood.models import Mood
from django.core.files.uploadedfile import SimpleUploadedFile
from pathlib import Path
from django.contrib.auth import get_user_model

image_path = Path(__file__).parent.parent.parent / "static/test.jpg"

@pytest.fixture
def users() : 
    return {
        "staff_user" : get_user_model().objects.create(
            email = "staff_user@gmail.com",
            username = "staff-user",
            is_staff = True, 
            is_active = True
        ),
        "normal_user" : get_user_model().objects.create(
            email = "normal_user@gmail.com" , 
            username = "normal-user" , 
            is_active = True
        )
    }

artist_data = dict(
    name = "artist 1",
    slug = "artist-1",
    image = SimpleUploadedFile(
        content = open(image_path,"rb").read(),
        content_type = "image/jpg" , 
        name = "artist1.jpg"
    )
)

data_album_1 = {
    "name" : "alnum 1",
    "slug" : "album-1",
    "image" : SimpleUploadedFile(
        content = open(image_path,"rb").read(),
        content_type = "image/jpg",
        name = "album.jpg"
    )
}

data_album_2 = {
    "name" : "alnum 2",
    "slug" : "album-2",
    "image" : SimpleUploadedFile(
        content = open(image_path,"rb").read(),
        content_type = "image/jpg",
        name = "album2.jpg"
    )
}

@pytest.fixture
def album_data()  :
    artist = Artist.objects.create(**artist_data)
    data_album_1["artist"] = artist.id
    data_album_1["moods"] = Mood.objects.create(name="mood 1").id
    return data_album_1


@pytest.fixture
def urls() : 
    return {
        "album_list" : reverse("album-list")
    }

@pytest.fixture
def client() : 
    return APIClient()