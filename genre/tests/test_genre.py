import pytest
from genre.serializers import GenreSerializer
from genre.models import Genre


@pytest.mark.django_db
def test_get_list(urls,client,genre) : 
    response = client.get(urls["genre_list"])
    assert response.status_code == 200
    assert response.data[0] == GenreSerializer(genre).data


@pytest.mark.django_db
def test_post(urls,client,users,data) : 
    # post normal user 
    client.force_authenticate(users["normal_user"])
    response = client.post(urls["genre_list"])
    assert response.status_code == 403

    # post staff user 
    client.force_authenticate(users["staff_user"])
    response = client.post(urls["genre_list"],data["data_2"])
    assert response.status_code == 201 
    assert response.data["slug"] == data["data_2"]["slug"]

@pytest.mark.django_db
def test_get_detail(urls,client,genre) : 
    response = client.get(urls["genre_detail"])
    assert response.status_code == 200
    assert response.data == GenreSerializer(genre).data

@pytest.mark.django_db
def test_delete(urls,client,genre,users) : 
    # delete by normal user 
    client.force_authenticate(users["normal_user"])
    response = client.delete(urls["genre_detail"])
    assert response.status_code == 403


    # delete by staff user 
    client.force_authenticate(users["staff_user"])
    response = client.delete(urls["genre_detail"])
    assert response.status_code == 204
    assert Genre.objects.all().count() == 0


@pytest.mark.django_db
def test_put(urls,client,genre,users) : 
    client.force_authenticate(users["staff_user"])
    response = client.put(urls["genre_detail"],{"text": "text"})
    assert response.status_code == 200