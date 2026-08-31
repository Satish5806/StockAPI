from django.urls import reverse
from stocksapp.models import Stock

def test_authentication_failed(client):
    response = client.get('/api/stocks/')
    assert response.status_code == 401

def test_authentication_success(client, user):
    client.force_authenticate(user=user)
    response = client.get('/api/stocks/')
    assert response.status_code == 200

def test_registration_success(client, db):
    url = reverse('register_user')
    data = {
        "username": "newuser",
        "email": "newuser@email.com",
        "password": "securepassword123"
    }
    response = client.post(url, data)
    assert response.status_code == 201

def test_registration_fail(client, user):
    url = reverse('register_user')
    data = {
        "username": user.username,
        "email": "anotheruser@email.com",
        "password": "Password123"
    }
    response = client.post(url, data)
    assert response.status_code == 400
    assert "username" in response.data

def test_getsymbol_pass(client, user, db):
    stock = Stock.objects.create(
        symbol="NABIL",
        sector="Bank",
        name="Nabil Bank"
    )
    client.force_authenticate(user=user)
    response = client.get(f'/api/stocks/{stock.symbol}/'
    )
    assert response.status_code == 200
    assert response.data["symbol"] == "NABIL"

def test_getsymbol_fail(client, user):
    client.force_authenticate(user=user)
    response = client.get('api/stocks/INVALID/')
    assert response.status_code == 404
    