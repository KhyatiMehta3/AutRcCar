# AutRcCar
This is an autonomous RC car using Raspberry Pi model 3 B+, Motor-driver L293d, Ultrasonic-sensor- HCSR04 and Picamera, along with OpenCV.
# Components:
1. Raspberry Pi 3 B,
2. Pi camera,
3. L293d motor driver,
4. Old RC car or 2 DC motors and wheels,
5. 9V battery for the motors,
6. Power Bank for the raspberry pi.
# Hardware :
![alt text](https://github.com/KhyatiMehta3/AutRcCar/blob/master/Connections.png)
## Description of Connections :
1. Red - Power-Positive.
2. Black - Ground.
3. Blue & Purple - Connections from l293d to Raspberry Pi.
4. Ochre - Connections HC SR-04 Ultrasonic Sensor to Raspberry pi.
5. Orange - Connections to the motors.

L293d       | Raspberry Pi 3B+:
------------|------------------
Pin1        | Pin13
Pin2        | Pin3
Pin3        | Motor1
Pin4,5,12,13| Pin9
Pin6        | Motor2
Pin7        | Pin5
Pin8        | 9v Power
pin9        | Pin15
Pin10       | Pin7
Pin11       | Motor3.
Pin14       | Motor4.
Pin15       | Pin11.
Pin16       | Pin2.

---------------------------------------------------------------------------------------------------------------------------------------
# Software :
## Steps to train the car:
The flask folder contains all the required files to control the pi car from any device (connected to the same network) using a browser, while streaming the camera data.
1. SSH into your raspberry pi and go to the flask folder.
2. Run python app.py and open the browser on another device. Type in your raspberry pi's IP address:5000 (which is the default port. Can be changed.)
3. Drive your car around while recording the camera stream from RPi_Cam_Web_Interface cloned and installed from Github. Link - https://github.com/silvanmelchior/RPi_Cam_Web_Interface
4. Run "Opencv_vid2.py" - convert video to images and save it in "TrainingData" folder.
5. Sort out the images of left direction into folder named "left", images of right direction into the folder named "Right" and so on.
6. Open and run the "trainer.py" file to convert the sorted images into numpy array and accordingly label them, using another file called label_images.py. After labeling, the npz file is saved and file name along with image count is returned to trainer.py file, where the training data gets split into 80:20 ratio. The model can be trained on 80% of the data and tested on the rest 20% data. This is good practice. Function "dataSplitter()" does this job.
7. npz file will be saved in "training_data_temp" folder.
8. Use the file "csv1.py" to convert npz file into csv format in case required to debug.

Direction | Labels
----------|--------
Left      | [1 0 0 0]
Forward   | [0 1 0 0]
Right     | [0 0 1 0]
Reverse   | [0 0 0 1]

9. The model gets saved in mlp_xml folder.
## Steps to deploy the model on the pi:
1. Transfer the saved xml model to the pi. 
  -On Windows, use WinSCP software for really quick transfer of mlp.xml files. 
  -On linux, you can directly use scp command after SSH into pi.
2. cd into your directory where this repo is cloned.
3. Copy the filename of your xml file and paste it at the neuralnet() object initialization.
4. Run Python3 Autodriver.py to run the car autonomously.
