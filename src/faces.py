import urllib.request
import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')

URL = "http://192.168.43.1:8080/shot.jpg"
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(r"C:\\Users\\Shree\\Desktop\\face\\OpenCV-Python-Series-master\\src\\recognizers\\face-trainner.yml")

labels = {"person_name": 1}
with open(r"C:\\Users\\Shree\\Desktop\\face\\OpenCV-Python-Series-master\\src\\pickles\\face-labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}
print(labels)
# cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    # ret, frame = cap.read()
	img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
	img = cv2.imdecode(img_arr,-1)
	gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	for (x, y, w, h) in faces:
    	#print(x,y,w,h)
		roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
		roi_color = img[y:y+h, x:x+w]

    	# recognize? deep learned model predict keras tensorflow pytorch scikit learn
		id_, conf = recognizer.predict(roi_gray)
		# print(conf)
		if conf>=45 and conf <= 85:
			print("Id is:",id_)
			print("labels[id_]:",labels[id_])
			font = cv2.FONT_HERSHEY_SIMPLEX
			name = labels[id_]
			print("Name is:",name)
			color = (255, 255, 255)
			stroke = 2
			cv2.putText(img, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
			
		img_item = "7.png"
		cv2.imwrite(img_item, roi_color)
		
		color = (255, 0, 0) #BGR 0-255 
		stroke = 2
		end_cord_x = x + w
		end_cord_y = y + h
		cv2.rectangle(img, (x, y), (end_cord_x, end_cord_y), color, stroke)
		
		# subitems = smile_cascade.detectMultiScale(roi_gray)
		# for (ex,ey,ew,eh) in subitems:
		# 	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    # Display the resulting frame
	# cv2.imshow('frame',frame)
	cv2.imshow('IPWebcam',img)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

# When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
