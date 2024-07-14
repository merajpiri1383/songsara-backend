import pytest 
from django.contrib.auth import get_user_model 
from rest_framework.test import APIClient
from django.urls import reverse 


@pytest.fixture
def user() : 
    return get_user_model().objects.create(
        email = "test@gmail.com",
        username = "test-user" 
    )

@pytest.fixture 
def user_data() : 
    return dict(
        email = "test_user@gmail.com",
        username = "test-user-2",
        password = "password123"
    )

@pytest.fixture
def client() :
    return APIClient()

@pytest.fixture
def urls() : 
    return dict(
        register = reverse("register"),
    )