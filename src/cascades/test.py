import numpy as np
import cv2



import urllib.request
import time
URL = "http://192.168.43.199:8080/shot.jpg"
while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    cv2.imshow('IPWebcam',img)
    
    cv2.waitKey(1)

