import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model 
from genre.models import Genre
from rest_framework.test import APIClient

genre_data = {
    "data_1" : {
        "name" : "genre 1",
        "slug" : "genre-1",
        "text" : "text 1"
    },
    "data_2" : {
        "name" : "genre 2",
        "slug" : "genre-2",
        "text" : "text 2"
    }
}

@pytest.fixture
def data() : 
    return genre_data

@pytest.fixture
def genre() : 
    return Genre.objects.create(**genre_data["data_1"])

@pytest.fixture
def urls() : 
    return {
        "genre_list" : reverse("genre-list"),
        "genre_detail" : reverse("genre-detail",args=[genre_data["data_1"]["slug"]])
    }

@pytest.fixture
def client() : 
    return APIClient()

@pytest.fixture
def users() : 
    return {
        "staff_user" : get_user_model().objects.create(
            email = "staff_user@gmail.com",
            username = "staff-user",
            is_staff = True,
            is_active = True,
        ),
        "normal_user" : get_user_model().objects.create(
            email = "normal_user@gmail.com",
            username = "normal-user",
            is_active = True
        )
    }