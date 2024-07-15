import pytest
from django.urls import reverse
from mood.models import Mood
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

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

data = {
    "data_1" : {
        "name" : "mood 1",
        "slug" : "mood-1"
    },
    "data_2" : {
        "name" : "mood 2",
        "slug" : "mood-2"
    }
}

@pytest.fixture
def mood() : 
    return Mood.objects.create(
        name = data["data_1"]["name"],
        slug = data["data_1"]["slug"]
    )

@pytest.fixture
def mood_data() : 
    return data

@pytest.fixture
def urls() : 
    return dict(
        mood_list = reverse("mood-list"),
        mood_detail = reverse("mood-detail",args=[data["data_1"]["slug"]])
    )

@pytest.fixture
def client() : 
    return APIClient()