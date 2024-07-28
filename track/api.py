from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from track.models import Track
from track.serializers import TrackSerializer
from utils.permissions import IsStaffOrReadOnly
from utils.pagination import Pagination

class TrackBase : 
    serializer_class = TrackSerializer
    permission_classes = [IsStaffOrReadOnly]


class TrackListCreateAPIView(TrackBase,ListCreateAPIView) : 
    pagination_class = Pagination
    queryset = Track.objects.filter(playlist=None,album=None).order_by("-created")

class TrackDetailView(TrackBase,RetrieveUpdateDestroyAPIView) : 
    lookup_field = "slug"
    queryset = Track.objects.all()