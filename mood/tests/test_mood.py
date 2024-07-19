import pytest
from mood.tests import MoodTest
from mood.models import Mood

class Test(MoodTest) : 
    
    @pytest.mark.django_db
    def test_get_list(self) : 
        response = self.client.get(self.list_url)
        assert response.status_code == 200
        assert response.data[0]["slug"] == self.mood.slug

    @pytest.mark.django_db
    def test_post_mood_by_normal_user(self) : 
        self.client.force_authenticate(self.normal_user)
        response = self.client.post(self.list_url,data=self.data)
        assert response.status_code == 403
    
    @pytest.mark.django_db
    def test_post_by_staff_user(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.post(self.list_url,data=self.data)
        assert response.status_code == 201
        assert Mood.objects.count() == 2
        assert response.data["slug"] == self.data["slug"]
    
    @pytest.mark.django_db
    def test_get_detail(self) : 
        response = self.client.get(self.detail_url)
        assert response.status_code == 200
        assert response.data["slug"] == self.mood.slug
    
    @pytest.mark.django_db
    def test_delete_by_normal_user(self) : 
        self.client.force_authenticate(self.normal_user)
        response = self.client.delete(self.detail_url)
        assert response.status_code == 403
    
    @pytest.mark.django_db
    def test_delete_by_staff_user(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.delete(self.detail_url)
        assert response.status_code == 204 
        assert Mood.objects.count() == 0 
    
    @pytest.mark.django_db
    def test_put(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.put(self.detail_url,{"name" : "name_edited"})
        assert response.status_code == 200