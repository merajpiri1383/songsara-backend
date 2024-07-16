import pytest

@pytest.mark.django_db
def test_get(urls,client) : 
    response = client.get(urls["album_list"])
    assert response.status_code == 200

@pytest.mark.django_db
def test_post(urls,client,album_data,users) :
    client.force_authenticate(users.get("normal_user"))
    response = client.post(urls["album_list"])
    assert response.status_code == 403

    client.force_authenticate(users.get("staff_user"))
    response = client.post(urls["album_list"],album_data)
    print(response.data)
    assert response.status_code == 201
    assert response.data["slug"] == album_data["slug"]