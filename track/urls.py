from django.urls import path
from track import api

urlpatterns = [
    path('',api.TrackListCreateAPIView.as_view(),name="track-list"),
    path('<slug:slug>/',api.TrackDetailView.as_view(),name="track-detail"),
]