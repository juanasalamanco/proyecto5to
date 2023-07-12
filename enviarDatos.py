import requests

#falta agregar mas diccionarios de vagones y trenes

def mandarDatos(datosVagon):
  API_URL = "http://10.4.4.225:5000/IA"
  response = requests.post(API_URL, json=datosVagon)
  print(response.json())
  return


# API_URL = "http://10.4.4.225:5000/IA" #poner la ip de ambar
# datosVagon = {
#     "personas" : "red",
#     "idVagon" : 5,
#     "idTren" : 1
# }
# response = requests.post(API_URL, json=datosVagon)
# print(response.json())


