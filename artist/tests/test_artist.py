import pytest

@pytest.mark.django_db
def test_get_list(urls,client,users,artist) :
    
    response = client.get(urls.get("artist_list"))

    assert response.status_code == 200
    assert response.data[0].get("slug") == artist.slug

@pytest.mark.django_db
def test_post(urls,client,users,data) : 
    client.force_authenticate(users.get("normal_user"))
    response_normal_user = client.post(urls.get("artist_list"))
    assert response_normal_user.status_code == 403

    client.force_authenticate(users.get("staff_user"))
    response = client.post(urls.get("artist_list"),data=data["data_2"])
    print(response.data)
    assert response.status_code == 201

@pytest.mark.django_db
def test_get_artist(urls,client,artist) :
    response = client.get(urls["artist_detail"])
    assert response.status_code == 200
    assert response.data["slug"] == artist.slug 