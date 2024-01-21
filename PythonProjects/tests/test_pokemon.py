import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type':'application/json,"trainer_token": "ba630b51f6c815f7004bb47f6df7539a"'}

body = {
    "trainer_token": "ba630b51f6c815f7004bb47f6df7539a",
    "email": "kris90982@yandex.ru",
    "password": "Kris909"
}

def test_get_trainers():
    """
    get trainers
    """
    response = requests.get(url = f'{URL}/trainers', json=body, headers=HEADER, timeout=10)
    assert response.status_code == 200

def test_get_trainers_id():
    """
    get trainers_id
    """
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id':'3622'},json=body, headers=HEADER, timeout=10)
    assert response.json()['trainer_name'] == 'Кристина'
