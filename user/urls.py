from django.urls import path
from user import api

urlpatterns = [
    path("",api.UserAPIView.as_view(),name="user"),
]