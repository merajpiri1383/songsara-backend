from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from album.models import Album
from album.serializers import AlbumSerializer
from utils.permissions import IsStaffOrReadOnly
from utils.pagination import Pagination

class AlbumBase : 
    serializer_class = AlbumSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = Album.objects.all().order_by("-created")

class AlbumListCreateAPIView(AlbumBase,ListCreateAPIView) : 
    pagination_class = Pagination

class AlbumDetailView(AlbumBase,RetrieveUpdateDestroyAPIView) : 
    lookup_field = "slug"