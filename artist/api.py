from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from artist.serializers import ArtistSerializer
from artist.models import Artist
from utils.permissions import IsStaffOrReadOnly

class ArtistBase : 
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

class ArtistListCreateAPIView(ArtistBase,ListCreateAPIView) : 
    pass 


class ArtistDetailAPIView(ArtistBase,RetrieveUpdateDestroyAPIView) : 
    lookup_field = "slug"