from artist import api
from django.urls import path 

urlpatterns = [
    path("",api.ArtistListCreateAPIView.as_view(),name="artist-list"),
    path("<slug>/",api.ArtistDetailAPIView.as_view(),name="artist-detail"),
]