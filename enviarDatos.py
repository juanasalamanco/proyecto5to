import requests

API_URL = "http://10.4.4.225:5000/IA" #poner la ip de ambar

datosVagon = {
    "personas" : "rojo",
    "idVagon" : 5,
    "idTren" : 1
}

datosVagon1 = {
    "personas" : "amarillo",
    "idVagon" : 3,
    "idTren" : 1
}

response = requests.post(API_URL, json=datosVagon)
print(response.json())

response = requests.post(API_URL, json=datosVagon1)
print(response.json())