import pytest
from playlist.tests import PlaylistTestCase
from playlist.models import Playlist

class TestModel(PlaylistTestCase) : 
    
    @pytest.mark.django_db
    def test_post(self) : 
        self.client.force_authenticate(self.staff_user)
        self.client.post(self.list_url,self.data)
        assert Playlist.objects.count() == 2
    
    @pytest.mark.django_db
    def test_delete(self) : 
        self.client.force_authenticate(self.staff_user)
        self.client.delete(self.detail_url)
        assert Playlist.objects.count() == 0