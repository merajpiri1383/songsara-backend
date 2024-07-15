from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('account/',include("authentication.urls")),
    path('mood/',include('mood.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
]
