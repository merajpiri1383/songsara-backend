import pytest

@pytest.mark.django_db
def test_get_list(urls,client,mood) : 
    
    response = client.get(urls.get("mood_list"))

    assert response.status_code == 200
    assert response.data[0]["slug"] == mood.slug

@pytest.mark.django_db
def test_create_mood(urls,client,mood_data,users) : 

    client.force_authenticate(users.get("staff_user"))

    response = client.post(urls["mood_list"],mood_data["data_2"])

    assert response.status_code == 201 
    assert response.data.get("slug") == mood_data["data_2"]["slug"]


@pytest.mark.django_db
def test_get_mood(urls,client,mood) : 

    response = client.get(urls.get("mood_detail"))
    
    assert response.status_code == 200
    assert response.data.get("slug") == mood.slug