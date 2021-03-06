__author__ = 'kkm'
''' This file takes ultrasonic reading connected in GPIO 12, 16 and returns distance of object from the car.
'''
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
TRIG = 12
ECHO = 16
def distance():
  gpio.setmode(gpio.BOARD)
  gpio.setup(TRIG, gpio.OUT)
  gpio.setup(ECHO, gpio.IN)

  gpio.output(TRIG, False)
  time.sleep(2)
  gpio.output(TRIG, True)
  time.sleep(0.00001)
  gpio.output(TRIG, False)

  while gpio.input(ECHO) == 0:
    start = time.time()
  while gpio.input(ECHO) == 1:
    end = time.time()
  t = end - start
  dist = t * 17150
  dist = round(dist, 2)
  return dist
