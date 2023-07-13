#ESTO FUNCIONA PERO ES HORRIBLE

import cv2
import requests
import time

def detectar_personas_en_video():
    # Carga el modelo preentrenado para la detección de personas
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Captura el video desde la cámara o un archivo de video
    video = cv2.VideoCapture(0)  # Usa 0 para la cámara predeterminada o proporciona la ruta de un archivo de video

    while True:
        # Lee un fotograma del video
        ret, frame = video.read()

        if not ret:
            break

        # Realiza la detección de personas en el fotograma actual
        cajas, _ = hog.detectMultiScale(frame)

        # Obtiene el número de personas detectadas en el fotograma actual
        numero_personas = len(cajas)

        # Dibuja rectángulos alrededor de las personas detectadas
        for (x, y, w, h) in cajas:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Muestra el fotograma con las personas detectadas y el número de personas
        cv2.putText(frame, f"Número de personas: {numero_personas}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Detección de personas en videostream", frame)

        # Detiene el bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) == ord('q'):
            break

    # Libera los recursos
    video.release()
    cv2.destroyAllWindows()

    # Realiza una solicitud POST al servidor local
    datosVagon = {
    "personas" : numero_personas,
    "idVagon" : 5,
    "idTren" : 1
    }
    API_URL = "http://10.4.4.225:5000/IA"
    response = requests.post(API_URL, json=datosVagon)
    print(response.json())

    if response.status_code == 200:
        print("Solicitud POST enviada con éxito.")
    else:
        print("Error al enviar la solicitud POST.")

# Ejecuta el código cada minuto
while True:
    detectar_personas_en_video()
    time.sleep(60)

