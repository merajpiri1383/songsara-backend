import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from artist.models import Artist
from django.core.files.uploadedfile import SimpleUploadedFile
from pathlib import Path


image_path = Path(__file__).parent.parent.parent / "static/test.jpg"

@pytest.fixture
def users() : 
    return dict(
        staff_user = get_user_model().objects.create(
            email = "staff_user@gmail.com",
            username = "staff-user",
            is_active = True,
            is_staff = True
        ),
        normal_user = get_user_model().objects.create(
            email = "normal_user@gmail.com",
            username = "normal-user",
            is_active = True
        )
    ) 

@pytest.fixture
def client() : 
    return APIClient()

data_artist = {
    "data_1" : {
        "name" : "artist 1",
        "image" : SimpleUploadedFile(
            content= open(image_path,"rb").read() ,
            name="artist-1.jpg",
            content_type="image/jpg"
        ),
        "slug" : "artist-1"
    },
    "data_2" : {
        "name" : "artist 2",
        "image" : SimpleUploadedFile(
            content= open(image_path,"rb").read(),
            name = "artist-2.jpg",
            content_type="image/jpg"
        ),
        "slug" : "artist-2"
    }
}

@pytest.fixture
def data() : 
    return data_artist

@pytest.fixture
def artist() : 
    return Artist.objects.create(**data_artist["data_1"])

@pytest.fixture
def urls() : 
    return dict(
        artist_list = reverse("artist-list"),
        artist_detail = reverse("artist-detail",args=[data_artist["data_1"]["slug"]])
    )