from utils.tests import TestBase
from django.urls import reverse
from mood.models import Mood

class MoodTest(TestBase) : 
    @classmethod
    def setUpTestData(self) -> None :
        super().setUpTestData()
        self.mood = Mood.objects.create(
            name = "mood 1",
            hex_color = "dsknfgfsd"
        )
        self.data = {
            "name" : "mood 2",
            "slug" : "mood-2",
            "hex_color" : "dsdsdff2"
        }
        self.list_url = reverse("mood-list")
        self.detail_url = reverse('mood-detail',args=[self.mood.slug])