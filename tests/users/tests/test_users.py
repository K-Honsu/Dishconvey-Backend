import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()

@pytest.mark.django_db
def test_user_flow(client):
    register_data = {
            'email':'money@gmail.com',
            'first_name':'forex',
            'last_name':'jamie',
            'username':'feragambo',
            'password':'emmanuella1234'
        }
    
    response = client.post('/auth/users/', register_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert 'username' in response.data
    
    # access user detail without authentication
    response = client.get('/auth/users/me', follow=True)
    assert response.data['detail'] == 'Authentication credentials were not provided.'
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    # login
    login_data = {
        'password':'emmanuella1234',
        'email':'money@gmail.com'
    }

    response = client.post('/auth/jwt/create/', login_data)
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    token = response.data['access']
    
    # access with authorization
    headers = {'Authorization': f"JWT {token}"}
    response = client.get('/auth/users/me', HTTP_AUTHORIZATION= f"JWT {token}", follow=True)
    assert response.status_code == status.HTTP_200_OK
    assert 'email' in response.data
    assert response.data['email'] == 'money@gmail.com'
    
    
     # log out
    response = client.post(reverse('logout'), HTTP_AUTHORIZATION= f"JWT {token}", follow=True)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
    # attempt to access after logoutN
    headers = {'Authorization': f"JWT {token}"}
    response = client.get('/auth/users/me', HTTP_AUTHORIZATION= f"JWT {token}", follow=True)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert 'detail' in response.data
    assert response.data['detail'] == 'Invalid Token'
    
    
   