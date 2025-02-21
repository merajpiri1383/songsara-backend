import pytest 
from django.contrib.auth import get_user_model

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
        "email" : user.email , 
        "otp" : user.otp ,  
    }

    response = client.post(urls.get("activate"),payload) 

    print(response.data)
    assert response.status_code == 200
    assert "access_token" in response.data
    assert "refresh_token" in response.data

@pytest.mark.django_db
def test_login(urls,client,user) : 
    
    payload = {
        "email" : user.email , 
        "password" : "password"
    }
    response = client.post(urls.get("login"),payload)

    assert response.status_code == 200 
    assert "access_token" in response.data 
    assert "refresh_token" in response.data 