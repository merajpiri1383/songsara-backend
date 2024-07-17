import pytest
from track.tests import TrackTestBase
from track.models import Track

class RouteTest(TrackTestBase) : 


    @pytest.mark.django_db
    def test_get_list(self) : 
        response = self.client.get(self.list_url)
        assert response.status_code == 200
        assert response.data[0]["slug"] == self.track.slug

    @pytest.mark.django_db
    def test_post_by_normal_user(self) :
        self.client.force_authenticate(self.normal_user)
        response = self.client.post(self.list_url,self.data) 
        assert response.status_code == 403
    
    @pytest.mark.django_db
    def test_post_by_staff_user(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.post(self.list_url,self.data)
        assert response.status_code == 201
        assert response.data["slug"] == self.data["slug"]
        assert Track.objects.count() == 2
    
    @pytest.mark.django_db
    def test_get_detail(self) : 
        response = self.client.get(self.detail_url)
        assert response.status_code == 200
        assert response.data["slug"] == self.track.slug
    
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
        assert Track.objects.count() == 0
    