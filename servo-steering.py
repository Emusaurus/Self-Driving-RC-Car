import RPi.GPIO as GPIO
from time import sleep
import turtle

servoPIN  = 4
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 PWM with 50Hz
p.start(2.5) # Initialize

#  On clientside keypress a:
#    p.ChangeDutyCycle(45)

#  On evserver keypress d:
#    p.ChangeDutyCycle(-45)