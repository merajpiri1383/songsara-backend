from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from utils.permissions import IsStaffOrReadOnly
from playlist.models import Playlist
from playlist.serializers import PlaylistSerializer

class PlaylistBase : 
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all()
    permission_classes = [IsStaffOrReadOnly]

class PlaylistListCreateAPIView(PlaylistBase,ListCreateAPIView) : 
    pass 

class PlaylistDetailAPIView(PlaylistBase,RetrieveUpdateDestroyAPIView) : 
    lookup_field = "slug"