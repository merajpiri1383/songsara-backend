from django.urls import path 
from authentication import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/",views.RegisterAPIView.as_view(),name="register"),
    path("activate/",views.ActivateEmailAPIView.as_view(),name="activate"),
    path("login/",views.LoginAPIView.as_view(),name="login"),
    path("forget-password/",views.ForgetPasswordAPIView.as_view(),name="forget-password"),
    path("reset-password/",views.ResetPasswordAPIView.as_view(),name="reset-password"),
    path("refresh/",TokenRefreshView.as_view(),name="refresh"),
]