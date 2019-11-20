import RPi.GPIO as GPIO  #for outputting
from datetime import datetime
from time import sleep, gmtime, strftime
import yaml  #for settings file

datetime.now().strftime('%H:%M:%S')  #set time format
GPIO.setmode(GPIO.BCM)  #using broadcom chip's pinouts
GPIO.setup(2, GPIO.OUT)  #2 is an output
GPIO.setup(0, GPIO.OUT)  #0 is an output
speed = 5  #ft/s speed of the car (used in timed driving)

#       ^
# Change this variable


def inputError():
    print('Invalaid input')


def forward():
    GPIO.output(2, 0)  # send positive to positive
    GPIO.output(0, 1)  # send negative to negative


def reverse():
    print(gmtime(), "- going backwards")
    GPIO.output(2, 1)  # send negative to positive
    GPIO.output(0, 0)  # send positive to negative


def forwardtimed():
    length = int(input("Ft to move: "))
    if length <= 0:
        inputError()
    if length > 1000:
        inputError()
    timing = length / speed
    print(gmtime(), "- going forwards for ", timing, " seconds")
    GPIO.output(2, 1)  # send positive to positive
    GPIO.output(0, 0)  # send negative to negative
    time.sleep(timing)
    GPIO.output(2, 0)  # send negative to positive, stops motor.
    GPIO.output(0, 0)  # send negative to negative


#length = int(input("Ft to move: "))
#if length < 0:
#  print('Invalaid input')
#timing = length/speed
