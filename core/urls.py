from django.contrib import admin
from django.urls import path,include,re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('account/',include("authentication.urls")),
    path('mood/',include('mood.urls')),
    path('artist/',include('artist.urls')),
    path('album/',include('album.urls')),
    path('genre/',include('genre.urls')),
    path('playlist/',include('playlist.urls')),
    path('track/',include('track.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    re_path(r'^media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT}),
]