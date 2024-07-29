from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from mood.models import Mood
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from mood.serializers import MoodSerializer 
from utils.permissions import IsStaffOrReadOnly
from django.core.paginator import Paginator
from mood.serializers import TotalSerializer

# mood 
class MoodBase : 
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = MoodSerializer
    queryset = Mood.objects.all() 

class MoodListCreateAPIView(MoodBase,ListCreateAPIView) : 
    pass 

class MoodDetailView(MoodBase,RetrieveUpdateDestroyAPIView) : 
    lookup_field = "slug"

class MoodTrackAPIView(APIView) : 
    permission_classes = [IsStaffOrReadOnly]
    
    def get(self,request, slug) : 
        try : 
            mood = Mood.objects.get(slug=slug)
        except : 
            return Response({"detail":"mood with this slug does not exist ."},status=status.HTTP_400_BAD_REQUEST)
        objects = [*mood.tracks.all()] + [*mood.playlists.all()] + [*mood.albums.all()]
        paginator = Paginator(objects,per_page=20)
        return Response({
            "results" : TotalSerializer(paginator.get_page(request.GET.get("page",1)),context = {"request":request} , many=True).data ,
            "pages" : paginator.num_pages,
        })