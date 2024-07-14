import pytest 

@pytest.mark.django_db
def test_registeration(urls,client,user_data) : 
    
    response = client.post(urls.get("register"),user_data)
    assert response.status_code == 201
    assert response.data.get("username") == user_data.get("username") 
    assert response.data.get("email") == user_data.get("email")
    assert "id" in response.data 


@pytest.mark.django_db
def test_activation(urls,client,user) : 

    payload = {
        "id" : user.id , 
        "otp" : user.otp , 
    }

    response = client.post(urls.get("activate"),payload) 

    assert response.status_code == 200
    assert response.data["email"] == user.email
    assert response.data["is_active"]