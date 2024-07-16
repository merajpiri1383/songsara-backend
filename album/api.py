from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from album.models import Album
from album.serializers import AlbumSerializer
from utils.permissions import IsStaffOrReadOnly

class AlbumBase : 
    serializer_class = AlbumSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = Album.objects.all()

class AlbumListCreateAPIView(AlbumBase,ListCreateAPIView) : 
    pass

class AlbumDetailView(AlbumBase,RetrieveUpdateDestroyAPIView) : 
    lookup_field = "slug"