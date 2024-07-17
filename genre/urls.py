from django.urls import path
from genre import api

urlpatterns = [
    path('',api.GenreListCreateAPIView.as_view(),name="genre-list"),
    path('<slug:slug>/',api.GenreDetailView.as_view(),name="genre-detail"),
]