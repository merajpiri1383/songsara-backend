from django.urls import path 
from playlist import api

urlpatterns = [
    path('',api.PlaylistListCreateAPIView.as_view(),name="playlist-list"),
    path('<slug:slug>/',api.PlaylistDetailAPIView.as_view(),name="playlist-detail"),
]