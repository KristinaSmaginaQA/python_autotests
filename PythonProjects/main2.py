""""
pokemon sozdanie
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type':'application/json', "trainer_token": "ba630b51f6c815f7004bb47f6df7539a"}

#body = {
#    "name": "Питон",
#    "photo": "https://dolnikov.ru/pokemons/albums/005.png"
#}

#body1 ={
#    "pokemon_id": "28165",
#    "name": "Ирина Петровна",
#    "photo": "https://dolnikov.ru/pokemons/albums/007.png"
#}

body2={
    "pokemon_id": "28165"
}

#response = requests.post(url=f'{URL}//pokemons',json=body,headers=HEADER,timeout=5)
#print(f'Статус код: {response.status_code}.Сообщение: {response.json()["message"]}')

#response = requests.put(url=f'{URL}//pokemons',json=body1,headers=HEADER,timeout=5)
#print(f'Статус код: {response.status_code}.Сообщение: {response.json()["message"]}')

response = requests.post(url=f'{URL}//trainers/add_pokeball',json=body2,headers=HEADER,timeout=5)
print(f'Статус код: {response.status_code}.Сообщение: {response.json()["message"]}')

