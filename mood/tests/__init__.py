from utils.tests import TestBase
from django.urls import reverse
from mood.models import Mood

class MoodTest(TestBase) : 
    @classmethod
    def setUpTestData(self) -> None :
        super().setUpTestData()
        self.mood = Mood.objects.create(
            name = "mood 1",
            image = self.image_1
        )
        self.data = {
            "name" : "mood 2",
            "slug" : "mood-2",
            "image" : self.image_2
        }
        self.list_url = reverse("mood-list")
        self.detail_url = reverse('mood-detail',args=[self.mood.slug])