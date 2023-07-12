def contarPersonas(detections, datosVagon):
  if len(detections) <= 50:
    datosVagon["personas"] = "verde"
  elif len(detections) >= 50 and len(detections) <= 100:
    datosVagon["personas"] = "amarillo"
  elif len(detections) >= 100 and len(detections) <= 169:
    datosVagon["personas"] = "rojo"
  print(datosVagon, len(detections))
  return 