import IPython 
import cv2
from base64 import b64decode, b64encode
import numpy as np
import PIL
import io
import html
import time
import matplotlib.pyplot as plt
import requests

from enviarDatos import *
from contarPers import *
from capture import *
from funcionesImagenes import *

#%cd darknet

##### !make
#TENGO QUE HACER EL MAKE PARA QUE COMPILE

#DARKNET PARA PYTHON--------------------------------------------------
from darknet.darknet import *

network, class_names, class_colors = load_network("cfg/yolov4-csp.cfg", "cfg/coco.data", "yolov4-csp.weights")
width = network_width(network)
height = network_height(network)

def darknet_helper(img, width, height):
  darknet_image = make_image(width, height, 3)
  img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  img_resized = cv2.resize(img_rgb, (width, height), interpolation=cv2.INTER_LINEAR)

  img_height, img_width, _ = img.shape
  width_ratio = img_width/width
  height_ratio = img_height/height

  copy_image_from_bytes(darknet_image, img_resized.tobytes())
  detections = detect_image(network, class_names, darknet_image)
  free_image(darknet_image)
  return detections, width_ratio, height_ratio


#LO QUE LE VOY A MANDAR A AMBAR
datosVagon = {
    "personas" : "",
    "idVagon" : 5,
    "idTren" : 1
}

#FUNCION QUE CORRE CADA CIERTO TIEMPO
def correrCada1min():

  vid = cv2.VideoCapture(0)
  while(True):
    print("hola")
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  vid.release()
  cv2.destroyAllWindows()

  #contarPersonas(detections, datosVagon)
  mandarDatos(datosVagon)

  time.sleep(10)
  correrCada1min()

  return 

correrCada1min()