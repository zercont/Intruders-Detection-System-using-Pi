#!/usr/bin/python             # This is server.py file
import socket                 # Import socket module
import time
from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
pir = MotionSensor(4)
def led_blink():
    print " Wait For Intruders "
    pir.wait_for_motion()
    filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
    camera.start_recording(filename)
    print "Intruders Detected!!!! And Start Recording"
    pir.wait_for_no_motion()
    camera.stop_recording()


s = socket.socket()           # Create a socket object
host = "192.168.43.225"        # Get local machine name
port = 8000                  # Port
s.bind((host, port))          # Bind to the port
s.listen(5)                   # Now wait for client connection.
print "Server is Running Now"
while True:
    c, addr = s.accept()       # Establish connection with client.
    print 'Got connection from', addr
    msg = c.recv(1024)
    msg1 = "10"
    if msg == msg1:
        led_blink()
    print msg
c.close()
