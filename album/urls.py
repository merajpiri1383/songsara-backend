from django.urls import path 
from album import api

urlpatterns = [
    path('',api.AlbumListCreateAPIView.as_view(),name="album-list"),
    path('<slug:slug>/',api.AlbumDetailView.as_view(),name="album-detail")
]