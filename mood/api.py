from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from mood.models import Mood
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from mood.serializers import MoodSerializer 
from utils.permissions import IsStaffOrReadOnly

# mood 
class MoodBase : 
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = MoodSerializer
    queryset = Mood.objects.all() 

class MoodListCreateAPIView(MoodBase,ListCreateAPIView) : 
    pass 

class MoodDetailView(MoodBase,RetrieveUpdateDestroyAPIView) : 
    lookup_field = "slug"