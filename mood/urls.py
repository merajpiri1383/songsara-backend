from django.urls import path 
from mood import api


urlpatterns = [
    path('',api.MoodListCreateAPIView.as_view(),name="mood-list"),
    path('<slug>/',api.MoodDetailView.as_view(),name="mood-detail"),
]