from django.urls import path 
from authentication import views

urlpatterns = [
    path("register/",views.RegisterAPIView.as_view(),name="register"),
    path("activate/",views.ActivateEmailAPIView.as_view(),name="activate"),
    path("login/",views.LoginAPIView.as_view(),name="login"),
]