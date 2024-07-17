from genre.models import Genre
from genre.serializers import GenreSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from utils.permissions import IsStaffOrReadOnly


class GenreBase : 
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [IsStaffOrReadOnly]

class GenreListCreateAPIView(GenreBase,ListCreateAPIView) : 
    pass  

class GenreDetailView(GenreBase,RetrieveUpdateDestroyAPIView) : 
    lookup_field = "slug"