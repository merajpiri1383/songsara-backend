from utils.tests import TestBase
from django.urls import reverse
import pytest

class UserTest(TestBase) : 
    @classmethod
    def setUpTestData(self) -> None : 
        super().setUpTestData()
        self.user_url = reverse("user")
    
    @pytest.mark.django_db
    def test_get_user_without_authentication(self) : 
        response = self.client.get(self.user_url)
        assert response.status_code == 401
    
    @pytest.mark.django_db
    def test_get_user_with_authentication(self) : 
        self.client.force_authenticate(self.normal_user)
        response = self.client.get(self.user_url)
        assert response.status_code == 200
    