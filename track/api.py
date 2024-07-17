from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from track.models import Track
from track.serializers import TrackSerializer
from utils.permissions import IsStaffOrReadOnly

class TrackBase : 
    serializer_class = TrackSerializer
    queryset = Track.objects.filter(playlist=None,album=None)
    permission_classes = [IsStaffOrReadOnly]


class TrackListCreateAPIView(TrackBase,ListCreateAPIView) : 
    pass 

class TrackDetailView(TrackBase,RetrieveUpdateDestroyAPIView) : 
    lookup_field = "slug"