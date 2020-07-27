# face-detection-using-OpenCV

The objective of the program given is to detect object of interest(face) in real time and to keep tracking of the same object with label using mobile camera.

<h4>Note: Please download android mobile app named IP Webcam. Then set your IP address shown in app to URL variable section</h4>

## OpenCV

- OpenCV is the most popular library for computer vision. Originally written in C/C++, it now provides bindings for Python.<br>
- OpenCV uses cascades.Like a series of waterfalls, the OpenCV cascade breaks the problem of detecting faces into multiple stages. For each block, it does a very rough and quick   
  test. If that passes, it does a slightly more detailed test, and so on. The algorithm may have 30 to 50 of these stages or cascades, and it will only detect a face if all stages   pass.<br>
- The cascades themselves are just a bunch of XML files that contain OpenCV data used to detect objects. You initialize your code with the cascade you want, and then it does the  
  work for you.<br>
- Since face detection is such a common case, OpenCV comes with a number of built-in cascades for detecting everything from faces to eyes to hands to legs.<br>

<h6>Steps for implementation :</h6>
 - Install requirements.<br>
 - click your picture from various angles with good quality.<br>
 - put those pictures into a folder named your-name.<br>
 - then run faces-train.py python file (it is faster).<br>
 - after that run faces.py  <br>
 - Now the webcam will be opened and it will detect your face with the label.<br>
 
 # Thank You.

