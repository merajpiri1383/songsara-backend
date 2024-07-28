from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from utils.permissions import IsStaffOrReadOnly
from playlist.models import Playlist
from playlist.serializers import PlaylistSerializer
from utils.pagination import Pagination

class PlaylistBase : 
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all().order_by("-created")
    permission_classes = [IsStaffOrReadOnly]

class PlaylistListCreateAPIView(PlaylistBase,ListCreateAPIView) : 
    pagination_class = Pagination

class PlaylistDetailAPIView(PlaylistBase,RetrieveUpdateDestroyAPIView) : 
    lookup_field = "slug"